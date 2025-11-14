<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST');
header('Access-Control-Allow-Headers: Content-Type');

$dataFile = 'voices_data.json';
$uploadDir = 'uploads/';

// アップロードディレクトリを作成
if (!file_exists($uploadDir)) {
    mkdir($uploadDir, 0777, true);
}

// データファイルが存在しない場合は作成
if (!file_exists($dataFile)) {
    file_put_contents($dataFile, json_encode([]));
}

// GET: 投稿リストを取得
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    $data = json_decode(file_get_contents($dataFile), true);

    // 新しい順にソート
    usort($data, function($a, $b) {
        return $b['timestamp'] - $a['timestamp'];
    });

    echo json_encode($data);
    exit;
}

// POST: 投稿を追加
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // 通常のフォームデータとして受信
    $name = htmlspecialchars($_POST['name'] ?? '');
    $message = htmlspecialchars($_POST['message'] ?? '');
    $sns = htmlspecialchars($_POST['sns'] ?? '');

    $photoPath = '';

    // 画像アップロード処理
    if (isset($_FILES['photo']) && $_FILES['photo']['error'] === UPLOAD_ERR_OK) {
        $allowedTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif'];
        $fileType = $_FILES['photo']['type'];

        if (in_array($fileType, $allowedTypes)) {
            $extension = pathinfo($_FILES['photo']['name'], PATHINFO_EXTENSION);
            $filename = uniqid() . '.' . $extension;
            $destination = $uploadDir . $filename;

            if (move_uploaded_file($_FILES['photo']['tmp_name'], $destination)) {
                $photoPath = $destination;
            }
        }
    }

    $data = json_decode(file_get_contents($dataFile), true);

    $newVoice = [
        'id' => uniqid(),
        'name' => $name,
        'message' => $message,
        'sns' => $sns,
        'photo' => $photoPath,
        'timestamp' => time()
    ];

    $data[] = $newVoice;
    file_put_contents($dataFile, json_encode($data));

    echo json_encode(['success' => true, 'voice' => $newVoice]);
    exit;
}
?>
