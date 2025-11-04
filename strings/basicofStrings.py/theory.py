# # string is sequence of character enclosed in quotes


# # single='chandresh'
# # db="moger"
# # trip='''moger'''


# # print(single)
# # for i in single:
# #     print(i)


# # 
# # 
# # name="chandresh"
# # 
# # print(name.endswith('sh'))
# # 
# # name="moge, moger "
# # 
# # l=name.split(',')
# # print(l)
# # 
# # 
# # s="madum"
# # print(s[::-1])
# # 
# # 
# # count=0
# # for num in s:
#     # if num in "aeiou":
#         # count+=1
#     # 
# # print(count)
# # 
# # 
# # lne=len(s)-1
# # n=len(s)//2
# # for i in range(n):
#     # if s[i]!=s[lne-i]:
#         # print(False)
#     # 
# # print(True)


# s="aabbcde"

# for char in s :
#     if s.count(char)==1:
#         print(char)
#         break


# s='  cha  n d '

# n=s.replace(" ","")
# print(n)a



# s="my name is chandu"
# for i in range(s):
    # print()


nums= "the sky is blue"
s1=""
s2=""
for i in range(len(nums)-1,-1,-1):
    char=nums[i]
    if char!=" ": 
        s1=s1+char
    else:
        if char ==" ":
            if s1!= " ":
                s2=s1+" "+s2
            
    
print(s2)

