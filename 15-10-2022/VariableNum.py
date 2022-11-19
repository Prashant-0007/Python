#Addtional variable number which are passing through caller function
from optparse import Values


def Add(*values):
    print(type(values)) #tuple yeil type karan values vhange nahi honar kadhich
    print("Number of arguments are :",len(values))
    #type tuple ahe mhanun loop ne traverse karun
    Sum = 0
    for no in values:
        Sum  = Sum + no
    
    return Sum 

def AddX(*values):
    Sum = 0
    for i in range(0, len(values),1):
        Sum = Sum + values[i] 
    
    return Sum
    
    

def main():
    Ans = AddX(10, 11,12)
    print("Addition is :",Ans)
    
if __name__ == "__main__":
    main()
    