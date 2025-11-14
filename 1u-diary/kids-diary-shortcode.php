<?php
/**
 * いちゆう日記レコーダー ショートコード
 *
 * 使い方: functions.phpに以下を追加
 * require_once get_stylesheet_directory() . '/kids-diary-shortcode.php';
 *
 * ページには [kids_diary_recorder] を記述
 */

// JavaScriptの登録
function kids_diary_enqueue_scripts() {
    // スクリプトを登録（まだ読み込まない）
    wp_register_script(
        'kids-diary-recorder',
        get_stylesheet_directory_uri() . '/kids-diary-recorder.js',
        array(),
        '1.0.0',
        true // フッターで読み込む
    );
}
add_action('wp_enqueue_scripts', 'kids_diary_enqueue_scripts');

function kids_diary_recorder_shortcode($atts) {
    // 属性を取得（webhook_urlを指定可能に）
    // デフォルトはWordPressのプロキシエンドポイント（HTTPSで安全）
    $atts = shortcode_atts(array(
        'webhook_url' => rest_url('kids-diary/v1/proxy'),
    ), $atts);

    // スクリプトを読み込む
    wp_enqueue_script('kids-diary-recorder');

    // 一意のIDを生成（同じページに複数設置する場合のため）
    $unique_id = 'kids_diary_' . uniqid();

    // HTMLを出力
    ob_start();
    ?>
    <div id="<?php echo esc_attr($unique_id); ?>_recorder"
         class="kids-diary-recorder"
         data-unique-id="<?php echo esc_attr($unique_id); ?>"
         data-webhook-url="<?php echo esc_attr($atts['webhook_url']); ?>"
         style="max-width:520px;margin:20px auto;padding:16px;border:1px solid #ddd;border-radius:12px;">

        <h3 style="margin:0 0 12px;">いちゆう日記 レコーダー</h3>

        <button id="<?php echo esc_attr($unique_id); ?>_btnToggle"
                style="padding:12px 18px;border-radius:10px;cursor:pointer;border:1px solid #ccc;background:#f0f0f0;">
            🎙️ 録音開始
        </button>

        <div id="<?php echo esc_attr($unique_id); ?>_status" style="margin-top:12px;color:#555;">
            準備OK（HTTPS必須）
        </div>

        <audio id="<?php echo esc_attr($unique_id); ?>_preview"
               controls
               style="width:100%;margin-top:8px;display:none;">
        </audio>

        <div id="<?php echo esc_attr($unique_id); ?>_result" style="margin-top:8px;">
        </div>
    </div>
    <?php
    return ob_get_clean();
}

add_shortcode('kids_diary_recorder', 'kids_diary_recorder_shortcode');
