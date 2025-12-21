# 1859. Sorting the Sentence
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.
# 
# A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.
# 
# For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
# Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.
# 
#  
# 
# Example 1:
# 
# Input: s = "is2 sentence4 This1 a3"
# Output: "This is a sentence"
# Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.
# Example 2:
# 
# Input: s = "Myself2 Me1 I4 and3"
# Output: "Me Myself and I"
# Explanation: Sort the words in s to their original positions "Me1 Myself2 and3 I4", then remove the numbers.







# def sts(s):
    # maxi=0
    # for i in s:
        # if i.isdigit():
            # maxi=max(maxi,int(i))
# 
    # ans=[0]*maxi
    # char=""
# 
    # for i in s:
        # if i.isalpha():
            # char+=i
        # 
        # elif i.isdigit():
            # i=int(i)-1
            # ans[i]=char
            # char=""
        # 
    # 
    # return " ".join(ans)
# 
# 
# s = "Myself2 Me1 I4 and3"
# print(sts(s))
# 
            
    


def sts(s):
    s=s.split()
    arr=[""]*len(s)

    for i in range(len(s)):
        arr[int(s[i][-1])-1]=s[i][:-1]
    

    print(arr)



s = "Myself2 Me1 I4 and3"
print(sts(s))