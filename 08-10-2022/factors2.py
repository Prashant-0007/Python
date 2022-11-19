#display the factors
def main():
    
    print("Enter number: ")
    No = int(input())
    
    print("Factors are: ")
    #Ithe aapan divide by 2 karun time complexities kami keli..
    for i in range(1, int((No/2)+1), 1):
        if No % i == 0:
            print(i)
            
       # i = i + 1
        

#starter
if __name__ == "__main__":
    main()
    