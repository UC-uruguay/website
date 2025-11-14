<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST');
header('Access-Control-Allow-Headers: Content-Type');

$dataFile = 'chabashira_data.json';

// データファイルが存在しない場合は作成
if (!file_exists($dataFile)) {
    file_put_contents($dataFile, json_encode([]));
}

// GET: スコアリストを取得
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    $data = json_decode(file_get_contents($dataFile), true);

    // 個数の多い順にソート
    usort($data, function($a, $b) {
        return $b['count'] - $a['count'];
    });

    echo json_encode($data);
    exit;
}

// POST: スコアを投稿
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $input = json_decode(file_get_contents('php://input'), true);
    $data = json_decode(file_get_contents($dataFile), true);

    if (isset($input['action']) && $input['action'] === 'post') {
        $newScore = [
            'id' => uniqid(),
            'name' => htmlspecialchars($input['name']),
            'count' => intval($input['count']),
            'timestamp' => time()
        ];
        $data[] = $newScore;
        file_put_contents($dataFile, json_encode($data));
        echo json_encode(['success' => true, 'score' => $newScore]);
        exit;
    }
}
?>
