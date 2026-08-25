def solve(board):
    row = [set() for _ in range(9)]
    col = [set() for _ in range(9)]
    boxes = {}

    for i in range(9):
        for j in range(9):

            val = board[i][j]

            if val == '.':
                continue

            if val in row[i]:
                return False

            row[i].add(val)

            if val in col[j]:
                return False

            col[j].add(val)

            # 3x3 Box
            box = (i // 3, j // 3)

            if box not in boxes:
                boxes[box] = set()

            if val in boxes[box]:
                return False

            boxes[box].add(val)

    return True


board = []

for _ in range(9):
    row = input().split()
    board.append(row)

print(solve(board))
