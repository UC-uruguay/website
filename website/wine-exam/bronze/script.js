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

// ===== クイズ履歴管理 =====
function saveQuizResult(questionIndex, isCorrect) {
    const question = quizQuestions[questionIndex];
    const history = getQuizHistory();
    history.push({
        questionIndex: questionIndex,
        category: question.category,
        isCorrect: isCorrect,
        timestamp: Date.now()
    });
    localStorage.setItem('wineBronzeQuizHistory', JSON.stringify(history));
    updateProgressFromQuizHistory();
}

function getQuizHistory() {
    const saved = localStorage.getItem('wineBronzeQuizHistory');
    return saved ? JSON.parse(saved) : [];
}

function calculateCategoryStats() {
    const history = getQuizHistory();
    const stats = {};
    const categories = ['white', 'red', 'basics', 'tasting', 'bottle', 'history', 'pairing'];

    categories.forEach(cat => {
        stats[cat] = { correct: 0, total: 0, percentage: 0 };
    });

    history.forEach(entry => {
        const cat = entry.category;
        if (stats[cat]) {
            stats[cat].total++;
            if (entry.isCorrect) {
                stats[cat].correct++;
            }
        }
    });

    Object.keys(stats).forEach(cat => {
        if (stats[cat].total > 0) {
            stats[cat].percentage = (stats[cat].correct / stats[cat].total) * 100;
        }
    });

    return stats;
}

function updateProgressFromQuizHistory() {
    const stats = calculateCategoryStats();
    const maxValues = {
        white: 30,
        red: 30,
        basics: 15,
        tasting: 5,
        bottle: 5,
        history: 5,
        pairing: 10
    };

    // カテゴリー別の進捗を更新
    Object.keys(stats).forEach(category => {
        const percentage = stats[category].percentage;
        const maxValue = maxValues[category];
        if (maxValue) {
            progressData[category] = Math.round((percentage / 100) * maxValue);
        }

        // 統計表示を更新
        const statsElement = document.getElementById(`stats-${category}`);
        if (statsElement) {
            if (stats[category].total > 0) {
                statsElement.textContent = `(${stats[category].correct}/${stats[category].total})`;
            } else {
                statsElement.textContent = '(未挑戦)';
            }
        }
    });

    saveProgress();
    updateAllProgress();
}

