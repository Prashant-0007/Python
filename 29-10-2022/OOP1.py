class Arithmetic:
    #Constructor
    def __init__(self, A, B):
        self.no1 = A
        self.no2 = B
        
    def Addition(self):
        Ans = self.no1 + self.no2
        return Ans
    
    def Substraction(self):
        Ans = self.no1 - self.no2
        return Ans
        
        
        

def main():
    print("Inside main Method")
    
    obj = Arithmetic(20, 10)
    Ans = obj.Addition()
    print("Addition is : ",Ans)
    Ans = obj.Substraction()
    print("Substraction is : ",Ans)

if __name__ == "__main__":
    print("Inside starter")
    main()