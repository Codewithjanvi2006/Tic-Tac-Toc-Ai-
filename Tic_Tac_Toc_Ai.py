import math

# Define players
HUMAN = 'X'
AI = 'O'
EMPTY = ' '

# Initialize board
board = [EMPTY] * 9

def print_board():
    for i in range(0,9,3):
        print('|'.join(board[i:i+3]))

def available_moves():
    return [i for i, spot in enumerate(board) if spot == EMPTY]

def winner(player):
    win_indices = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for a, b, c in win_indices:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def minimax(depth, is_maximizing):
    if winner(AI):
        return 1
    if winner(HUMAN):
        return -1
    if not available_moves():
        return 0
    
    if is_maximizing:
        max_eval = -math.inf
        for move in available_moves():
            board[move] = AI
            eval = minimax(depth + 1, False)
            board[move] = EMPTY
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for move in available_moves():
            board[move] = HUMAN
            eval = minimax(depth + 1, True)
            board[move] = EMPTY
            min_eval = min(min_eval, eval)
        return min_eval

def best_move():
    best_val = -math.inf
    move = -1
    for i in available_moves():
        board[i] = AI
        move_val = minimax(0, False)
        board[i] = EMPTY
        if move_val > best_val:
            best_val = move_val
            move = i
    return move

def play():
    print("Let's play Tic-Tac-Toe! You are X.")
    print_board()
    while True:
        human_move = int(input("Enter your move (0-8): "))
        if human_move not in available_moves():
            print("Invalid move.")
            continue
        board[human_move] = HUMAN
        if winner(HUMAN):
            print_board()
            print("Congratulations! You win.")
            break
        if not available_moves():
            print_board()
            print("Tie.")
            break
        
        ai_move = best_move()
        board[ai_move] = AI
        if winner(AI):
            print_board()
            print("AI wins.")
            break
        if not available_moves():
            print_board()
            print("Tie.")
            break
        print_board()

if __name__ == "__main__":
    play()
