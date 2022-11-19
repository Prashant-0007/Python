from functools import reduce

def main():
    print("Enter Number Of elements you want to enter:")
    iSize = int(input())
    
    Data_Input = []
    print("Please enter the data in list : ")
    for iCnt in range(0, iSize, 1):
        Value = int(input())
        Data_Input.append(Value)
    print("Created List is : ",Data_Input)
    
    Data_Filter = list(filter(lambda No:(No%2 == 0), Data_Input))
    print("Data After Filter is : ",Data_Filter)
    
    #typecast list madhe hyasathi karan tyachi return value list ahe.
    Data_Map = list(map(lambda No:(No*2), Data_Filter))
    print("Data after map is :",Data_Map)
    
    Output = reduce(lambda A,B:(A+B),Data_Map)
    
    print("result after reduce is :",Output)   
    
if __name__ == "__main__":
    main()