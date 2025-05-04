import random

class GameState:
    def __init__(self):
        """Initialize the game state"""
        self.board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.score = 0
        self.game_over = False
        self.initialize_board()
    
    def initialize_board(self):
        """Initialize the game board with two random tiles"""
        self.board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.score = 0
        self.game_over = False
        self.add_random_tile()
        self.add_random_tile()
    
    def get_state(self):
        """Return the current game state"""
        return {
            "board": self.board,
            "score": self.score,
            "game_over": self.game_over
        }
    
    def add_random_tile(self):
        """Add a random tile (2 or 4) to an empty cell"""
        empty_cells = []
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    empty_cells.append((i, j))
        
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.board[i][j] = 2 if random.random() < 0.9 else 4
            return True
        return False
    
    def move_left(self):
        """Move all tiles to the left and merge if possible"""
        moved = False
        for row in range(4):
            # Compact non-zero elements to the left
            new_row = [val for val in self.board[row] if val != 0]
            
            # Merge adjacent equal tiles
            i = 0
            while i < len(new_row) - 1:
                if new_row[i] == new_row[i + 1]:
                    new_row[i] *= 2
                    self.score += new_row[i]
                    new_row.pop(i + 1)
                    new_row.append(0)
                i += 1
            
            # Fill with zeros
            while len(new_row) < 4:
                new_row.append(0)
            
            # Check if the board changed
            if new_row != self.board[row]:
                moved = True
            
            self.board[row] = new_row
        
        return moved

    def move_right(self):
        """Move all tiles to the right and merge if possible"""
        # Reverse each row, move left, then reverse again
        for row in range(4):
            self.board[row].reverse()
        moved = self.move_left()
        for row in range(4):
            self.board[row].reverse()
        return moved

    def move_up(self):
        """Move all tiles up and merge if possible"""
        # Transpose, move left, then transpose back
        self.transpose()
        moved = self.move_left()
        self.transpose()
        return moved

    def move_down(self):
        """Move all tiles down and merge if possible"""
        # Transpose, move right, then transpose back
        self.transpose()
        moved = self.move_right()
        self.transpose()
        return moved

    def transpose(self):
        """Transpose the board"""
        for i in range(4):
            for j in range(i + 1, 4):
                self.board[i][j], self.board[j][i] = self.board[j][i], self.board[i][j]

    def check_game_over(self):
        """Check if the game is over by seeing if any moves are possible"""
        # Check for empty cells
        for row in range(4):
            for col in range(4):
                if self.board[row][col] == 0:
                    return False

        # Check for possible merges horizontally
        for row in range(4):
            for col in range(3):
                if self.board[row][col] == self.board[row][col + 1]:
                    return False

        # Check for possible merges vertically
        for row in range(3):
            for col in range(4):
                if self.board[row][col] == self.board[row + 1][col]:
                    return False

        return True
    
    def handle_move(self, direction):
        """Handle a move in the specified direction"""
        if self.game_over:
            return False
        
        moved = False
        
        if direction == 'left':
            moved = self.move_left()
        elif direction == 'right':
            moved = self.move_right()
        elif direction == 'up':
            moved = self.move_up()
        elif direction == 'down':
            moved = self.move_down()
        
        if moved:
            self.add_random_tile()
            self.game_over = self.check_game_over()
        
        return moved