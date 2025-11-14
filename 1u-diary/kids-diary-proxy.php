<?php
/**
 * いちゆう日記レコーダー プロキシエンドポイント
 *
 * Mixed Contentエラーを回避するため、WordPressサーバー経由でn8nにアクセス
 *
 * 使い方: functions.phpに以下を追加
 * require_once get_stylesheet_directory() . '/kids-diary-proxy.php';
 */

function kids_diary_proxy_endpoint() {
    // プロキシエンドポイントを登録
    register_rest_route('kids-diary/v1', '/proxy', array(
        'methods' => 'POST',
        'callback' => 'kids_diary_proxy_handler',
        'permission_callback' => '__return_true', // 認証不要（公開エンドポイント）
    ));
}
add_action('rest_api_init', 'kids_diary_proxy_endpoint');

function kids_diary_proxy_handler($request) {
    // n8nのWebhook URL（サーバー側からHTTPでアクセス）
    $n8n_webhook_url = 'http://35.200.56.246:5678/webhook/kids-diary-audio';

    // アップロードされたファイルを取得
    $files = $request->get_file_params();
    $body_params = $request->get_body_params();

    // エラーログ用
    error_log('[Kids Diary Proxy] リクエスト受信');
    error_log('[Kids Diary Proxy] Files: ' . print_r(array_keys($files), true));
    error_log('[Kids Diary Proxy] Params: ' . print_r($body_params, true));

    // cURLでn8nに転送
    $ch = curl_init();

    // マルチパート/フォームデータを構築
    $post_fields = array();

    // ファイルを追加（フィールド名は'data'）
    if (isset($files['data'])) {
        $audio_file = $files['data'];

        // 一時ファイルの場合はCURLFileとして追加
        if (isset($audio_file['tmp_name']) && file_exists($audio_file['tmp_name'])) {
            $filename = $audio_file['name'];
            $mime_type = $audio_file['type'];

            // ファイル名がUUID形式や拡張子なしの場合は修正（webm固定）
            if (!preg_match('/\.(webm|mp3|mp4|wav|m4a|ogg)$/i', $filename)) {
                $filename = 'kids-diary.webm';
            }

            // MIMEタイプが正しくない場合は修正
            if (strpos($mime_type, 'audio/') === false && strpos($mime_type, 'video/') === false) {
                $mime_type = 'audio/webm';
            }

            $post_fields['data'] = new CURLFile(
                $audio_file['tmp_name'],
                $mime_type,
                $filename
            );
            error_log('[Kids Diary Proxy] 音声ファイル追加: ' . $filename . ' (type: ' . $mime_type . ', size: ' . filesize($audio_file['tmp_name']) . ' bytes)');
        }
    }

    // その他のフィールドを追加
    if (isset($body_params['child_name'])) {
        $post_fields['child_name'] = $body_params['child_name'];
    }
    if (isset($body_params['date'])) {
        $post_fields['date'] = $body_params['date'];
    }

    // cURLオプション設定
    curl_setopt_array($ch, array(
        CURLOPT_URL => $n8n_webhook_url,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => $post_fields,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_TIMEOUT => 300, // 5分（音声処理に時間がかかる場合を考慮）
        CURLOPT_SSL_VERIFYPEER => false, // HTTPなのでSSL検証不要
        CURLOPT_HTTPHEADER => array(
            'Accept: application/json',
        ),
    ));

    // リクエスト実行
    $response = curl_exec($ch);
    $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    $curl_error = curl_error($ch);
    curl_close($ch);

    error_log('[Kids Diary Proxy] n8nレスポンス: HTTP ' . $http_code);
    error_log('[Kids Diary Proxy] レスポンスボディ: ' . substr($response, 0, 500));

    // エラーチェック
    if ($curl_error) {
        error_log('[Kids Diary Proxy] cURLエラー: ' . $curl_error);
        return new WP_Error('proxy_error', 'n8nへの接続に失敗しました: ' . $curl_error, array('status' => 500));
    }

    // レスポンスをJSONとしてパース
    $response_data = json_decode($response, true);

    if (json_last_error() !== JSON_ERROR_NONE) {
        error_log('[Kids Diary Proxy] JSON解析エラー: ' . json_last_error_msg());
        // JSONでない場合はそのまま返す
        return new WP_REST_Response(
            array(
                'ok' => ($http_code >= 200 && $http_code < 300),
                'status' => $http_code,
                'message' => $response,
            ),
            $http_code
        );
    }

    // 成功レスポンスを返す
    return new WP_REST_Response($response_data, $http_code);
}

// デバッグ用：エンドポイントのURLを表示
function kids_diary_show_proxy_url() {
    if (is_user_logged_in() && current_user_can('manage_options')) {
        $proxy_url = rest_url('kids-diary/v1/proxy');
        error_log('[Kids Diary Proxy] プロキシURL: ' . $proxy_url);
    }
}
add_action('init', 'kids_diary_show_proxy_url');
