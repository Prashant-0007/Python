#Functions type
#1 Positional/required Arguments
#2 Keyword argument
#3 Default Argument
#4 Variable no of argument

#Positional Argument function 
def Add1(No1, No2):
    print("Positional/Required Argument Functions")
    print("Value of No1 : ",No1)
    print("Value of No2 : ",No2)
    return No1 + No2

#Keyword Argument function 
def Sub1(No1, No2):
    print("Keyword Argument Functions")
    print("Value of No1 : ",No1)
    print("Value of No2 : ",No2)
    return No1 - No2

def main():
    Ans = 0
    Ans = Add1(10, 11)
    print("Addition is : ",Ans)
    
    #Keyword Je No2 and No1 Je Navane pathavale explicitly Postio mahiti nasel tar keyword
    Ans = Sub1(No2 = 11,No1 = 10)
    print("Subtraction is : ",Ans)
    

if __name__ == "__main__":
    main()

