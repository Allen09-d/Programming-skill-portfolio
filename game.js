// Game state variables
let currentRGB;
let lives = 3;
let score = 0;

// DOM elements
const rgbDisplay = document.getElementById('rgbDisplay');
const colorGrid = document.getElementById('colorGrid');
const livesDisplay = document.getElementById('lives');
const scoreDisplay = document.getElementById('score');
const modal = document.getElementById('gameOverModal');
const finalScoreDisplay = document.getElementById('finalScore');
const newGameBtn = document.getElementById('newGameBtn');
const playAgainBtn = document.getElementById('playAgainBtn');

// Generate random RGB color
function generateRandomRGB() {
    return {
        r: Math.floor(Math.random() * 256),
        g: Math.floor(Math.random() * 256),
        b: Math.floor(Math.random() * 256)
    };
}

// Convert RGB object to string
function rgbToString(rgb) {
    return `rgb(${rgb.r}, ${rgb.g}, ${rgb.b})`;
}

// Create color options
function createColorOptions() {
    colorGrid.innerHTML = '';
    currentRGB = generateRandomRGB();
    rgbDisplay.textContent = `RGB(${currentRGB.r}, ${currentRGB.g}, ${currentRGB.b})`;

    const colors = [currentRGB];
    for (let i = 0; i < 5; i++) {
        colors.push(generateRandomRGB());
    }

    // Shuffle colors
    colors.sort(() => Math.random() - 0.5);

    colors.forEach(color => {
        const div = document.createElement('div');
        div.className = 'color-option';
        div.style.backgroundColor = rgbToString(color);
        div.addEventListener('click', () => checkGuess(color));
        colorGrid.appendChild(div);
    });
}

// Check player's guess
function checkGuess(guessedColor) {
    const isCorrect = guessedColor.r === currentRGB.r && 
                    guessedColor.g === currentRGB.g && 
                    guessedColor.b === currentRGB.b;

    if (isCorrect) {
        score += 100;
        scoreDisplay.textContent = score;
        createColorOptions();
    } else {
        lives--;
        livesDisplay.textContent = lives;
        
        if (lives <= 0) {
            gameOver();
        }
    }
}

// Game over handling
function gameOver() {
    modal.style.display = 'flex';
    finalScoreDisplay.textContent = score;
}

// Start new game
function startNewGame() {
    lives = 3;
    score = 0;
    livesDisplay.textContent = lives;
    scoreDisplay.textContent = score;
    modal.style.display = 'none';
    createColorOptions();
}

// Event listeners
newGameBtn.addEventListener('click', startNewGame);
playAgainBtn.addEventListener('click', startNewGame);

// Initialize game
startNewGame();
