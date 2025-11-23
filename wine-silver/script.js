// ===== コンテンツカードのトグル機能 =====
function toggleContent(id) {
    const content = document.getElementById(id);
    const button = content.previousElementSibling.querySelector('.toggle-btn');

    if (content.classList.contains('active')) {
        content.classList.remove('active');
        button.textContent = '▼';
    } else {
        content.classList.add('active');
        button.textContent = '▲';
    }
}

// ===== クイズ機能 =====
const quizQuestions = [
    {
        question: "ボルドーの主要なブドウ品種の組み合わせとして正しいものは？",
        options: [
            "カベルネ・ソーヴィニヨン、メルロー、カベルネ・フラン",
            "ピノ・ノワール、シャルドネ、ガメイ",
            "シラー、グルナッシュ、ムールヴェードル",
            "リースリング、ミュラー・トゥルガウ、シルヴァーナー"
        ],
        correct: 0
    },
    {
        question: "ブルゴーニュの赤ワインに使用される主要品種は？",
        options: [
            "カベルネ・ソーヴィニヨン",
            "ピノ・ノワール",
            "シラー",
            "メルロー"
        ],
        correct: 1
    },
    {
        question: "シャンパーニュの製法は何と呼ばれる？",
        options: [
            "シャルマ方式",
            "炭酸ガス注入法",
            "メトード・シャンプノワーズ（瓶内二次発酵）",
            "トランスファー方式"
        ],
        correct: 2
    },
    {
        question: "イタリアワインの最高品質保証格付けは？",
        options: [
            "DOC",
            "DOCG",
            "IGT",
            "VDT"
        ],
        correct: 1
    },
    {
        question: "バローロとバルバレスコに使用される主要品種は？",
        options: [
            "サンジョヴェーゼ",
            "バルベーラ",
            "ネッビオーロ",
            "モンテプルチャーノ"
        ],
        correct: 2
    },
    {
        question: "スペインのリオハで主に使用される品種は？",
        options: [
            "テンプラニーリョ",
            "ガルナッチャ",
            "モナストレル",
            "カベルネ・ソーヴィニヨン"
        ],
        correct: 0
    },
    {
        question: "ドイツワインの品質分類で、最も遅く収穫されるのは？",
        options: [
            "Kabinett",
            "Spätlese",
            "Auslese",
            "Trockenbeerenauslese"
        ],
        correct: 3
    },
    {
        question: "日本を代表する白ブドウ品種は？",
        options: [
            "マスカット・ベーリーA",
            "甲州",
            "デラウェア",
            "シャルドネ"
        ],
        correct: 1
    },
    {
        question: "ワインのテイスティングの正しい順序は？",
        options: [
            "香り → 外観 → 味わい",
            "外観 → 味わい → 香り",
            "外観 → 香り → 味わい",
            "味わい → 香り → 外観"
        ],
        correct: 2
    },
    {
        question: "スパークリングワインの適正温度は？",
        options: [
            "16-18℃",
            "12-14℃",
            "8-12℃",
            "6-8℃"
        ],
        correct: 3
    },
    {
        question: "プロセッコの製造方法は？",
        options: [
            "瓶内二次発酵",
            "シャルマ方式（タンク内二次発酵）",
            "炭酸ガス注入法",
            "メトード・アンセストラル"
        ],
        correct: 1
    },
    {
        question: "キャンティ・クラシコの主要品種は？",
        options: [
            "ネッビオーロ",
            "バルベーラ",
            "サンジョヴェーゼ",
            "モンテプルチャーノ"
        ],
        correct: 2
    },
    {
        question: "ポートワインの産地は？",
        options: [
            "スペイン・ヘレス",
            "ポルトガル・ドウロ",
            "イタリア・シチリア",
            "フランス・ローヌ"
        ],
        correct: 1
    },
    {
        question: "赤ワインと白ワインの製造における最大の違いは？",
        options: [
            "使用するブドウの種類",
            "発酵温度",
            "果皮と共に発酵するかどうか",
            "熟成期間"
        ],
        correct: 2
    },
    {
        question: "ブラン・ド・ブランとは何を意味する？",
        options: [
            "白ブドウのみから造られたシャンパーニュ",
            "黒ブドウのみから造られたシャンパーニュ",
            "ロゼのシャンパーニュ",
            "甘口のシャンパーニュ"
        ],
        correct: 0
    }
];

