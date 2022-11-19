def CheckEven(No):
    return (No % 2 == 0)

def Increment(No):
    return No+2
def Add(A, B):
    return (A+B)

def FilterX(Arr, Function_Name):
    result = []
    for no in Arr:
        if(Function_Name(no)):
            result.append(no)
    return result
    
def MapX(Arr, Function_Name):
    Result = []
    for no in Arr:
        value = Function_Name(no)
        Result.append(value)
    return Result
def ReduceX(Arr, Function_Name):
        
    Sum = 0
    for no in Arr:
        Sum = Sum + no
    return Sum    

def main():
    data = [12, 3, 1, 6, 4, 5]
    print("Original Data : ", data)
    
    Data_Filtred = FilterX(data, CheckEven)
    print("Filtered data", Data_Filtred)
    
    Map_data =list(MapX(Data_Filtred, Increment))
    print("Data After Map : ",Map_data)
    
    
    
if __name__ == "__main__":
    main()