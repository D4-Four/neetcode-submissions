class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check vertical & horizontal
        for i in range(9):
            vertical = set()
            horizontal = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in vertical:
                        return False
                    else:
                        vertical.add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in horizontal:
                        return False
                    else:
                        horizontal.add(board[j][i])
        # 9 3x3 sudoku check
        for square in range(9):
            hashmap = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3)*3+i
                    col = (square%3)*3 +j
                    if board[row][col] != '.':
                        if board[row][col] in hashmap:
                            return False
                        else:
                            hashmap.add(board[row][col])
        return True