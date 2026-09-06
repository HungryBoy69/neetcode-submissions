class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set() # already visited nodes will not be visited

        def dfs(r,c, i):
            if i == len(word):
                return True
            
            if ((min(r,c) < 0) # outside the bounds (lower bound)
                or r >= ROWS
                or c >=COLS # outside the bounds (upper bounds)
                or  word[i]!= board[r][c] # the character we are progressing does not match in the board
                or (r,c) in path): # what if for the next character we went back to the same visited cell to match the word
                    return False  


            path.add((r, c))
            res = (dfs(r+1, c, i+1) # down
                 or dfs(r-1, c, i+1) # up
                 or dfs(r, c+1, i+1) # right
                 or dfs(r, c-1, i+1)) # left
            
            path.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0): #means try from the combination of all the cells as the beginning point
                    return True
        return False