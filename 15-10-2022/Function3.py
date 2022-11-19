#functions which accepts arguments and return one arguments

def Demo1():
    print("Inside Demo1")

def Demo2(No):
    print("Inside Demo2 with argument : ",No)
def Demo3(No):
    print("Inside Demo3 with arguments : ", No)
    return No+2
    
 #Fucntion accepts one parameter and returns one argument   
def main():
    print("Inside main")
    Demo1()
    Demo2(11)
    Ans = Demo3(10)
    print("Return value of demo3 is : ",Ans)
    
if __name__ == "__main__":
    main()