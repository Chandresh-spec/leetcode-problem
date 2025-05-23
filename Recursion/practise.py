# def subset(num):
#     ds=[]
#     def helper(index,count):
        
#         if index==len(num):
#             ds.append(count)
#             return 
        
#         helper(index+1,count+num[index])
#         helper(index+1,count)

#     helper(0,0)
#     return ds

# num=[5, 2, 1]
# print(subset(num))

# def combination_sum(candidates,target):
#     ans=[]
#     def helper(index,ds,target):
#         if len(candidates)==index:
#             if target==0:
#                 ans.append(ds[index])
#             return
        
#         if target>candidates[index]:
#             ds.append(candidates[index])
#             helper(index,ds,target-candidates[index])
#             ds.pop()
#         helper(index+1,ds,target-candidates[index])
    
#     helper(0,[],0)
#     return ans


# candidates = [2,3,6,7]
# target = 7


# def partition(s):
#         ans=[]
#         def helper(index,ds):
#             if index==len(s):
#                 ans.append(ds[:])
#                 return 
#             for i in range(index,len(s)):
#                 if ispallindrome(index,i,s):
#                     ds.append(s[index:i+1])
#                     helper(index+1,ds)
#                     ds.pop()
    
        
#         def ispallindrome(st,end,s):
#             while st <= end:
#                if s[st]!=s[end]:
#                   return False
#                st+=1
#                end-=1
            
#             return True
    
#         helper(0,[])
#         return ans


# s = "aab"
# print(partition(s))


def exist(board, word):
        def helper(r,c,index):
            if index==len(word):
               return True
            
            if r<0 or r>=len(board) or c<0 or c>=len(board[0]) or word[index]!=board[r][c]:
               return False
            
            temp=board[r][c]
            board[r][c]="#"

            found=(helper(r+1,c,index+1)or
                   helper(r-1,c,index+1)or
                   helper(r,c+1,index+1)or 
                   helper(r,c-1,index+1)
                   
                   )
            board[r][c]=temp
            return found


          
           
    



        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(i,j,0):
                    return True
            
    
        return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEEA"
print(exist(board, word))