def solve(row, n, board):
    if row == n:
        for c in board:
            print("." * c + "Q" + "." * (n - c - 1))
        print("-" * (n * 2))
        return

    for col in range(n):
        if all(board[i] != col and abs(board[i] - col) != abs(i - row)for i in range(row)):
            board[row] = col
            solve(row + 1, n, board)


n = int(input("Enter N : "))
solve(0, n, [0] * n)