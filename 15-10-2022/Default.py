#Functions type
#1 Positional/required Arguments
#2 Keyword argument
#3 Default Argument
#4 Variable no of argument

#default Argument Function
def Area(Radius, PI = 3.14):
    
    Result = PI * Radius * Radius
    return Result
    

def main():
    RValue = 10.5
    PIValue = 3.14
    
    #Positional
    Ans = Area(RValue, PIValue) #Internally Ans = Area(10.5, 3.14)
    print("Area Of Circle is :",Ans)
    
    #Keyword
    Ans = Area(Radius = RValue,PI = PIValue) #Internally Ans = Area(Radius = 10.5,PI = 3.14)
    print("Area Of Circle is :",Ans)
    
    #Positional argument and second is default
    Ans = Area(10.5)    
    print("Area Of Circle is :",Ans)
     
     #Keyword and second is default
    Ans = Area(Radius = 10.5)
    print("Area Of Circle is :",Ans)
    
    #Keyword argumnet
    Ans = Area(PI = 7.10, Radius = 10.5)
    print("Area Of Circle is :",Ans)

    

if __name__ == "__main__":
    main()

