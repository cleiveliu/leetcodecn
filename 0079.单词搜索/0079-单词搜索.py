class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        def h(board,i,j,cur,target,used):
            ret = False
            if board[i][j] == target[len(cur)]:
                cur += board[i][j]
                if cur == target:
                    return True
                if len(cur) >= len(target):
                    return False
                used[i][j] = True
                direcs = get_directions(i,j,len(board),len(board[0]))
                ret = any(h(board,x,y,cur,target,used) 
                          for x,y in direcs if not used[x][y])
            
            used[i][j] = False
            return ret
                        
        def get_directions(i,j,r,c):
            ret = []
            if i-1 >= 0:
                ret.append((i-1,j))
            if j-1 >= 0:
                ret.append((i,j-1))
            if i+1 < r:
                ret.append((i+1,j))
            if j+1 < c:
                ret.append((i,j+1))
            return ret
        used = [[False]*len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if h(board,i,j,'',word,used):
                        return True
        return False