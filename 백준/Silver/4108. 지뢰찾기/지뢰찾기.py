import sys
input = sys.stdin.read

def solve_minesweeper():
    data = input().split()
    
    if not data:
        return

    results = []
    data_index = 0
    
    DR = [-1, -1, -1, 0, 0, 1, 1, 1]
    DC = [-1, 0, 1, -1, 1, -1, 0, 1]

    while data_index < len(data):
        R = int(data[data_index])
        C = int(data[data_index + 1])
        data_index += 2
        
        if R == 0 and C == 0:
            break

        board = []
        for i in range(R):
            board.append(data[data_index])
            data_index += 1
        
        result_board = [list(row) for row in board]
        
        for r in range(R):
            for c in range(C):
                
                if board[r][c] == '.':
                    mine_count = 0

                    for i in range(8):
                        nr = r + DR[i]
                        nc = c + DC[i]

                        if 0 <= nr < R and 0 <= nc < C:
                            if board[nr][nc] == '*':
                                mine_count += 1
                    
                    result_board[r][c] = str(mine_count)
                
        for row in result_board:
            results.append("".join(row))

    print('\n'.join(results))

solve_minesweeper()