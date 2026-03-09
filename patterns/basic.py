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
#     for i in range(n):
#         print("*"*5)



# n=5
# print(basic3(n))




def basic5(n):
    for i in range(n+1):
        print(" "*(n-i),"*"*i)



n=5
basic5(n)



def basic6(n):
    for i in range(n):
        print(" "*i,"*"*(n-i))

n=5
basic6(n)