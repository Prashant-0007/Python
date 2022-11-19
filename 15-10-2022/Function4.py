#functions which accepts 2 arguments and return one arguments

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

    
 #Fucntion accepts one parameter and returns one argument   
def main():
    print("Inside main")
    Demo1()
    Demo2(11)
    Ans = Demo3(10)
    print("Return value of demo3 is : ",Ans)
    Ans = Demo4(10,11)
    print("Addtion value from Demo4 is : ",Ans)
    
if __name__ == "__main__":
    main()