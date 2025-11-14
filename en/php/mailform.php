<?php


session_start();
error_reporting(0);

mb_language('uni');
mb_internal_encoding('UTF-8');
date_default_timezone_set('Asia/Tokyo');

require_once(dirname(__FILE__) . '/class.mailform.php');
$responsive_mailform = new Mailform();




if (isset($_POST['token_get']) && $_POST['token_get'] !== '') {
    $responsive_mailform->javascript_action_check();
    $responsive_mailform->referer_check();
    $responsive_mailform->token_get();
    exit;
}




if ( file_exists( dirname( __FILE__ ) .'/../addon/confirm/confirm.php' ) ) {
	include( dirname( __FILE__ ) .'/../addon/confirm/confirm.php' );
}




$responsive_mailform->javascript_action_check();
$responsive_mailform->referer_check();
$responsive_mailform->token_check();

if ( file_exists( dirname( __FILE__ ) .'/../addon/csv-record/include/enquete.php' ) ) {
	include( dirname( __FILE__ ) .'/../addon/csv-record/include/enquete.php' );
}

$responsive_mailform->post_check( 'default' );

if ( file_exists( dirname( __FILE__ ) .'/../addon/block/block.php' ) ) {
	include( dirname( __FILE__ ) .'/../addon/block/block.php' );
}

$responsive_mailform->mail_set( 'send' );
$responsive_mailform->mail_set( 'thanks' );

if ( file_exists( dirname( __FILE__ ) .'/../addon/csv-record/include/csv.php' ) ) {
	include( dirname( __FILE__ ) .'/../addon/csv-record/include/csv.php' );
}

$responsive_mailform->mail_send();

// Notion API連携（フォーム送信時のみ実行）
if (!isset($_POST['token_get']) && isset($_POST['javascript_action']) && $_POST['javascript_action'] === 'true') {
    
    // 出力バッファをキャプチャ
    ob_start();
    
    try {
        @require_once(dirname(__FILE__) . '/class.notion.php');
        @require_once(dirname(__FILE__) . '/notion-config.php');
    
        if (!empty($notion_config['database_id'])) {
            try {
                $notion = new NotionAPI($notion_config['token'], $notion_config['database_id']);
                // フォームデータを取得し、oteratraing構造に合わせて整形
                $form_data = [
                    'company'      => $_POST['company'] ?? '',
                    'position'     => $_POST['position'] ?? '',
                    'name_1'       => $_POST['name_1'] ?? '',
                    'mail_address' => $_POST['mail_address'] ?? '',
                    'phone'        => $_POST['phone'] ?? ''
                ];
                $result = $notion->createPage($form_data);
                // 成功ログ（本番環境用に最小限）
                if (isset($result['id']) && isset($notion_log_file)) {
                    @error_log(date('Y-m-d H:i:s') . " - Notion page created (English): " . $result['id'] . "\n", 3, $notion_log_file);
                }
            } catch (Exception $e) {
                // エラーログに記録（メール送信は成功させる）
                if (isset($notion_log_file)) {
                    @error_log(date('Y-m-d H:i:s') . " - Notion API Error (English): " . $e->getMessage() . "\n", 3, $notion_log_file);
                }
            }
        }
    } catch (Exception $e) {
        // Notion連携エラーをログに記録
        @error_log('Notion連携エラー: ' . $e->getMessage());
    }
    
    // 出力バッファをクリア（Notion処理の出力を破棄）
    ob_end_clean();
}

$responsive_mailform->mail_result();

?>