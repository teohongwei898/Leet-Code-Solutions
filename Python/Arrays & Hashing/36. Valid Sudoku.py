class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (self.is_row_valid(board) and self.is_col_valid(board) and self.is_square_valid(board))
    
    def is_row_valid(self,row, board):
        hashrowset = set()
        for i in range(0,8):
            if board[row][i] in hashrowset:
                return False
            if board[row][i] != "."
                hashrowset.add(board[row][i])
         return True
      
   def is_col_valid(self,col, board):
        hashcolset = set()
        for i in range(0,8):
            if board[i][col] in hashrowset:
                return False
            if board[row][i] != "."
                hashrowset.add(board[i][col])
         return True
      
    def is_square_valid(self,col, board):
        hashsqset = set()
        for i in range(a,3):
          for j in range(b,3):
              curr = board[i][j]
            if board[i][j] in hashrowset:
                return False
         return True  
   
  
  

            
