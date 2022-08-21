WORD = 'father'
CORRECT_WORD_ARRAY = list(WORD)

ATTEMPTS = 0

board = [
    ['_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_'],
]

# Function to print the board
def print_board():
    for index in range(6):
        if index == ATTEMPTS:
            print(f'> {board[index]}')
        else:
            print(f'  {board[index]}')

def get_guess():
    guess = input('Guess a word: ')
    return guess

def handle_guess(guess):
    global ATTEMPTS
    if len(guess) != 6:
        print('Invalid guess\n')
        return
    
    guess_array = list(guess)

    for index in range(6):
        if guess_array[index] == CORRECT_WORD_ARRAY[index]:
            board[ATTEMPTS][index] = guess_array[index]
        elif guess_array[index] in CORRECT_WORD_ARRAY:
            print(f"{guess_array[index]} is in the word but wrong position")
    
    if board[ATTEMPTS] == CORRECT_WORD_ARRAY:
        print('You win!')
        return True

    ATTEMPTS = ATTEMPTS + 1

# Main gain starting point
def start_game():
    # displaying initial empty baord
    print_board()
    print()
    # ask the user for a guess as long as they have attempts left
    while ATTEMPTS < 6:
        guess = get_guess()
        won = handle_guess(guess)
        print_board()
        if won:
            break


start_game()