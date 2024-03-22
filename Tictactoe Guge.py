def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Проверяем строки
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Проверяем столбцы
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Проверяем диагонали
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Ходит игрок {player}")

        row = int(input("Выберите строку (1-3): ")) - 1
        col = int(input("Выберите столбец (1-3): ")) - 1

        if board[row][col] != " ":
            print("Эта клетка уже занята! Попробуйте снова.")
            continue

        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Игрок {player} победил!")
            break

        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print("Ничья!")
            break

        turn += 1

if __name__ == "__main__":
    tic_tac_toe()
