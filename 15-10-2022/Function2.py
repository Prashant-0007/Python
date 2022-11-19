#functions which accepts arguments and return nothing

def Demo1():
    print("Inside Demo1")

def Demo2(No):
    print("Inside Demo2 with argument : ",No)
    
 #Fucntion accepts one parameter and returns nothing   
def main():
    print("Inside main")
    Demo2(11)
    
if __name__ == "__main__":
    main()