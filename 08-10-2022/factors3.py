#display the factors
def main():
    
    print("Enter number: ")
    No = int(input())
    
    print("Factors are: ")
    #Ithe aapan divide by 2 karun time complexities kami keli..
    i = 1
    while i < int((No/2)+1):
        if No % i == 0:
            print(i)
        i = i + 1
            

#starter it is good way of programming...
if __name__ == "__main__":
    main()
    