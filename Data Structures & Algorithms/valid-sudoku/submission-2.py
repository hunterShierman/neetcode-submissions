class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):

                if board[row][col] == ".":
                    continue 

                box = row // 3 * 3 + col // 3 
                number = board[row][col]

                # not valid if number appears in current row, col, or box
                if number in rows[row] or number in cols[col] or number in boxes[box]:
                    return False

                rows[row].add(number)
                cols[col].add(number)
                boxes[box].add(number)

        return True
        