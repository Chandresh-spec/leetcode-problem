def wordserach(board,word):
    found=False
    def helper(r,c,index):
        if index==len(word):
            return True
        
        if r<0 or r>=len(board) or c<0  or c>=len(board[0]) or word[index]!=board[r][c]:
            return False
        
        temp=board[r][c]
        board[r][c]="#"
        
        found=(helper(r+1,c,index+1)or
               helper(r-1,c,index+1)or
               helper(r,c+1,index+1)or
               helper(r,c-1,index+1))
        
        board[r][c]=temp
        return found

        
        







    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if helper(i,j,0):
                return True
    
    return False

board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(wordserach(board,word))