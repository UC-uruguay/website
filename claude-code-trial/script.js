let currentBalance = 1247;
let currentLanguage = 'en';

// Language switching functionality
function switchLanguage(lang) {
    currentLanguage = lang;
    document.getElementById('html-root').lang = lang;
    
    // Update all elements with data attributes
    const elements = document.querySelectorAll('[data-en][data-ja]');
    elements.forEach(element => {
        element.textContent = element.getAttribute(`data-${lang}`);
    });
    
    // Update active language button
    document.querySelectorAll('.lang-btn').forEach(btn => btn.classList.remove('active'));
    document.getElementById(`lang-${lang}`).classList.add('active');
    
    // Update page title
    document.title = document.querySelector('title').getAttribute(`data-${lang}`);
}

// Balance management and mushroom level calculation
function getMushroomLevel(balance) {
    const digits = balance.toString().length;
    return Math.min(Math.max(digits - 3, 1), 10);
}

function updateMushroomBackground() {
    const level = getMushroomLevel(currentBalance);
    const mushroomLayer = document.getElementById('mushroom-layer');
    
    // Remove all existing mushroom classes
    for (let i = 1; i <= 10; i++) {
        mushroomLayer.classList.remove(`mushroom-level-${i}`);
    }
    
    // Add current level class
    mushroomLayer.classList.add(`mushroom-level-${level}`);
}

function triggerCoinAnimation() {
    const coinElement = document.getElementById('coin-animation');
    coinElement.classList.remove('active');
    
    // Trigger reflow to restart animation
    coinElement.offsetHeight;
    
    coinElement.classList.add('active');
    
    // Remove class after animation completes
    setTimeout(() => {
        coinElement.classList.remove('active');
    }, 1000);
}

function formatCurrency(amount) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
        maximumFractionDigits: 0
    }).format(amount);
}

function increaseBalance() {
    const oldDigits = currentBalance.toString().length;
    
    // Random increase between $100-$999
    const increase = Math.floor(Math.random() * 900) + 100;
    currentBalance += increase;
    
    const newDigits = currentBalance.toString().length;
    
    // Update display
    document.getElementById('balance-amount').textContent = formatCurrency(currentBalance);
    
    // Trigger coin animation if digits increased
    if (newDigits > oldDigits) {
        triggerCoinAnimation();
    }
    
    // Update mushroom background
    updateMushroomBackground();
}

// Automatic balance increase every 30 seconds
function autoIncreaseBalance() {
    const oldDigits = currentBalance.toString().length;
    
    // Smaller automatic increase
    const increase = Math.floor(Math.random() * 50) + 10;
    currentBalance += increase;
    
    const newDigits = currentBalance.toString().length;
    
    // Update display
    document.getElementById('balance-amount').textContent = formatCurrency(currentBalance);
    
    // Trigger coin animation if digits increased
    if (newDigits > oldDigits) {
        triggerCoinAnimation();
    }
    
    // Update mushroom background
    updateMushroomBackground();
}

// Easter egg: Konami code for massive balance boost
let konamiCode = [];
const konamiSequence = [
    'ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown',
    'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight',
    'KeyB', 'KeyA'
];

function handleKonamiCode(event) {
    konamiCode.push(event.code);
    
    if (konamiCode.length > konamiSequence.length) {
        konamiCode.shift();
    }
    
    if (konamiCode.length === konamiSequence.length &&
        konamiCode.every((code, index) => code === konamiSequence[index])) {
        
        // Massive balance boost
        const oldDigits = currentBalance.toString().length;
        currentBalance += 1000000;
        
        document.getElementById('balance-amount').textContent = formatCurrency(currentBalance);
        triggerCoinAnimation();
        updateMushroomBackground();
        
        // Show success message
        alert(currentLanguage === 'en' ? 
            '🎉 Konami Code activated! Massive revenue boost!' : 
            '🎉 コナミコマンド発動！大幅売上アップ！');
        
        konamiCode = [];
    }
}

// Initialize the page
document.addEventListener('DOMContentLoaded', function() {
    // Set initial language to English
    switchLanguage('en');
    
    // Initialize balance display
    document.getElementById('balance-amount').textContent = formatCurrency(currentBalance);
    
    // Initialize mushroom background
    updateMushroomBackground();
    
    // Start automatic balance increases
    setInterval(autoIncreaseBalance, 30000);
    
    // Add Konami code listener
    document.addEventListener('keydown', handleKonamiCode);
    
    // Add some fun interactions
    document.addEventListener('click', function(e) {
        // Create click effect
        const sparkle = document.createElement('div');
        sparkle.innerHTML = '✨';
        sparkle.style.position = 'fixed';
        sparkle.style.left = e.clientX + 'px';
        sparkle.style.top = e.clientY + 'px';
        sparkle.style.fontSize = '1.5rem';
        sparkle.style.pointerEvents = 'none';
        sparkle.style.zIndex = '9999';
        sparkle.style.animation = 'sparkle 1s ease-out forwards';
        
        document.body.appendChild(sparkle);
        
        setTimeout(() => {
            document.body.removeChild(sparkle);
        }, 1000);
    });
});

// Add sparkle animation CSS
const sparkleStyle = document.createElement('style');
sparkleStyle.textContent = `
    @keyframes sparkle {
        0% {
            opacity: 1;
            transform: scale(0) rotate(0deg);
        }
        50% {
            opacity: 1;
            transform: scale(1) rotate(180deg);
        }
        100% {
            opacity: 0;
            transform: scale(0) rotate(360deg);
        }
    }
`;
document.head.appendChild(sparkleStyle);