// ===== ハンバーガーメニュー機能 =====
function toggleMenu() {
    const navMenu = document.querySelector('.nav-menu');
    const hamburger = document.querySelector('.hamburger');
    navMenu.classList.toggle('active');
    hamburger.classList.toggle('active');
}

function closeMenu() {
    const navMenu = document.querySelector('.nav-menu');
    const hamburger = document.querySelector('.hamburger');
    navMenu.classList.remove('active');
    hamburger.classList.remove('active');
}

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

// ===== クイズ機能（エキスパートレベル） =====
const quizQuestions = [
    {
        question: "1973年に第2級から第1級に昇格したメドック格付けのシャトーは？",
        options: [
            "シャトー・ムートン・ロートシルト",
            "シャトー・コス・デストゥルネル",
            "シャトー・レオヴィル・ラス・カーズ",
            "シャトー・ピション・ロングヴィル・バロン"
        ],
        correct: 0
    },
    {
        question: "ブルゴーニュで最も多くのグラン・クリュを持つ村は？",
        options: [
            "ヴォーヌ・ロマネ",
            "ジュヴレ・シャンベルタン",
            "シャンボール・ミュジニー",
            "モレ・サン・ドニ"
        ],
        correct: 1
    },
    {
        question: "DRC（ドメーヌ・ド・ラ・ロマネ・コンティ）が単独所有するモノポールのグラン・クリュは？",
        options: [
            "ロマネ・コンティとラ・ターシュ",
            "ロマネ・コンティとリシュブール",
            "ラ・ターシュとロマネ・サン・ヴィヴァン",
            "ロマネ・コンティとグラン・エシェゾー"
        ],
        correct: 0
    },
    {
        question: "シャンパーニュのグラン・クリュ村は全部でいくつ？",
        options: [
            "15村",
            "17村",
            "19村",
            "21村"
        ],
        correct: 1
    },
    {
        question: "バローロのMGA（追加地理的表示）制度で最も有名な畑「カンヌビ」があるコムーネは？",
        options: [
            "ラ・モッラ",
            "バローロ",
            "セッラルンガ・ダルバ",
            "モンフォルテ・ダルバ"
        ],
        correct: 1
    },
    {
        question: "ブルネッロ・ディ・モンタルチーノ DOCGの最低熟成期間（リゼルヴァを除く）は？",
        options: [
            "最低4年（うち2年樽熟成）",
            "最低5年（うち2年樽熟成）",
            "最低5年（うち3年樽熟成）",
            "最低6年（うち2年樽熟成）"
        ],
        correct: 1
    },
    {
        question: "ポート・ワインの「ヴィンテージ・ポート」の最低樽熟成期間は？",
        options: [
            "最低1年",
            "最低2年",
            "最低3年",
            "最低4年"
        ],
        correct: 1
    },
    {
        question: "ドイツワインの品質分類で、Trockenbeerenauslese（TBA）の最低果汁糖度（Öchsle度）は？",
        options: [
            "110-128度",
            "128-150度",
            "150-154度",
            "154度以上"
        ],
        correct: 2
    },
    {
        question: "オーストリアのヴァッハウで最も格が高く、アルコール度数が最も高いカテゴリーは？",
        options: [
            "Steinfeder（シュタインフェーダー）",
            "Federspiel（フェーダーシュピール）",
            "Smaragd（スマラクト）",
            "Auslese（アウスレーゼ）"
        ],
        correct: 2
    },
    {
        question: "カリフォルニアの「パリスの審判（1976年）」で白ワイン部門1位を獲得したワイナリーは？",
        options: [
            "Stag's Leap Wine Cellars",
            "Chateau Montelena",
            "Ridge Vineyards",
            "Heitz Cellar"
        ],
        correct: 1
    },
    {
        question: "オーストラリアのバロッサ・ヴァレーで主に栽培される「GSM」ブレンドの品種の組み合わせは？",
        options: [
            "グルナッシュ、シラーズ、メルロー",
            "グルナッシュ、シラーズ、ムールヴェードル",
            "ガルナッチャ、サンジョヴェーゼ、モナストレル",
            "グルナッシュ、セミヨン、マスカット"
        ],
        correct: 1
    },
    {
        question: "アルゼンチンを代表する白ブドウ品種「トロンテス」の主要産地は？",
        options: [
            "メンドーサ",
            "サルタ",
            "パタゴニア",
            "サン・ファン"
        ],
        correct: 1
    },
    {
        question: "南アフリカ固有の交配品種「ピノタージュ」の親品種は？",
        options: [
            "ピノ・ノワール × カベルネ・ソーヴィニヨン",
            "ピノ・ノワール × サンソー（エルミタージュ）",
            "ピノ・ノワール × シラー",
            "ピノ・グリ × カリニャン"
        ],
        correct: 1
    },
    {
        question: "カベルネ・ソーヴィニヨンの親品種の組み合わせは？",
        options: [
            "カベルネ・フラン × メルロー",
            "カベルネ・フラン × ソーヴィニヨン・ブラン",
            "メルロー × ソーヴィニヨン・ブラン",
            "カベルネ・フラン × シャルドネ"
        ],
        correct: 1
    },
    {
        question: "シャトーヌフ・デュ・パプ AOPで使用可能なブドウ品種は最大何種類？",
        options: [
            "9品種",
            "11品種",
            "13品種",
            "15品種"
        ],
        correct: 2
    },
    {
        question: "リオハ DOCaのグラン・レセルバ（赤）の最低熟成期間は？",
        options: [
            "最低48ヶ月（うち18ヶ月樽熟成）",
            "最低60ヶ月（うち24ヶ月樽熟成）",
            "最低60ヶ月（うち18ヶ月樽熟成）",
            "最低72ヶ月（うち24ヶ月樽熟成）"
        ],
        correct: 1
    },
    {
        question: "アルザスのグラン・クリュは全部でいくつ？",
        options: [
            "47",
            "49",
            "51",
            "53"
        ],
        correct: 2
    },
    {
        question: "プロセッコ DOCG（最高格付け）の生産地域は？",
        options: [
            "ヴァルドッビアーデネ",
            "コネリアーノ・ヴァルドッビアーデネ",
            "アゾロ・モンテッロ",
            "コネリアーノ・ヴァルドッビアーデネとアゾロ・モンテッロ"
        ],
        correct: 3
    },
    {
        question: "マデイラワインの4つの主要品種のうち、最も辛口なのは？",
        options: [
            "セルシアル",
            "ヴェルデーリョ",
            "ボアル",
            "マルムジー"
        ],
        correct: 0
    },
    {
        question: "ニュージーランドで世界最南端のワイン産地として知られるのは？",
        options: [
            "マールボロ",
            "ホークス・ベイ",
            "セントラル・オタゴ",
            "マーティンボロ"
        ],
        correct: 2
    },
    {
        question: "ドイツのVDP格付けで最高峰の畑を表すのは？",
        options: [
            "VDP.GUTSWEIN",
            "VDP.ORTSWEIN",
            "VDP.ERSTE LAGE",
            "VDP.GROSSE LAGE"
        ],
        correct: 3
    },
    {
        question: "シャブリのグラン・クリュは全部でいくつ？",
        options: [
            "5",
            "7",
            "9",
            "11"
        ],
        correct: 1
    },
    {
        question: "ナパ・ヴァレーの中で、1976年「パリスの審判」で赤ワイン部門1位を獲得したワイナリーがあるサブAVAは？",
        options: [
            "ラザフォード",
            "オークヴィル",
            "スタッグス・リープ・ディストリクト",
            "ホーウェル・マウンテン"
        ],
        correct: 2
    },
    {
        question: "「スーパータスカン」の先駆けとなった1970年代のワインで、サンジョヴェーゼとカベルネ・ソーヴィニヨンのブレンドで有名なのは？",
        options: [
            "サッシカイア",
            "ティニャネロ",
            "オルネッライア",
            "ソライア"
        ],
        correct: 1
    },
    {
        question: "コート・ロティの2つの斜面の名前は？",
        options: [
            "コート・ブロンドとコート・ブリュヌ",
            "コート・ノールとコート・シュド",
            "コート・オリエンタルとコート・オクシデンタル",
            "コート・ド・ニュイとコート・ド・ボーヌ"
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
    document.getElementById('quiz-current').textContent = '0';
    document.getElementById('quiz-total').textContent = quizQuestions.length;
    document.getElementById('quiz-progress-fill').style.width = '0%';
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
        `<p class="question-text"><strong>問題 ${usedQuestions.length} / ${quizQuestions.length}</strong><br><br>${question.question}</p>`;

    const optionsHtml = question.options.map((option, index) =>
        `<button class="option-btn" onclick="checkAnswer(${randomIndex}, ${index})">${option}</button>`
    ).join('');

    document.getElementById('options-display').innerHTML = optionsHtml;
    document.getElementById('result-display').textContent = '';
    document.getElementById('next-btn').style.display = 'none';
    document.querySelector('.quiz-controls button:first-child').style.display = 'none';

    // 進捗バーを更新
    document.getElementById('quiz-current').textContent = usedQuestions.length;
    const progressPercentage = (usedQuestions.length / quizQuestions.length) * 100;
    document.getElementById('quiz-progress-fill').style.width = progressPercentage + '%';
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
            '<span style="color: #4ade80;">✓ 正解！</span>';
    } else {
        document.getElementById('result-display').innerHTML =
            '<span style="color: #ef4444;">✗ 不正解</span>';
    }

    document.getElementById('correct-count').textContent = correctAnswers;
    document.getElementById('total-count').textContent = totalQuestions;
    document.getElementById('next-btn').style.display = 'inline-block';
}

function nextQuestion() {
    loadQuestion();
}

// ===== フラッシュカード機能（エキスパートレベル） =====
const flashcards = [
    { front: "メドック格付け第1級の5シャトー", back: "ラフィット、マルゴー、ラトゥール、オー・ブリオン、ムートン・ロートシルト" },
    { front: "DRCのモノポール2つ", back: "ロマネ・コンティ、ラ・ターシュ" },
    { front: "シャブリのグラン・クリュ7つ", back: "ブランショ、レ・クロ、ヴォーデジール、グルヌイユ、ヴァルミュール、レ・プリューズ、ブーグロ" },
    { front: "シャンパーニュのグラン・クリュ村の数", back: "17村" },
    { front: "バローロの最低熟成期間", back: "最低38ヶ月（うち18ヶ月樽熟成）" },
    { front: "バルバレスコの最低熟成期間", back: "最低26ヶ月（うち9ヶ月樽熟成）" },
    { front: "ブルネッロ・ディ・モンタルチーノの最低熟成期間", back: "最低5年（うち2年樽熟成）、リゼルヴァは6年" },
    { front: "キャンティ・クラシコのサンジョヴェーゼ比率", back: "最低80%" },
    { front: "リオハのグラン・レセルバ（赤）の熟成期間", back: "最低60ヶ月（うち24ヶ月樽熟成）" },
    { front: "ポート・ワインのヴィンテージ・ポートの樽熟成", back: "最低2年樽熟成" },
    { front: "ドイツのTBA（トロッケンベーレンアウスレーゼ）の最低糖度", back: "150-154 Öchsle" },
    { front: "オーストリア・ヴァッハウの3つのカテゴリー", back: "Steinfeder（11.5%未満）、Federspiel（11.5-12.5%）、Smaragd（12.5%以上）" },
    { front: "カベルネ・ソーヴィニヨンの親品種", back: "カベルネ・フラン × ソーヴィニヨン・ブラン" },
    { front: "ピノタージュの親品種", back: "ピノ・ノワール × サンソー（エルミタージュ）" },
    { front: "シャトーヌフ・デュ・パプの使用可能品種数", back: "13品種" },
    { front: "アルザスのグラン・クリュの数", back: "51" },
    { front: "ドイツの13のワイン生産地域（主要6つ）", back: "モーゼル、ラインガウ、ファルツ、ラインヘッセン、バーデン、フランケン" },
    { front: "イタリアの格付け（上位3つ）", back: "DOCG、DOC、IGT" },
    { front: "スペインの格付け（上位3つ）", back: "DOCa/DOQ、DO、Vino de la Tierra" },
    { front: "マデイラワインの4つの主要品種（辛口→甘口順）", back: "セルシアル、ヴェルデーリョ、ボアル、マルムジー" },
    { front: "GSMブレンドの品種", back: "グルナッシュ、シラーズ（シラー）、ムールヴェードル" },
    { front: "ボルドーの主要右岸産地", back: "ポムロール、サンテミリオン" },
    { front: "ボルドーの主要左岸産地", back: "メドック（ポイヤック、マルゴー等）、グラーヴ、ペサック・レオニャン" },
    { front: "ブルゴーニュのコート・ドールの2つの地区", back: "コート・ド・ニュイ、コート・ド・ボーヌ" },
    { front: "コート・ロティの2つの斜面", back: "コート・ブロンド、コート・ブリュヌ" },
    { front: "ナパ・ヴァレーの主要サブAVA（5つ）", back: "スタッグス・リープ、ラザフォード、オークヴィル、ホーウェル・マウンテン、カリストガ" },
    { front: "オーストラリアのバロッサで有名な品種", back: "シラーズ（Shiraz）" },
    { front: "ニュージーランド・マールボロで有名な品種", back: "ソーヴィニヨン・ブラン" },
    { front: "アルゼンチンを代表する品種（赤/白）", back: "マルベック（赤）、トロンテス（白）" },
    { front: "チリを代表する固有品種", back: "カルメネール" }
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
    newworld: 0,
    grapes: 0,
    tasting: 0
};

// ローカルストレージから進捗を読み込む
function loadProgress() {
    const saved = localStorage.getItem('wineExpertProgress');
    if (saved) {
        progressData = JSON.parse(saved);
        updateAllProgress();
    }
}

// 進捗を保存
function saveProgress() {
    localStorage.setItem('wineExpertProgress', JSON.stringify(progressData));
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
    const categories = ['france', 'italy', 'spain', 'germany', 'newworld', 'grapes', 'tasting'];
    const maxValues = {
        france: 25,
        italy: 20,
        spain: 15,
        germany: 10,
        newworld: 15,
        grapes: 10,
        tasting: 5
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
            newworld: 0,
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