let currentQuestionIndex = 0;
let correctAnswers = 0;
let totalQuestions = 0;
let usedQuestions = [];

function startQuiz() {
    currentQuestionIndex = 0;
    correctAnswers = 0;
    totalQuestions = 0;
    usedQuestions = [];
    document.getElementById('correct-count').textContent = '0';
    document.getElementById('total-count').textContent = '0';
    document.getElementById('result-display').textContent = '';
    loadQuestion();
}

function loadQuestion() {
    if (usedQuestions.length === quizQuestions.length) {
        // すべての問題が終了
        document.getElementById('question-display').innerHTML =
            `<p class="question-text">すべての問題が終了しました！<br>正解数: ${correctAnswers} / ${totalQuestions}<br>正答率: ${Math.round((correctAnswers/totalQuestions)*100)}%</p>`;
        document.getElementById('options-display').innerHTML = '';
        document.getElementById('next-btn').style.display = 'none';
        document.querySelector('.quiz-controls button:first-child').style.display = 'inline-block';
        return;
    }

    // ランダムに未使用の問題を選択
    let randomIndex;
    do {
        randomIndex = Math.floor(Math.random() * quizQuestions.length);
    } while (usedQuestions.includes(randomIndex));

    usedQuestions.push(randomIndex);
    const question = quizQuestions[randomIndex];

    document.getElementById('question-display').innerHTML =
        `<p class="question-text">${question.question}</p>`;

    const optionsHtml = question.options.map((option, index) =>
        `<button class="option-btn" onclick="checkAnswer(${randomIndex}, ${index})">${option}</button>`
    ).join('');

    document.getElementById('options-display').innerHTML = optionsHtml;
    document.getElementById('result-display').textContent = '';
    document.getElementById('next-btn').style.display = 'none';
    document.querySelector('.quiz-controls button:first-child').style.display = 'none';
}

function checkAnswer(questionIndex, selectedIndex) {
    const question = quizQuestions[questionIndex];
    const buttons = document.querySelectorAll('.option-btn');

    totalQuestions++;

    buttons.forEach((btn, index) => {
        btn.disabled = true;
        if (index === question.correct) {
            btn.classList.add('correct');
        } else if (index === selectedIndex) {
            btn.classList.add('incorrect');
        }
    });

    if (selectedIndex === question.correct) {
        correctAnswers++;
        document.getElementById('result-display').innerHTML =
            '<span style="color: #4caf50;">✓ 正解！</span>';
    } else {
        document.getElementById('result-display').innerHTML =
            '<span style="color: #f44336;">✗ 不正解</span>';
    }

    document.getElementById('correct-count').textContent = correctAnswers;
    document.getElementById('total-count').textContent = totalQuestions;
    document.getElementById('next-btn').style.display = 'inline-block';
}

function nextQuestion() {
    loadQuestion();
}

// ===== フラッシュカード機能 =====
const flashcards = [
    { front: "ボルドーの主要品種（赤）", back: "カベルネ・ソーヴィニヨン、メルロー、カベルネ・フラン" },
    { front: "ブルゴーニュの主要品種（赤）", back: "ピノ・ノワール" },
    { front: "ブルゴーニュの主要品種（白）", back: "シャルドネ" },
    { front: "シャンパーニュの製法", back: "メトード・シャンプノワーズ（瓶内二次発酵）" },
    { front: "イタリアの最高品質格付け", back: "DOCG（デノミナツィオーネ・ディ・オリージネ・コントロッラータ・エ・ガランティータ）" },
    { front: "バローロの主要品種", back: "ネッビオーロ" },
    { front: "キャンティの主要品種", back: "サンジョヴェーゼ" },
    { front: "リオハの主要品種", back: "テンプラニーリョ" },
    { front: "ポートワインの産地", back: "ポルトガル・ドウロ地方" },
    { front: "ドイツの代表的白品種", back: "リースリング" },
    { front: "日本の代表的白品種", back: "甲州" },
    { front: "日本の代表的赤品種", back: "マスカット・ベーリーA" },
    { front: "プロセッコの製法", back: "シャルマ方式（タンク内二次発酵）" },
    { front: "ブラン・ド・ブランの意味", back: "白ブドウのみから造られたシャンパーニュ" },
    { front: "ブラン・ド・ノワールの意味", back: "黒ブドウのみから造られた白またはロゼのシャンパーニュ" },
    { front: "マロラクティック発酵の効果", back: "リンゴ酸を乳酸に変換し、酸味をまろやかにする" },
    { front: "テロワールの意味", back: "土壌、気候、地形などブドウ栽培に影響を与える環境要因の総称" },
    { front: "タンニンの主な特徴", back: "渋みを与え、赤ワインの骨格を形成。主に果皮、種、樽から抽出" },
    { front: "スパークリングワインの適正温度", back: "6-8℃" },
    { front: "フルボディ赤ワインの適正温度", back: "16-18℃" }
];

