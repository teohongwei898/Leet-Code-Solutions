class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #2 binary search, search row first, then search within row.
        
        topRow= 0
        bottomRow = len(matrix)-1  #Numberof columns = len(matrix[0])
        
        while topRow<=bottomRow:
            middleRow = (topRow+bottomRow) //2            
            if target > matrix[middleRow][-1]:  #if target more than middle row last column, 
                topRow = middleRow + 1              #means dun care above one,
            elif target < matrix[middleRow][0]: #if target less than middle row first column, dun care below
                bottomRow = middleRow - 1
            else:
                break  #else in the correct row
                
        if not (topRow<=bottomRow):   #if not in any rows means ggwp
            return False
        
        targetRow = (topRow+bottomRow)//2
        L = 0
        R = len(matrix[0]) - 1
        
        while L<=R:
            middle = (L+R)//2
            if matrix[targetRow][middle] > target:
                R = middle -1
            elif matrix[targetRow][middle] < target:
                L = middle + 1
            else:
                return True
        return False
        
        
