class Numbers:

    def __init__(self):
        print("Inside Init Method")
        self.Size = 0
        self.Arr = list()
        
    def Accept(self):
        print("Enter How many elemetns you Want : ")
        self.Size = int(input())
        
        print("Please Enter The Elements : ")
        for i in range(0, self.Size, 1):
            Value = int(input())
            self.Arr.append(Value)
        
    def Display(self):
        print("Elements from list are : ")
        for i in range(0, self.Size, 1):
            print(self.Arr[i])
    
    def Summation(self):
        Sum = 0 
        for no in self.Arr:
            Sum = Sum + no
        
        return Sum
        
    def Average(self):
        Sum = 0
        for i in range(0, self.Size):
            Sum  = Sum + self.Arr[i]
        
        return (Sum/self.Size)
        
    def Maximum(self):
        Max = self.Arr[0]
        for i in range(0, self.Size):
            if self.Arr[i]> Max:
                Max = self.Arr[i]
        
        return Max
    

def main():
    
    obj = Numbers()
    obj.Accept()
    obj.Display()
    
    Output = obj.Summation()
    print("Summation of all elemetns : ", Output)
    
    Avg = obj.Average()
    print("Average Of All elements from list is : ", Avg)
    
    Max = obj.Maximum()
    print("Maximum from give list is : ", Max)
    
    
   

if __name__ == "__main__":
    main()