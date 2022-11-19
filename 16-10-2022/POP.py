def Add(A,B):
    return A+B

def Sub(A,B):
    return A-B

def main():
    print("Enter First Number:")
    No1 = int(input())
    
    print("Enter second Number:")
    No2 = int(input())
    
    Ans = Add(No1, No2)
    print("Addtion is : ",Ans)
    
    Ans = Sub(No1, No2)
    print("Subtraction is : ",Ans)
    
if __name__ == "__main__":
    main()
    

    