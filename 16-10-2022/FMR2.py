from multiprocessing.sharedctypes import Value


def main():
    print("Enter Number Of elements you want to enter:")
    iSize = int(input())
    
    Data_Input = []
    print("Please enter the data in list : ")
    for iCnt in range(0, iSize, 1):
        Value = int(input())
        Data_Input.append(Value)
    print("Created List is : ",Data_Input)
        
    
if __name__ == "__main__":
    main()