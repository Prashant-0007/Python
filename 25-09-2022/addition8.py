print("Application to demostrate Industrial program")

import prashantsModule
def main():
    print("Value of __name__ from main is : ",__name__)
    print("Enter First Number : ")
    no1 = int(input())   #input function always take string value note this one.

    print("Enter Second Number : ")
    no2 = int(input())

    sum = prashantsModule.Addition(no1,no2)
    print("Addition is : ",sum)

if __name__ == "__main__":  #: colon started the block
    main()
   

