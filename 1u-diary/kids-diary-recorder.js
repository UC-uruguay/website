/**
 * いちゆう日記レコーダー JavaScript
 */
(function() {
    // DOMの読み込み完了を待つ
    function initRecorder() {
        var recorderEl = document.querySelector('.kids-diary-recorder');
        if (!recorderEl) return;

        var uniqueId = recorderEl.getAttribute('data-unique-id');
        var btnToggle = document.getElementById(uniqueId + '_btnToggle');
        var statusEl = document.getElementById(uniqueId + '_status');
        var audioEl = document.getElementById(uniqueId + '_preview');
        var resultEl = document.getElementById(uniqueId + '_result');
        var webhookUrl = recorderEl.getAttribute('data-webhook-url');

        var mediaRecorder, chunks = [], stream, recording = false, mimeType, ext;

        function setStatus(t) {
            statusEl.textContent = t;
        }

        function ymdTokyo() {
            var d = new Date();
            var y = new Intl.DateTimeFormat('ja-JP', {year:'numeric', timeZone:'Asia/Tokyo'}).format(d);
            var m = new Intl.DateTimeFormat('ja-JP', {month:'2-digit', timeZone:'Asia/Tokyo'}).format(d);
            var dd = new Intl.DateTimeFormat('ja-JP', {day:'2-digit', timeZone:'Asia/Tokyo'}).format(d);
            return y + '/' + m + '/' + dd;
        }

        function startRecording() {
            navigator.mediaDevices.getUserMedia({ audio: true })
                .then(function(s) {
                    stream = s;
                    chunks = [];

                    // webm固定で録音（Chromeで最適、OpenAI Whisper対応）
                    mimeType = 'audio/webm';
                    ext = 'webm';

                    mediaRecorder = new MediaRecorder(stream, { mimeType: 'audio/webm' });

                    mediaRecorder.ondataavailable = function(e) {
                        if (e.data.size > 0) chunks.push(e.data);
                    };

                    mediaRecorder.onstop = onStop;
                    mediaRecorder.start();
                    recording = true;
                    btnToggle.textContent = '⏹️ 録音停止';
                    setStatus('録音中…話し終わったら「録音停止」を押してください');

                    setTimeout(function() {
                        if (mediaRecorder && mediaRecorder.state === 'recording') {
                            stopRecording();
                        }
                    }, 5 * 60 * 1000);
                })
                .catch(function(e) {
                    console.error(e);
                    setStatus('マイクの許可が必要です（HTTPS必須）。');
                });
        }

        function stopRecording() {
            if (mediaRecorder && mediaRecorder.state === 'recording') {
                mediaRecorder.stop();
                setStatus('処理中…');
            }
        }

        function onStop() {
            try {
                var blob = new Blob(chunks, { type: 'audio/webm' });
                audioEl.src = URL.createObjectURL(blob);
                audioEl.style.display = 'block';

                console.log('[デバッグ] 音声Blob作成完了:', blob.size, 'bytes, type:', blob.type);
                setStatus('音声をアップロード中…');

                var fd = new FormData();
                // Blobを直接ファイル名付きでappend（3番目の引数がファイル名）
                fd.append('data', blob, 'kids-diary.webm');
                fd.append('child_name', 'いちゆう');
                fd.append('date', ymdTokyo());

                console.log('[デバッグ] FormData作成完了: kids-diary.webm (audio/webm)');

                console.log('[デバッグ] Webhook URL:', webhookUrl);
                console.log('[デバッグ] 送信データ: child_name=いちゆう, date=' + ymdTokyo());

                fetch(webhookUrl, { method: 'POST', body: fd })
                    .then(function(res) {
                        console.log('[デバッグ] レスポンスステータス:', res.status, res.statusText);
                        return res.text().then(function(text) {
                            console.log('[デバッグ] レスポンスボディ（生データ）:', text);
                            try {
                                var data = JSON.parse(text);
                                return { res: res, data: data };
                            } catch(e) {
                                console.log('[デバッグ] JSON解析失敗、テキストとして扱います');
                                return { res: res, data: { message: text } };
                            }
                        });
                    })
                    .then(function(result) {
                        console.log('[デバッグ] 処理結果:', result);

                        if (result.res.ok) {
                            setStatus('✅ 公開完了！');
                            if (result.data.link) {
                                resultEl.innerHTML = '<div style="padding:10px;background:#e8f5e9;border-radius:5px;margin-top:10px;">' +
                                    '<strong>投稿成功！</strong><br>' +
                                    '<a href="' + result.data.link + '" target="_blank" rel="noopener" style="color:#2e7d32;">📝 公開ページを開く →</a>' +
                                    '</div>';
                            } else {
                                resultEl.innerHTML = '<div style="padding:10px;background:#fff3cd;border-radius:5px;margin-top:10px;">' +
                                    '⚠️ 投稿されましたが、URLが取得できませんでした<br>' +
                                    '<small>レスポンス: ' + JSON.stringify(result.data) + '</small>' +
                                    '</div>';
                            }
                        } else {
                            setStatus('❌ エラー発生（ステータス: ' + result.res.status + '）');
                            resultEl.innerHTML = '<div style="padding:10px;background:#ffebee;border-radius:5px;margin-top:10px;">' +
                                '<strong>エラー詳細:</strong><br>' +
                                '<small>' + (result.data.message || JSON.stringify(result.data)) + '</small>' +
                                '</div>';
                        }
                    })
                    .catch(function(err) {
                        console.error('[デバッグ] エラー発生:', err);
                        setStatus('❌ 送信に失敗しました');
                        resultEl.innerHTML = '<div style="padding:10px;background:#ffebee;border-radius:5px;margin-top:10px;">' +
                            '<strong>送信エラー:</strong><br>' +
                            '<small>' + err.message + '</small><br>' +
                            '<small>コンソール（F12）で詳細を確認してください</small>' +
                            '</div>';
                    })
                    .finally(function() {
                        try {
                            if (stream) {
                                stream.getTracks().forEach(function(t) { t.stop(); });
                            }
                        } catch(e) {}
                        recording = false;
                        btnToggle.textContent = '🎙️ 録音開始';
                    });
            } catch (err) {
                console.error('[デバッグ] onStop内エラー:', err);
                setStatus('❌ エラーが発生しました');
                resultEl.textContent = 'エラー: ' + err.message;
                recording = false;
                btnToggle.textContent = '🎙️ 録音開始';
            }
        }

        if (btnToggle) {
            btnToggle.addEventListener('click', function() {
                if (!recording) {
                    startRecording();
                } else {
                    stopRecording();
                }
            });
        }

        setStatus('準備OK（HTTPS必須）');
    }

    // DOMContentLoaded または即座に実行
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initRecorder);
    } else {
        initRecorder();
    }
})();
