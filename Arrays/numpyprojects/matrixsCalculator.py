import numpy as np
class MatrixCalculator:
    def __init__(self):
        pass
    


    def add_matrix(self,a,b):
        print("Matrix A:")
        print(a)
        print("Matrix B:")
        print(b)
        print("_________________________________________-")
        add_a=np.array(a)
        add_b=np.array(b)

        print("Sum of Matrix is :")
        print(add_a+add_b)

    
    def substract_matrix(self,a,b):
        print("Matrix A:")
        print(a)
        print("Matrix B:")
        print(b)
        print("_________________________________________-")

        print("Substraction of Matrix A and B is :")

        sub_a=np.array(a)
        sub_b=np.array(b)

        print(sub_a-sub_b)

        





obj=MatrixCalculator()



def take_output(first,row,col):
    matrix_list=[]
    if first:
        print("Enter The Value For Matrix A")
    else:
        print("Enter the Value for matrix B")
    for i in range(row):
        matrix_row=[]
        for j in range(1,col+1):
           matrix_row.append(int(input(f"Enter the {i+1}th Row  {j}th element:  ")))
    

        matrix_list.append(matrix_row)


    return matrix_list



print("WELCOME TO MATRIX CALCULATOR")
print("1.ADDITION\n2.SUBSTRACTION ")
choice=int(input("CHOOSE A NUMBER [1,2]:  "))



if  choice ==1:
    row=int(input("Enter the number of row you want to insert:  "))
    col=int(input("Enter the number of Column you want to insert:  "))
    a=take_output(True,row,col)
    b=take_output(False)

    obj.add_matrix(a,b)

elif choice == 2:
    row=int(input("Enter the number of row you want to insert:  "))
    col=int(input("Enter the number of Column you want to insert:  "))
    a=take_output(True,row,col)
    b=take_output(False,row,col)

    obj.substract_matrix(a,b)




