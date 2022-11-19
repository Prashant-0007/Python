#functions which accepts 2 arguments and return one arguments

from tkinter import N


def Demo1():
    print("Inside Demo1")

def Demo2(No):
    print("Inside Demo2 with argument : ",No)
def Demo3(No):
    print("Inside Demo3 with arguments : ", No)
    return No+2
def Demo4(No1, No2):
    print("Inside demo4 ")
    Add = No1 + No2
    return Add
#Function accepts two parameter and return two parameters
def Demo5(No1, No2):
    print("Inside demo5 :")
    Add = No1 + No2
    Sub = No1 - No2
    return Add, Sub

    
 #Fucntion accepts one parameter and returns one argument   
def main():
    
    print("Inside main")
    Demo1()
    
    Demo2(11)
    
    Ans = Demo3(10)
    print("Return value of demo3 is : ",Ans)
    
    Ans = Demo4(10,11)
    print("Addtion value from Demo4 is : ",Ans)
    
    Ans1, Ans2 = Demo5(11, 10)
    print("first return value is :",Ans1)
    print("second return value is :",Ans2)
    
if __name__ == "__main__":
    main()