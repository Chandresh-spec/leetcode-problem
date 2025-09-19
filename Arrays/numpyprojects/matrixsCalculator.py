import numpy as np
class MatrixCalculator:
    def __init__(self,rows,cols):
        self.rows=rows
        self.cols=cols
    


    def add_matrix(self,a,b):
        print("Matrix A:")
        print(a)
        print("Matrix B:")
        print(b)
        print("_"*40)
        add_a=np.array(a)
        add_b=np.array(b)

        print("Sum of Matrix is :")
        print(add_a+add_b)

    
    def subtract_matrix(self,a,b):
        print("Matrix A:")
        print(a)
        print("Matrix B:")
        print(b)
        print("-"*40)

        print("Substraction of Matrix A and B is :")

        sub_a=np.array(a)
        sub_b=np.array(b)

        print(sub_a-sub_b)

        






row=int(input("Enter the number of row you want to insert:  "))
col=int(input("Enter the number of Column you want to insert:  "))

obj=MatrixCalculator(row,col)



def take_output(first,row,col):
    
    if first:
        print("Enter The Value For Matrix A")
    else:
        print("Enter the Value for matrix B")
    matrix_list=[]
    for i in range(row):
        matrix_row=[]
        for j in range(1,col+1):
           matrix_row.append(int(input(f"Enter Element at Row {i+1}, Col{j}:")))
    

        matrix_list.append(matrix_row)


    return np.array(matrix_list)



print("WELCOME TO MATRIX CALCULATOR")
print("1.ADDITION\n2.SUBTRACTION ")
choice=int(input("CHOOSE A NUMBER [1,2]:  "))



if  choice ==1:
    a=take_output(True,row,col)
    b=take_output(False,row,col)

    obj.add_matrix(a,b)

elif choice == 2:
    a=take_output(True,row,col)
    b=take_output(False,row,col)

    obj.subtract_matrix(a,b)