// ===== クイズ機能 =====
const quizQuestions = [
    // 白ブドウ品種 (14問)
    {
        question: "シャルドネの主要産地として正しいものはどれですか？",
        options: [
            "フランス、アメリカ、オーストラリア",
            "ドイツ、オーストリア、イタリア",
            "スペイン、ポルトガル、南アフリカ",
            "アルゼンチン、チリ、ニュージーランド"
        ],
        correct: 0,
        category: "white"
    },
    {
        question: "ソーヴィニヨン・ブランの特徴的な香りはどれですか？",
        options: [
            "バラ、ライチ",
            "グレープフルーツ、ハーブ",
            "蜂蜜、アプリコット",
            "バター、バニラ"
        ],
        correct: 1,
        category: "white"
    },
    {
        question: "リースリングの主要産地はどこですか？",
        options: [
            "イタリア",
            "スペイン",
            "ドイツ",
            "ポルトガル"
        ],
        correct: 2,
        category: "white"
    },
    {
        question: "ゲヴュルツトラミネールの香りの特徴として正しいものはどれですか？",
        options: [
            "柑橘類、ミネラル",
            "ライチ、バラ、スパイス",
            "青リンゴ、洋梨",
            "レモン、グレープフルーツ"
        ],
        correct: 1,
        category: "white"
    },
    {
        question: "ピノ・グリの別名（イタリア名）は何ですか？",
        options: [
            "ピノ・ビアンコ",
            "ピノ・グリージョ",
            "トレッビアーノ",
            "ヴェルディッキオ"
        ],
        correct: 1,
        category: "white"
    },
    {
        question: "セミヨンが貴腐ワインの原料となる主要産地はどこですか？",
        options: [
            "ブルゴーニュ",
            "ボルドー（ソーテルヌ）",
            "ローヌ",
            "ロワール"
        ],
        correct: 1,
        category: "white"
    },
    {
        question: "ミュスカデの主要産地はどこですか？",
        options: [
            "ブルゴーニュ",
            "ボルドー",
            "ロワール",
            "ローヌ"
        ],
        correct: 2,
        category: "white"
    },
    {
        question: "ヴィオニエの特徴的な香りはどれですか？",
        options: [
            "アプリコット、白桃、花",
            "グレープフルーツ、ハーブ",
            "リンゴ、洋梨",
            "レモン、ライム"
        ],
        correct: 0,
        category: "white"
    },
    {
        question: "シュナン・ブランの主要産地はどこですか？",
        options: [
            "ボルドー",
            "ブルゴーニュ",
            "ロワール",
            "アルザス"
        ],
        correct: 2,
        category: "white"
    },
    {
        question: "アルバリーニョの主要産地はどこですか？",
        options: [
            "イタリア",
            "フランス",
            "スペイン（リアス・バイシャス）",
            "ドイツ"
        ],
        correct: 2,
        category: "white"
    },
    {
        question: "トレッビアーノの別名（フランス名）は何ですか？",
        options: [
            "ユニ・ブラン",
            "ピノ・ブラン",
            "シャルドネ",
            "ソーヴィニヨン・ブラン"
        ],
        correct: 0,
        category: "white"
    },
    {
        question: "甲州の主要産地はどこですか？",
        options: [
            "長野県",
            "山梨県",
            "北海道",
            "山形県"
        ],
        correct: 1,
        category: "white"
    },
    {
        question: "リースリング・イタリコはリースリングと同じ品種ですか？",
        options: [
            "同じ品種である",
            "別品種である",
            "リースリングの亜種である",
            "リースリングの交配種である"
        ],
        correct: 1,
        category: "white"
    },
    {
        question: "ミュラー・トゥルガウの主要産地はどこですか？",
        options: [
            "フランス",
            "イタリア",
            "ドイツ",
            "スペイン"
        ],
        correct: 2,
        category: "white"
    },
    // 黒ブドウ品種 (14問)
    {
        question: "カベルネ・ソーヴィニヨンの特徴的な香りはどれですか？",
        options: [
            "イチゴ、ラズベリー",
            "カシス、杉、タンニン豊富",
            "チェリー、プラム",
            "バラ、タール"
        ],
        correct: 1,
        category: "red"
    },
    {
        question: "メルローの主要産地として有名なボルドーの地区はどこですか？",
        options: [
            "メドック",
            "ポムロール",
            "ソーテルヌ",
            "グラーヴ"
        ],
        correct: 1,
        category: "red"
    },
    {
        question: "ピノ・ノワールの主要産地として最も有名なのはどこですか？",
        options: [
            "ボルドー",
            "ブルゴーニュ",
            "ローヌ",
            "ロワール"
        ],
        correct: 1,
        category: "red"
    },
    {
        question: "シラーの別名（オーストラリアでの呼び名）は何ですか？",
        options: [
            "シラーズ",
            "グルナッシュ",
            "マルベック",
            "カリニャン"
        ],
        correct: 0,
        category: "red"
    },
    {
        question: "グルナッシュの特徴として正しいものはどれですか？",
        options: [
            "低いアルコール度数、軽いボディ",
            "高いアルコール度数、果実味豊か",
            "強いタンニン、長期熟成向き",
            "高い酸味、軽やかな味わい"
        ],
        correct: 1,
        category: "red"
    },
    {
        question: "テンプラニーリョの主要産地はどこですか？",
        options: [
            "イタリア",
            "フランス",
            "スペイン",
            "ポルトガル"
        ],
        correct: 2,
        category: "red"
    },
    {
        question: "サンジョヴェーゼの主要産地はどこですか？",
        options: [
            "ピエモンテ",
            "トスカーナ",
            "ヴェネト",
            "シチリア"
        ],
        correct: 1,
        category: "red"
    },
    {
        question: "ネッビオーロから造られる有名なワインはどれですか？",
        options: [
            "キャンティ",
            "バローロ",
            "ヴァルポリチェッラ",
            "ソアーヴェ"
        ],
        correct: 1,
        category: "red"
    },
    {
        question: "カベルネ・フランの特徴的な香りはどれですか？",
        options: [
            "カシス、杉",
            "ラズベリー、ピーマン、ハーブ",
            "ブラックペッパー、スパイス",
            "チェリー、プラム"
        ],
        correct: 1,
        category: "red"
    },
    {
        question: "マルベックの主要産地として有名なのはどこですか？",
        options: [
            "チリ",
            "アルゼンチン",
            "オーストラリア",
            "南アフリカ"
        ],
        correct: 1,
        category: "red"
    },
    {
        question: "ピノタージュの主要産地はどこですか？",
        options: [
            "オーストラリア",
            "ニュージーランド",
            "南アフリカ",
            "チリ"
        ],
        correct: 2,
        category: "red"
    },
    {
        question: "ジンファンデルの主要産地はどこですか？",
        options: [
            "フランス",
            "イタリア",
            "アメリカ（カリフォルニア）",
            "オーストラリア"
        ],
        correct: 2,
        category: "red"
    },
    {
        question: "マスカット・ベーリーAは何の品種ですか？",
        options: [
            "白ブドウ品種",
            "黒ブドウ品種（日本固有）",
            "ロゼ専用品種",
            "スパークリング専用品種"
        ],
        correct: 1,
        category: "red"
    },
    {
        question: "ガメイから造られる有名なワインはどれですか？",
        options: [
            "ボジョレー・ヌーヴォー",
            "シャブリ",
            "サンセール",
            "ミュスカデ"
        ],
        correct: 0,
        category: "red"
    },
    // ワインの分類・製法 (8問)
    {
        question: "赤ワインと白ワインの製造における最大の違いは何ですか？",
        options: [
            "使用するブドウの種類",
            "発酵温度",
            "果皮と共に発酵するかどうか",
            "熟成期間"
        ],
        correct: 2,
        category: "basics"
    },
    {
        question: "マロラクティック発酵の効果は何ですか？",
        options: [
            "アルコール度数を高める",
            "酸味をまろやかにする",
            "色を濃くする",
            "タンニンを増やす"
        ],
        correct: 1,
        category: "basics"
    },
    {
        question: "シャンパーニュの製造方法は何と呼ばれますか？",
        options: [
            "シャルマ方式",
            "瓶内二次発酵",
            "炭酸ガス注入法",
            "メトード・アンセストラル"
        ],
        correct: 1,
        category: "basics"
    },
    {
        question: "プロセッコの製造方法は何と呼ばれますか？",
        options: [
            "瓶内二次発酵",
            "シャルマ方式（タンク内二次発酵）",
            "炭酸ガス注入法",
            "メトード・シャンプノワーズ"
        ],
        correct: 1,
        category: "basics"
    },
    {
        question: "酒精強化ワインの例として正しいものはどれですか？",
        options: [
            "シャンパーニュ",
            "プロセッコ",
            "ポート",
            "ボジョレー"
        ],
        correct: 2,
        category: "basics"
    },
    {
        question: "白ワインの製造工程で、圧搾はいつ行いますか？",
        options: [
            "破砕の前",
            "破砕の後、発酵の前",
            "発酵の後",
            "熟成の後"
        ],
        correct: 1,
        category: "basics"
    },
    {
        question: "ロゼワインの製造方法として正しくないものはどれですか？",
        options: [
            "赤ワインと白ワインを混ぜる（シャンパーニュを除く）",
            "短時間果皮と接触させる",
            "直接圧搾法",
            "セニエ法"
        ],
        correct: 0,
        category: "basics"
    },
    {
        question: "スパークリングワインの分類で正しくないものはどれですか？",
        options: [
            "シャンパーニュ方式",
            "シャルマ方式",
            "マロラクティック方式",
            "炭酸ガス注入法"
        ],
        correct: 2,
        category: "basics"
    },
    // 保存・テイスティング (3問)
    {
        question: "ワインの保存に適した温度は何度ですか？",
        options: [
            "5-8℃",
            "12-15℃",
            "18-22℃",
            "25-28℃"
        ],
        correct: 1,
        category: "tasting"
    },
    {
        question: "テイスティングの正しい順序はどれですか？",
        options: [
            "香り → 外観 → 味わい",
            "外観 → 味わい → 香り",
            "外観 → 香り → 味わい",
            "味わい → 香り → 外観"
        ],
        correct: 2,
        category: "tasting"
    },
    {
        question: "スパークリングワインの適正温度は何度ですか？",
        options: [
            "16-18℃",
            "12-14℃",
            "8-12℃",
            "6-8℃"
        ],
        correct: 3,
        category: "tasting"
    },
    // ボトル・ラベル (3問)
    {
        question: "ボルドー型ボトルの特徴は何ですか？",
        options: [
            "なで肩",
            "いかり肩",
            "細長いフルート型",
            "厚いガラスのシャンパーニュ型"
        ],
        correct: 1,
        category: "bottle"
    },
    {
        question: "ワインボトルの標準容量は何mlですか？",
        options: [
            "500ml",
            "750ml",
            "1000ml",
            "1500ml"
        ],
        correct: 1,
        category: "bottle"
    },
    {
        question: "マグナムボトルの容量は何mlですか？",
        options: [
            "750ml",
            "1000ml",
            "1500ml",
            "2000ml"
        ],
        correct: 2,
        category: "bottle"
    },
    // ワイン史 (3問)
    {
        question: "ワインの起源とされる地域はどこですか？",
        options: [
            "イタリア",
            "フランス",
            "ジョージア（コーカサス地方）",
            "ギリシャ"
        ],
        correct: 2,
        category: "history"
    },
    {
        question: "19世紀にヨーロッパのブドウ畑を壊滅させた害虫は何ですか？",
        options: [
            "アブラムシ",
            "フィロキセラ",
            "カメムシ",
            "ハダニ"
        ],
        correct: 1,
        category: "history"
    },
    {
        question: "中世にワイン造りを継承・発展させたのは誰ですか？",
        options: [
            "貴族",
            "商人",
            "修道院（修道士）",
            "農民"
        ],
        correct: 2,
        category: "history"
    },
    // 食事との組み合わせ (5問)
    {
        question: "フードペアリングの基本原則として正しくないものはどれですか？",
        options: [
            "軽い料理には軽いワイン",
            "白身魚には赤ワイン",
            "赤身肉には赤ワイン",
            "地域の料理には同じ地域のワイン"
        ],
        correct: 1,
        category: "pairing"
    },
    {
        question: "牡蠣に合うワインとして最も適切なのはどれですか？",
        options: [
            "フルボディの赤ワイン",
            "軽口の白ワイン",
            "甘口の白ワイン",
            "酒精強化ワイン"
        ],
        correct: 1,
        category: "pairing"
    },
    {
        question: "ビーフステーキに合うワインとして最も適切なのはどれですか？",
        options: [
            "軽口の白ワイン",
            "スパークリングワイン",
            "フルボディの赤ワイン",
            "ロゼワイン"
        ],
        correct: 2,
        category: "pairing"
    },
    {
        question: "スパークリングワインと相性が良い料理はどれですか？",
        options: [
            "揚げ物、天ぷら",
            "ビーフシチュー",
            "ジビエ",
            "濃厚なソースの肉料理"
        ],
        correct: 0,
        category: "pairing"
    },
    {
        question: "フォアグラに合うワインとして最も適切なのはどれですか？",
        options: [
            "辛口の白ワイン",
            "甘口の白ワイン（貴腐ワイン）",
            "軽口の赤ワイン",
            "フルボディの赤ワイン"
        ],
        correct: 1,
        category: "pairing"
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
        const percentage = Math.round((correctAnswers/totalQuestions)*100);
        const passStatus = percentage >= 70 ? '合格！' : '不合格';
        document.getElementById('question-display').innerHTML =
            `<p class="question-text">すべての問題が終了しました！<br>正解数: ${correctAnswers} / ${totalQuestions}<br>正答率: ${percentage}%<br>${passStatus}</p>`;
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

    const isCorrect = selectedIndex === question.correct;

    buttons.forEach((btn, index) => {
        btn.disabled = true;
        if (index === question.correct) {
            btn.classList.add('correct');
        } else if (index === selectedIndex) {
            btn.classList.add('incorrect');
        }
    });

    if (isCorrect) {
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

    // クイズ結果を保存
    saveQuizResult(questionIndex, isCorrect);
}

function nextQuestion() {
    loadQuestion();
}

// ===== フラッシュカード機能 =====
const flashcards = [
    // 白ブドウ品種 (14種)
    { front: "シャルドネ (Chardonnay)", back: "柑橘類、バター、バニラ。主要産地: フランス（ブルゴーニュ、シャンパーニュ）、アメリカ、オーストラリア" },
    { front: "ソーヴィニヨン・ブラン (Sauvignon Blanc)", back: "グレープフルーツ、ハーブ、青草。主要産地: フランス（ロワール、ボルドー）、ニュージーランド" },
    { front: "リースリング (Riesling)", back: "リンゴ、蜂蜜、ペトロール。高い酸味。主要産地: ドイツ、フランス（アルザス）" },
    { front: "ゲヴュルツトラミネール (Gewürztraminer)", back: "ライチ、バラ、スパイス。非常にアロマティック。主要産地: フランス（アルザス）" },
    { front: "ピノ・グリ (Pinot Gris)", back: "洋梨、アーモンド、軽やかな酸味。主要産地: イタリア、フランス（アルザス）" },
    { front: "セミヨン (Sémillon)", back: "蜂蜜、レモン、無花果。貴腐ワインにも使用。主要産地: フランス（ボルドー）" },
    { front: "ミュスカデ (Muscadet)", back: "レモン、ミネラル、軽やか。シュール・リー製法。主要産地: フランス（ロワール）" },
    { front: "ヴィオニエ (Viognier)", back: "アプリコット、白桃、花の香り。フルボディ。主要産地: フランス（ローヌ）" },
    { front: "シュナン・ブラン (Chenin Blanc)", back: "リンゴ、蜂蜜、高い酸味。多様なスタイル。主要産地: フランス（ロワール）" },
    { front: "アルバリーニョ (Albariño)", back: "柑橘類、白桃、ミネラル感。主要産地: スペイン（リアス・バイシャス）" },
    { front: "トレッビアーノ (Trebbiano)", back: "レモン、軽やか、ニュートラル。主要産地: イタリア、フランス（コニャック地方）" },
    { front: "甲州 (Koshu)", back: "柑橘類、白桃、繊細。和食との相性良い。主要産地: 日本（山梨県）" },
    { front: "リースリング・イタリコ (Riesling Italico)", back: "リンゴ、柑橘類、軽やか。リースリングとは別品種。主要産地: イタリア、オーストリア" },
    { front: "ミュラー・トゥルガウ (Müller-Thurgau)", back: "マスカット、花の香り、軽やかでフルーティ。主要産地: ドイツ、オーストリア" },
    // 黒ブドウ品種 (14種)
    { front: "カベルネ・ソーヴィニヨン (Cabernet Sauvignon)", back: "カシス、杉、タンニン豊富。長期熟成向き。主要産地: フランス（ボルドー）" },
    { front: "メルロー (Merlot)", back: "プラム、ブラックチェリー、まろやかなタンニン。主要産地: フランス（ボルドー、ポムロール）" },
    { front: "ピノ・ノワール (Pinot Noir)", back: "ラズベリー、イチゴ、エレガント。軽〜中程度のボディ。主要産地: フランス（ブルゴーニュ）" },
    { front: "シラー / シラーズ (Syrah / Shiraz)", back: "ブラックペッパー、スパイス、スミレ。力強い。主要産地: フランス（ローヌ）、オーストラリア" },
    { front: "グルナッシュ (Grenache)", back: "レッドベリー、スパイス、高いアルコール度数。主要産地: フランス（ローヌ南部）、スペイン" },
    { front: "テンプラニーリョ (Tempranillo)", back: "イチゴ、プラム、革、バニラ。主要産地: スペイン（リオハ、リベラ・デル・ドゥエロ）" },
    { front: "サンジョヴェーゼ (Sangiovese)", back: "チェリー、プラム、高い酸味。主要産地: イタリア（トスカーナ）" },
    { front: "ネッビオーロ (Nebbiolo)", back: "バラ、タール、強いタンニン。長期熟成向き。主要産地: イタリア（ピエモンテ）" },
    { front: "カベルネ・フラン (Cabernet Franc)", back: "ラズベリー、ピーマン、ハーブ。主要産地: フランス（ロワール、ボルドー）" },
    { front: "マルベック (Malbec)", back: "ブラックベリー、プラム、濃い色調。主要産地: アルゼンチン" },
    { front: "ピノタージュ (Pinotage)", back: "プラム、スモーク、土っぽさ。南アフリカ固有品種" },
    { front: "ジンファンデル (Zinfandel)", back: "ジャム、スパイス、高いアルコール度数。主要産地: アメリカ（カリフォルニア）" },
    { front: "マスカット・ベーリーA (Muscat Bailey A)", back: "イチゴ、キャンディ、軽やかなタンニン。日本固有品種" },
    { front: "ガメイ (Gamay)", back: "イチゴ、バナナ、軽やかで果実味豊か。ボジョレー・ヌーヴォー。主要産地: フランス（ボジョレー）" }
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
    white: 0,
    red: 0,
    basics: 0,
    tasting: 0,
    bottle: 0,
    history: 0,
    pairing: 0
};

// ローカルストレージから進捗を読み込む
function loadProgress() {
    const saved = localStorage.getItem('wineBronzeProgress');
    if (saved) {
        progressData = JSON.parse(saved);
        updateAllProgress();
    }
}

// 進捗を保存
function saveProgress() {
    localStorage.setItem('wineBronzeProgress', JSON.stringify(progressData));
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
    const categories = ['white', 'red', 'basics', 'tasting', 'bottle', 'history', 'pairing'];
    const maxValues = {
        white: 30,
        red: 30,
        basics: 15,
        tasting: 5,
        bottle: 5,
        history: 5,
        pairing: 10
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
    if (confirm('進捗とクイズ履歴をすべてリセットしてもよろしいですか？')) {
        progressData = {
            white: 0,
            red: 0,
            basics: 0,
            tasting: 0,
            bottle: 0,
            history: 0,
            pairing: 0
        };
        saveProgress();

        // クイズ履歴をリセット
        localStorage.removeItem('wineBronzeQuizHistory');

        updateAllProgress();

        // 統計表示をリセット
        const categories = ['white', 'red', 'basics', 'tasting', 'bottle', 'history', 'pairing'];
        categories.forEach(category => {
            const statsElement = document.getElementById(`stats-${category}`);
            if (statsElement) {
                statsElement.textContent = '(未挑戦)';
            }
        });

        alert('進捗とクイズ履歴をリセットしました');
    }
}

// ページ読み込み時に進捗を復元
window.addEventListener('DOMContentLoaded', () => {
    loadProgress();
    updateProgressFromQuizHistory();
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

// ナビバー自動非表示機能
let lastScrollTop = 0;
let scrollThreshold = 10;

window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    const currentScroll = window.pageYOffset || document.documentElement.scrollTop;

    // スクロール量が閾値より小さい場合は何もしない
    if (Math.abs(currentScroll - lastScrollTop) < scrollThreshold) {
        return;
    }

    // 下にスクロールしている場合は非表示
    if (currentScroll > lastScrollTop && currentScroll > 80) {
        navbar.classList.add('hidden');
    } else {
        // 上にスクロールしている場合は表示
        navbar.classList.remove('hidden');
    }

    lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
});
