
def main():
    #create empty list
    Arr = list()
    print("Enter how many elements you want to store?")
    size = int(input())
    print("Please Enter the values :")
    
    for i in range(0, size):
        #Enter Values
        no = int(input())    
        Arr.append(no)

    print(Arr)    

if __name__ == "__main__":
    main()
