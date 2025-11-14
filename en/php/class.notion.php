<?php

class NotionAPI {
    private $token;
    private $database_id;
    private $api_url = 'https://api.notion.com/v1';
    
    public function __construct($token, $database_id) {
        $this->token = $token;
        // データベースIDからハイフンを除去（念のため）
        $this->database_id = str_replace('-', '', $database_id);
    }
    
    public function createPage($data) {
        $url = $this->api_url . '/pages';
        
        // 現在の日時を取得
        $current_datetime = date('Y-m-d\TH:i:s.000\Z', strtotime('-9 hours')); // UTCに変換
        
        $body = [
            'parent' => [
                'type' => 'database_id',
                'database_id' => $this->database_id
            ],
            'properties' => [
                '企業名' => [
                    'rich_text' => [
                        [
                            'text' => [
                                'content' => $data['company'] ?? '企業名未入力'
                            ]
                        ]
                    ]
                ],
                '案件名' => [
                    'title' => [
                        [
                            'text' => [
                                'content' => '【ヨガページ（英語）】' . ($data['company'] ?? '企業名未入力')
                            ]
                        ]
                    ]
                ],
                '先方連絡先' => [
                    'rich_text' => [
                        [
                            'text' => [
                                'content' => ($data['mail_address'] ?? '') . ' / ' . ($data['phone'] ?? '')
                            ]
                        ]
                    ]
                ],
                '資料請求ステータス' => [
                    'select' => [
                        'name' => '資料請求：0.新規'
                    ]
                ],
                '問い合わせルート' => [
                    'select' => [
                        'name' => '資料請求'
                    ]
                ],
                '資料請求詳細' => [
                    'rich_text' => [
                        [
                            'text' => [
                                'content' => $this->formatAllFormData($data)
                            ]
                        ]
                    ]
                ]
            ]
        ];
        
        $ch = curl_init($url);
        curl_setopt($ch, CURLOPT_HTTPHEADER, [
            'Authorization: Bearer ' . $this->token,
            'Content-Type: application/json',
            'Notion-Version: 2022-06-28'
        ]);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($body));
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        
        $response = curl_exec($ch);
        $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        $error = curl_error($ch);
        curl_close($ch);
        
        if ($error) {
            throw new Exception('cURL Error: ' . $error);
        }
        
        if ($http_code !== 200) {
            $response_data = json_decode($response, true);
            throw new Exception('Notion API Error: ' . ($response_data['message'] ?? 'Unknown error') . ' (HTTP ' . $http_code . ')');
        }
        
        return json_decode($response, true);
    }
    
    private function formatAllFormData($data) {
        $formatted = [];
        $formatted[] = '【問い合わせ元】ヨガページ（英語）からのお問い合わせ';
        $formatted[] = '【送信時刻】' . date('Y年m月d日　H時i分s秒');
        
        if (!empty($data['company'])) {
            $formatted[] = '【会社名】' . $data['company'];
        }
        if (!empty($data['position'])) {
            $formatted[] = '【役職】' . $data['position'];
        }
        if (!empty($data['name_1'])) {
            $formatted[] = '【お名前】' . $data['name_1'];
        }
        if (!empty($data['mail_address'])) {
            $formatted[] = '【メールアドレス】' . $data['mail_address'];
        }
        if (!empty($data['phone'])) {
            $formatted[] = '【電話番号】' . $data['phone'];
        }
        
        return implode("\n", $formatted);
    }
} 