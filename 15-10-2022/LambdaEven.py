def chkEven(No):
    if(No % 2 == 0):
        return True
    else:
        return False
def chkEvenX(No):
    return (No % 2 == 0)
CheckEven = lambda No : (No%2==0)    
    
def main():
    ret = CheckEven(12)
    if(ret == True):
        print("True")
    else:
        print("False")
        
main()
    
    