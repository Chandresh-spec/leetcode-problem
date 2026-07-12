






# def subsequence(arr,k):

#     ans=[]
#     ds=[]
#     def helper(index,count):
#         if index==len(arr):
#             if count==k:
#                 ans.append(ds[:])
            
#             return
        

#         ds.append(arr[index])
#         helper(index+1,count+arr[index])
#         ds.pop()
#         helper(index+1,count)
    

    


#     def helper1(index,count):
#         if index==len(arr):
#             if count==k:
#                 ans.append(ds[:])
#                 return True
            
#             return False
        
#         ds.append(arr[index])
#         if (helper1(index+1,count+arr[index]))==True:
#             return True
#         ds.pop()
#         if (helper1(index+1,count))==True:
#             return True
    

#     def helper2(index,count):
#         if index==len(arr):
#             if count==k:
#                 return 1
        
#             return 0
        
#         l=helper2(index+1,count+arr[index])
#         r=helper2(index+1,count)
#         return l+r
    

#     return helper2(0,0)
    
       
        

    
    
        







# nums = [1, 2, 3, 4, 5] 
# k = 8
# print(subsequence(nums,k))



# def combinationSum2(candidates,target):

        # ans=set()
        # ds=[]
        # def helper(index,target):
        #     if index==len(candidates):
        #         if target==0:
        #             ds.sort()
        #             ans.add(tuple(ds[:]))

        #         return
            
        #     ds.append(candidates[index])
        #     helper(index+1,target-candidates[index])
        #     ds.pop()
        #     helper(index+1,target)
       
        # helper(0,target)
        # final_ans=[list(item)for item in ans]
        # return final_ans



#         ans=[]
#         ds=[]
#         def helper(index,target):
#             if target==0:
#                 ans.append(ds[:])
#                 return
            

#             for i in range(index,len(candidates)):
#                 if i>index and candidates[i]==candidates[i-1]:
                    
#                     continue

#                 if target<candidates[i]:
#                     break

#                 ds.append(candidates[i])
#                 helper(i+1,target-candidates[i])
#                 ds.pop()
        
#         helper(0,target)
#         return ans





# candidates = [1,2,2,2,5]
# target = 5
# candidates.sort()
# print(combinationSum2(candidates,target))






# def combinationSum3(k,n):
#         ans=[]
#         ds=[]
#         def helper(index,count,k,n):

#             if len(ds)==k:
#                  if count==n:
#                       ans.append(ds[:])
#                  return
            

#             for i in range(index,10):

#                 ds.append(i)
#                 helper(i+1,count+i,k,n)
#                 ds.pop()
        
#         helper(1,0,k,n)
#         return ans
        
        


# k=3
# n=7
# print(combinationSum3(k,n))





    
    
# def ispallindrome(index,i,s):
#     while i>index:
#         if s[i]!=s[index]:
#             return False
#         i-=1
#         index+=1
        
#     return True






# def partition(s: str):
    
#     ans=[]
#     ds=[]
#     def helper(index):
#         if index==len(s):
#             ans.append(ds[:])
#             return
        
#         for i  in range(index,len(s)):
            
#             if  ispallindrome(index,i,s)==False:
#                 continue
            
#             ds.append(s[index:i+1])
#             helper(i+1)
#             ds.pop()
#     helper(0)
#     return ans
        
        

# s = "baa"
# print(partition(s))




def exist(board,word):

    def helper(row,col,board,word,index,visited,m,n):

        if index==len(word):
            return True
        
        if col<0 or col>n-1 or row<0 or row>m-1 or visited[row][col]==True or board[row][col]!=word[index]:
            return False
        
        visited[row][col]=True
        

        if   (helper(row,col+1,board,word,index+1,visited,m,n)or
                helper(row,col-1,board,word,index+1,visited,m,n)or
                helper(row+1,col,board,word,index+1,visited,m,n)or
                helper(row-1,col,board,word,index+1,visited,m,n))==True:
            return True
            
        

        visited[row][col]=False

        
            
            
        












    m=len(board)
    n=len(board[0])
    visited=[[False for _ in range(n)]for _ in range(m)]
    print(visited)
    for i in range(m):
        for j in range(n):
            if board[i][j]==word[0]:
                if(helper(i,j,board,word,0,visited,m,n))==True:
                    return True
    
    return False


    

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"

print(exist(board,word))







     
       


        