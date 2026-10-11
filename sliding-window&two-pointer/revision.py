# def lengthOfLongestSubstring(s) -> int:
#         n=len(s)
#         j=0
#         maxi=0
#         hashmap={}
#         for i in range(n):
#             if s[i] in hashmap and hashmap[s[i]]>=j:
#                 j=hashmap[s[i]]+1
            
#             hashmap[s[i]]=i
#             maxi=max(maxi,i-j+1)
        
#         return maxi



# s ="ccbbcc"
# print(lengthOfLongestSubstring(s))



def totalFruit(fruits):
        hashmap={}
        n=len(fruits)

        for i in range(n):

            if fruits[i] in hashmap:
                hashmap[fruits[i]]+=fruits[i]
            
            else:
                hashmap[fruits[i]]=fruits[i]
        
        
        max1=0
        total_count1=0
        for item,val in hashmap.items():

            if val>total_count1:
                total_count1=val
                max1=item
        

        max2=0
        total_count2=0

        for item,val in hashmap.items():

            if val>total_count2 and item!=max1:
                total_count2=val
                max2=item
        

        count=total_count1//max1
        count+=total_count2//max2

        return count



fruits =[1,2,1]
print(totalFruit(fruits))