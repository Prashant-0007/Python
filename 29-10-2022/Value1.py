class Value:
    
    def __init__(self, data):
        self.no = data
        
    def SumFactors(self):
        Sum = 0
        
        for i in range(1, self.no):
            if (self.no % i == 0):
                Sum = Sum + i
                
        return Sum
    
    def CheckPerfect(self):
        Ans = self.SumFactors()
        
        if(self.no == Ans):
            return True
        else:
            return False
        

def main():
    print("Please Enter Number :")
    A = int(input())
    
    obj = Value(A)
    
    Ret = obj.CheckPerfect()
    
    if (Ret == True):
        print("{} is a perfect Number".format(A))
    else:
        print("{} is not perfect Number".format(A))
	

if __name__ == "__main__":
	main()
	
	