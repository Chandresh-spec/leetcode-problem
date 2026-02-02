# def reverseString(s):
#     temp=""
#     ans=""
#     for char in s :
#         if char !=" ":
#             temp+=char
        
#         else:
#             if temp!=" ":
#                 if ans !="":
#                     ans=temp + " "+ans
                
#                 else:
#                     ans+=temp
            
#             temp=""
        
    
#     if temp:
#         if ans !="":
#             ans=temp + " "+ans
#         else:
#             ans+=temp
#     return ans


# s=  "  hello world  "
# print(reverseString(s))





def frequencySort(s: str) -> str:
        hashmap={}
        for char in s:
            hashmap[char]=hashmap.get(char,0)+1

        

        arr=sorted(hashmap.items(),key=lambda x:x[1],reverse=True)

       
        return "".join()



s= "tree"
print(frequencySort(s))