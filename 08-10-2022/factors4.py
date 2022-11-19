
#import NumbersModule  
#from NumbersModule import DisplayFactors
#from NumbersModule import *
import NumbersModule as NUM # alias...

def main():    
    print("Enter number: ")
    No = int(input())
    NUM.DisplayFactors(No)
      
#starter it is good way of programming...
if __name__ == "__main__":
    main()
    