let currentCardIndex = 0;

function startFlashcards() {
    currentCardIndex = 0;
    updateFlashcard();
    document.getElementById('total-cards').textContent = flashcards.length;
}

function updateFlashcard() {
    const card = flashcards[currentCardIndex];
    document.getElementById('card-front').textContent = card.front;
    document.getElementById('card-back').textContent = card.back;
    document.getElementById('current-card').textContent = currentCardIndex + 1;

    // カードをリセット（表面に戻す）
    const flashcard = document.getElementById('flashcard');
    flashcard.classList.remove('flipped');
}

function flipCard() {
    const flashcard = document.getElementById('flashcard');
    flashcard.classList.toggle('flipped');
}

function nextCard() {
    if (currentCardIndex < flashcards.length - 1) {
        currentCardIndex++;
        updateFlashcard();
    }
}

function prevCard() {
    if (currentCardIndex > 0) {
        currentCardIndex--;
        updateFlashcard();
    }
}

// ===== 進捗管理機能 =====
let progressData = {
    france: 0,
    italy: 0,
    spain: 0,
    germany: 0,
    japan: 0,
    grapes: 0,
    tasting: 0
};

// ローカルストレージから進捗を読み込む
function loadProgress() {
    const saved = localStorage.getItem('wineStudyProgress');
    if (saved) {
        progressData = JSON.parse(saved);
        updateAllProgress();
    }
}

// 進捗を保存
function saveProgress() {
    localStorage.setItem('wineStudyProgress', JSON.stringify(progressData));
}

// 進捗を更新
function updateProgress(category, maxValue) {
    if (progressData[category] < maxValue) {
        progressData[category] = Math.min(progressData[category] + maxValue, maxValue);
        saveProgress();
        updateAllProgress();
    }
}

// すべての進捗バーを更新
function updateAllProgress() {
    const categories = ['france', 'italy', 'spain', 'germany', 'japan', 'grapes', 'tasting'];
    const maxValues = {
        france: 20,
        italy: 20,
        spain: 15,
        germany: 15,
        japan: 10,
        grapes: 10,
        tasting: 10
    };

    categories.forEach(category => {
        const percentage = (progressData[category] / maxValues[category]) * 100;
        const element = document.getElementById(`progress-${category}`);
        if (element) {
            element.style.width = percentage + '%';
        }
    });

    // 全体の進捗を計算
    const totalMax = Object.values(maxValues).reduce((a, b) => a + b, 0);
    const totalProgress = Object.values(progressData).reduce((a, b) => a + b, 0);
    const totalPercentage = (totalProgress / totalMax) * 100;

    document.getElementById('progress-total').style.width = totalPercentage + '%';
    document.getElementById('total-percentage').textContent = Math.round(totalPercentage);
}

// 進捗をリセット
function resetProgress() {
    if (confirm('進捗をリセットしてもよろしいですか？')) {
        progressData = {
            france: 0,
            italy: 0,
            spain: 0,
            germany: 0,
            japan: 0,
            grapes: 0,
            tasting: 0
        };
        saveProgress();
        updateAllProgress();
    }
}

// ページ読み込み時に進捗を復元
window.addEventListener('DOMContentLoaded', () => {
    loadProgress();
});

// スムーススクロール
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});
