document.addEventListener('DOMContentLoaded', function() {
    const tileContainer = document.getElementById('tile-container');
    const scoreElement = document.getElementById('score');
    const newGameButton = document.getElementById('new-game');
    const gameOverElement = document.getElementById('game-over');

    // Start a new game when the page loads
    startNewGame();

    // Add event listener for the New Game button
    newGameButton.addEventListener('click', startNewGame);

    // Add keyboard event listeners
    document.addEventListener('keydown', handleKeyPress);
    
    // Add touch support for mobile devices
    let touchStartX, touchStartY, touchEndX, touchEndY;
    const gameContainer = document.querySelector('.game-container');
    
    gameContainer.addEventListener('touchstart', function(e) {
        touchStartX = e.touches[0].clientX;
        touchStartY = e.touches[0].clientY;
        e.preventDefault();
    }, { passive: false });
    
    gameContainer.addEventListener('touchend', function(e) {
        touchEndX = e.changedTouches[0].clientX;
        touchEndY = e.changedTouches[0].clientY;
        handleSwipe();
        e.preventDefault();
    }, { passive: false });
    
    function handleSwipe() {
        const xDiff = touchStartX - touchEndX;
        const yDiff = touchStartY - touchEndY;
        
        // Determine if the swipe was horizontal or vertical
        if (Math.abs(xDiff) > Math.abs(yDiff)) {
            if (xDiff > 0) {
                // Left swipe
                makeMove('left');
            } else {
                // Right swipe
                makeMove('right');
            }
        } else {
            if (yDiff > 0) {
                // Up swipe
                makeMove('up');
            } else {
                // Down swipe
                makeMove('down');
            }
        }
    }
    
    // Function to start a new game
    function startNewGame() {
        fetch('/new_game', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then(response => response.json())
        .then(data => {
            updateBoard(data);
            gameOverElement.classList.remove('show');
        })
        .catch(error => {
            console.error('Error starting new game:', error);
        });
    }

    // Function to handle key presses
    function handleKeyPress(event) {
        let direction = null;
        
        switch(event.key) {
            case 'ArrowLeft':
                direction = 'left';
                event.preventDefault();
                break;
            case 'ArrowRight':
                direction = 'right';
                event.preventDefault();
                break;
            case 'ArrowUp':
                direction = 'up';
                event.preventDefault();
                break;
            case 'ArrowDown':
                direction = 'down';
                event.preventDefault();
                break;
            default:
                return;
        }
        
        makeMove(direction);
    }
    
    // Function to make a move
    function makeMove(direction) {
        fetch('/move', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ direction })
        })
        .then(response => response.json())
        .then(data => {
            updateBoard(data);
            if (data.game_over) {
                gameOverElement.classList.add('show');
            }
        })
        .catch(error => {
            console.error('Error making move:', error);
        });
    }

    // Function to update the game board
    function updateBoard(gameState) {
        // Update score
        scoreElement.textContent = gameState.score;
        
        // Clear the tile container
        tileContainer.innerHTML = '';
        
        // Create and update tiles
        for (let row = 0; row < 4; row++) {
            for (let col = 0; col < 4; col++) {
                const value = gameState.board[row][col];
                if (value > 0) {
                    const tile = document.createElement('div');
                    tile.className = `tile tile-${value}`;
                    tile.style.gridRow = row + 1;
                    tile.style.gridColumn = col + 1;
                    tile.textContent = value;
                    tileContainer.appendChild(tile);
                }
            }
        }
    }
});