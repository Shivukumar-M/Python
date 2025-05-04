from flask import Flask, render_template, jsonify, request
from game_logic import GameState

app = Flask(__name__)

# Create a game state instance
game = GameState()

@app.route('/')
def index():
    """Render the main game page"""
    return render_template('index.html')

@app.route('/new_game', methods=['POST'])
def new_game():
    """Start a new game"""
    game.initialize_board()
    return jsonify(game.get_state())

@app.route('/move', methods=['POST'])
def move():
    """Process a move"""
    if game.game_over:
        return jsonify(game.get_state())
    
    direction = request.json.get('direction', None)
    game.handle_move(direction)
    
    return jsonify(game.get_state())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Set host to '0.0.0.0' to allow external access