class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columnval=0
        columnhash = [set() for _ in range(9)]
        boxhash = [set() for _ in range(9)]
        boxval=0
        rowval=0
        for i in board:
            rowhash=set()
            for j in i:
                if j!='.':
                    if j in rowhash:
                        return False
                    rowhash.add(j)
                    if j in columnhash[columnval]:
                        return False
                    columnhash[columnval].add(j)
                    boxval=(rowval//3)*3 + columnval//3
                    if j in boxhash[boxval]:
                        return False
                    boxhash[boxval].add(j)
                columnval+=1
                continue
            rowval+=1
            columnval=0
        return True