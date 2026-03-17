# def pattern(n):
#     for _ in range(n):
#         print("*")



# n=4
# print(pattern(n))




# def basic2(n):
#     for i in range(n+1):
#         print("*"*i)




# n=5
# basic2(n)




# def basic3(n):
#     for i in range(n+1,-1,-1):
#         print("*"*i)




# n=5
# basic2(n)


# def basic4(n):
# #     for i in range(n):
# #         print("*"*5)



# # n=5
# # print(basic3(n))




# def basic5(n):
#     for i in range(n+1):
#         print(" "*(n-i),"*"*i)



# n=5
# basic5(n)



# def basic6(n):
#     for i in range(n):
#         print(" "*i,"*"*(n-i))

# n=5
# basic6(n)



# def basic21(n):
#     for i in range(1,n+1):
#         print("*"*i,end="")
#         print()
#     for i in range(n-1,-1,-1):
#         print("*"*i,end=" ")
#         print()



# # n=5
# # basic21(n)

# n=5
# # for i in range(1,n+2):
# #     for j in range(1,i):
# #       print(j,end=" ")
    
# #     print()



# for i in range(1,n+1):
#     for j in range(i):
#       print(i,end="")
    
#     print()



# n=5
# for i in range(n+1,-1,-1):
#     print("*"*i)



# n=5
# for i in range(n+1,-1,-1):
#     for j in range(1,i):
#         print(j,end="")
    
#     print()


# n=5
# for i in range(n):
#     for j in range(n-i+1,-1,-1):
#         print(" ",end="")
    
#     for k in range(2*i+1):
#         print("*",end="")
    
#     for l in range(n-i+1,-1,-1):
#         print(" ",end="")
    
#     print()



n=5
for i in range(n):
    for j in range(i):
        print(" ",end="")
    
    for k in range((n*2)-(2*i+1)):
        print("*",end="")
    
    for l in range(i):
        print(" ",end="")
    

    print()