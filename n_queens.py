n = 4
board = [-1] * n
row = 0
col = 0
count = 0

while row >= 0:
    placed = False
    while col < n:
        conflict = False
        for prev_row in range(row):
            prev_col = board[prev_row]
            if prev_col == col or abs(prev_row - row) == abs(prev_col - col):
                conflict = True
                break
        if not conflict:
            board[row] = col
            placed = True
            col = 0
            break
        col += 1
    
    if placed:
        row += 1
        if row == n:
            count += 1
            row -= 1
            col = board[row] + 1
    else:
        row -= 1
        if row >= 0:
            col = board[row] + 1

print(count)
