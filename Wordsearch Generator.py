import random
import string


def place_word(board, word):
    orientations = [0, 1, 2, 3]  # 0=horizontal, 1=vertical, 2=diag TL-BR, 3=diag BL-TR
    tries = 100

    while tries > 0:
        orientation = random.choice(orientations)
        reversed_word = word[::-1] if random.choice([True, False]) else word
        length = len(reversed_word)

        if orientation == 0:  # Horizontal
            row = random.randint(0, len(board) - 1)
            col = random.randint(0, len(board[0]) - length)
            if all(board[row][c] == '-' or board[row][c] == reversed_word[i]
                   for i, c in enumerate(range(col, col + length))):
                for i, c in enumerate(range(col, col + length)):
                    board[row][c] = reversed_word[i]
                return True

        elif orientation == 1:  # Vertical
            row = random.randint(0, len(board) - length)
            col = random.randint(0, len(board[0]) - 1)
            if all(board[r][col] == '-' or board[r][col] == reversed_word[i]
                   for i, r in enumerate(range(row, row + length))):
                for i, r in enumerate(range(row, row + length)):
                    board[r][col] = reversed_word[i]
                return True

        elif orientation == 2:  # Diagonal TL-BR
            row = random.randint(0, len(board) - length)
            col = random.randint(0, len(board[0]) - length)
            if all(board[r][c] == '-' or board[r][c] == reversed_word[i]
                   for i, (r, c) in enumerate(zip(range(row, row + length),
                                                  range(col, col + length)))):
                for i, (r, c) in enumerate(zip(range(row, row + length),
                                               range(col, col + length))):
                    board[r][c] = reversed_word[i]
                return True

        elif orientation == 3:  # Diagonal BL-TR
            row = random.randint(length - 1, len(board) - 1)
            col = random.randint(0, len(board[0]) - length)
            if all(board[r][c] == '-' or board[r][c] == reversed_word[i]
                   for i, (r, c) in enumerate(zip(range(row, row - length, -1),
                                                  range(col, col + length)))):
                for i, (r, c) in enumerate(zip(range(row, row - length, -1),
                                               range(col, col + length))):
                    board[r][c] = reversed_word[i]
                return True

        tries -= 1

    print(f"Could not place word: {word}")
    return False

def fill_empty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == '-':
                board[row][col] = random.choice(string.ascii_uppercase)

def create_word_search(words, size=13):
    board = [['-' for _ in range(size)] for _ in range(size)]
    for word in words:
        place_word(board, word.upper())
    fill_empty(board)
    return board

def display_board(board):
    for row in board:
        print(' '.join(row))


while True:
    words = input("Enter any 5 or less of your words separated by commas (don't use any spaces): ").split(',')

    valid = True
    for word in words:
        if not (isinstance(word, str) and word.strip() and word.strip().isalpha()):
            print("Please enter valid words (letters only, no numbers or special characters).")
            valid = False
            break

    if not valid:
        continue

    board = create_word_search(words)
    display_board(board)
    print("\nWords to Find:")
    print(", ".join(words))
    if input("Do you want to start again? Click s to start again or (Press Enter to exit...)") != 's':
        break

