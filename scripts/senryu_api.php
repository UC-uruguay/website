<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST');
header('Access-Control-Allow-Headers: Content-Type');

$dataFile = 'senryu_data.json';

// データファイルが存在しない場合は作成
if (!file_exists($dataFile)) {
    file_put_contents($dataFile, json_encode([]));
}

// GET: 川柳リストを取得
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    $data = json_decode(file_get_contents($dataFile), true);
    echo json_encode($data);
    exit;
}

// POST: 川柳を投稿 or いいね
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $input = json_decode(file_get_contents('php://input'), true);
    $data = json_decode(file_get_contents($dataFile), true);

    // 川柳を投稿
    if (isset($input['action']) && $input['action'] === 'post') {
        $newSenryu = [
            'id' => uniqid(),
            'author' => htmlspecialchars($input['author']),
            'text' => htmlspecialchars($input['text']),
            'likes' => 0,
            'timestamp' => time()
        ];
        $data[] = $newSenryu;
        file_put_contents($dataFile, json_encode($data));
        echo json_encode(['success' => true, 'senryu' => $newSenryu]);
        exit;
    }

    // いいねを追加
    if (isset($input['action']) && $input['action'] === 'like') {
        $id = $input['id'];
        foreach ($data as &$senryu) {
            if ($senryu['id'] === $id) {
                $senryu['likes']++;
                break;
            }
        }
        file_put_contents($dataFile, json_encode($data));
        echo json_encode(['success' => true]);
        exit;
    }
}
?>
