#Accept 2 numbers and performs add and sub of it.

#Kay karayacha ahe? ->Behaviours(Of Functions)
#Addtion ani Subtraction

#Te karayala kay lagnar ahe?    ->Characteristics(Data)
# 2 numbers lagnar ahe.

# Class = Characteristics + Behaviours
# Class = Data + Functions

class Arithmatic:
    #In python if you want to do characteristics you have to write constructor.
    def __init__(self,A,B): #constructor
        self.No1 = A
        self.No2 = B
        
    def Add(self):
        return self.No1+self.No2
    
    def Sub(self):
        return self.No1-self.No2
    
    

def main():
    print("Enter First Number:")
    value1 = int(input())
    
    print("Enter second Number:")
    value2 = int(input())
    
    obj = Arithmatic(value1,value2)
    
    Ans= obj.Add()
    print("Addition is :",Ans)
    
    Ans= obj.Sub()
    print("Addition is :",Ans)
    
        
if __name__ == "__main__":
    main()
    

    