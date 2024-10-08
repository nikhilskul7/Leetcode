class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols=defaultdict(set)
        rows=defaultdict(set)
        
        squares=defaultdict(set)
        
        for i in range(9):
            
            for j in range(9):
                
                if board[i][j]==".":
                    continue
                r=i//3
                c=j//3
                
                if (board[i][j] in rows[i]) or (board[i][j] in cols[j]) or (board[i][j] in squares[r,c]):
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[r,c].add(board[i][j])
                
        return True