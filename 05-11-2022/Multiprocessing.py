def DisplayEven(No):

 for i in range(No):
        if(i % 2 == 0):
            print("Even Number :",i)
           

def DisplayOdd(No):

    for i in range(No):
        if(i % 2 != 0):
            print("Odd Number :",i)
        
        

def main():
    
    print("Demostration Of Serial Programming")
    DisplayEven(2000)
    DisplayOdd(2000)

if __name__ == "__main__":
    main()