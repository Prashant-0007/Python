from functools import reduce

CheckEven = lambda No:(No%2 == 0)
Doubles = lambda No:(No*2)
Sum = lambda A,B:(A+B)

def main():
    print("Enter Number Of elements you want to enter:")
    iSize = int(input())
    
    Data_Input = []
    print("Please enter the data in list : ")
    for iCnt in range(0, iSize, 1):
        Value = int(input())
        Data_Input.append(Value)
    print("Created List is : ",Data_Input)
    
    Data_Filter = list(filter(CheckEven, Data_Input))
    print("Data After Filter is : ",Data_Filter)
    
    #typecast list madhe hyasathi karan tyachi return value list ahe.
    Data_Map = list(map(Doubles, Data_Filter))
    print("Data after map is :",Data_Map)
    
    Output = reduce(Sum,Data_Map)
    
    print("result after reduce is :",Output)   
    
if __name__ == "__main__":
    main()
    