print("Application to demostrate Industrial program")

def main():
    print("Enter First Number : ")
    no1 = int(input())   #input function always take string value note this one.
    print(type(no1))
    print("Enter Second Number : ")
    no2 = input()
    print(type(no2))
    ans = no1 + int(no2)
    print("Addition is : ",ans)

if __name__ == "__main__":  #: colon started the block
    main()

