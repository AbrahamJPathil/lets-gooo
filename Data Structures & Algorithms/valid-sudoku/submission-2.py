class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            currRow = board[i]
            numColl = set()
            for n in currRow:
                if n.isnumeric():
                    currNum = int(n)
                    if currNum in numColl:
                        return False
                    numColl.add(currNum)
        
        for i in range(9):
            numColl = set()
            for j in range(9):
                if board[j][i].isnumeric():
                    currNum = int(board[j][i])
                    if currNum in numColl:
                        return False
                    numColl.add(currNum)

        rowUb = 3
        prevRUb = 0
        colUb = 3
        prevCb = 0
        
        for i in range(9):
            numColl = set()
            for k in range(prevRUb, rowUb):
                for j in range(prevCb, colUb):
                    if board[k][j].isnumeric():
                        currNum = int(board[k][j])
                        if currNum in numColl:
                            return False
                        numColl.add(currNum)
            
            prevRUb = rowUb
            rowUb = rowUb + 3
            
            if (i + 1) % 3 == 0:
                prevRUb = 0
                rowUb = 3
                prevCb = colUb
                colUb += 3

        return True