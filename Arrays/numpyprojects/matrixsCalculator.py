import numpy as np
class MatrixCalculator:
    def __init__(self,rows,cols):
        self.rows=rows
        self.cols=cols
    

    def print_matrix(self,op):
        print("Matrix A:")
        print(a)
        print("Matrix B:")
        print(b)
        print("_"*40)

        print(f" {op} of Matrix A and B is:")

    


    def add_matrix(self,a,b):
        self.print_matrix("Sum")
        print(a+b)
 
    
    def subtract_matrix(self,a,b):
        self.print_matrix("Subtrack")
        print(a-b)
    

    def Multiply_matrix(self,a,b):
        self.print_matrix("Element-Wise Multiplication")


        print(a*b)
    
    def dot_product_matrix(self,a,b):
           cal=np.dot(a,b)
           print("Dot Product Multiplication   of Matrix A and B is :")  
           print(cal)
        
    

    def division_ops(self,a,b):
         self.print_matrix("Element-Wise Division")

         print(a/b)

           






        






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
print("1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION")

choice=int(input("CHOOSE A NUMBER [1,2,3,4]:  "))



if  choice ==1:
    a=take_output(True,row,col)
    b=take_output(False,row,col)

    obj.add_matrix(a,b)

elif choice == 2:
    a=take_output(True,row,col)
    b=take_output(False,row,col)

    obj.subtract_matrix(a,b)

elif choice==3:
    print("1.Element-wise Multiplication")
    print("2.Matrix Multiplication (dot product)")
    choice_n=int(input("Enter the a choice : "))

    if choice_n==1:
        a=take_output(True,row,col)
        b=take_output(False,row,col)
        obj.Multiply_matrix(a,b)
    # elif choice_n==2:
        # row_=int(input("Enter the number of rows for A"))
    
elif choice==4:
     a=take_output(True,row,col)
     b=take_output(False,row,col)
     obj.division_ops(a,b)


    
        





