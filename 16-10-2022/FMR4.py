CheckEven = lambda No:(No%2 == 0)
Doubles = lambda No:(No*2)


def filterX(Helper_Function, Data):
    Result = []
    for i in range(0,len(Data),1):
        if(Helper_Function(Data[i]) == True):
            Result.append(Data[i])
            
    return Result
def mapX(Helper_Function,Data):
    Result = []
    for no in Data:
        Value = Helper_Function(no)
        Result.append(Value)
        
    return Result

def main():
    print("Enter Number Of elements you want to enter:")
    iSize = int(input())
    
    Data_Input = []
    print("Please enter the data in list : ")
    for iCnt in range(0, iSize, 1):
        Value = int(input())
        Data_Input.append(Value)
    print("Created List is : ",Data_Input)
    
    Data_Filter = filterX(CheckEven, Data_Input)
    print("Data After Filter is : ",Data_Filter)
    
    Data_Map = mapX(Doubles, Data_Filter)
    print("Data after map is :",Data_Map)
        
    
if __name__ == "__main__":
    main()