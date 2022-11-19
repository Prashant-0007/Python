print("Application to demostrate Industrial program")

def Addition(value1,value2):
    Ans = value1 + value2
    return Ans
    
def main():
    print("Enter First Number : ")
    no1 = int(input())   #input function always take string value note this one.

    print("Enter Second Number : ")
    no2 = int(input())

    sum = Addition(no1,no2)
    print("Addition is : ",sum)

if __name__ == "__main__":  #: colon started the block
    main()
    

