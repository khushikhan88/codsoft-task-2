import random

board = [" " for _ in range(9)]

wins = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

def show():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")

def check(player):
    return any(board[a] == board[b] == board[c] == player for a, b, c in wins)

print("Positions:")
print("1 2 3\n4 5 6\n7 8 9")

while True:
    show()

    try:
        pos = int(input("Your move (1-9): ")) - 1

        if pos < 0 or pos > 8 or board[pos] != " ":
            print("Invalid move.")
            continue

        board[pos] = "X"

        if check("X"):
            show()
            print("🎉 You win!")
            break

        free = [i for i in range(9) if board[i] == " "]

        if not free:
            show()
            print("🤝 Draw!")
            break

        ai = random.choice(free)
        board[ai] = "O"

        if check("O"):
            show()
            print("🤖 Computer wins!")
            break

    except ValueError:
        print("Enter a valid number.")