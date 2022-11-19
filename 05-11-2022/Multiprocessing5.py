import time
import multiprocessing

def DisplayEven(No):

 for i in range(No):
        if(i % 2 == 0):
            print("Even Number :",i)
           

def DisplayOdd(No):

    for i in range(No):
        if(i % 2 != 0):
            print("Odd Number :",i)
        
        

def main():
    
    print("Demostration Of Parallel Programming Using Multiple Processess")
    Number = 200000
    
    P1 = multiprocessing.Process(target = DisplayEven, args = (Number,))
    P2 = multiprocessing.Process(target = DisplayOdd, args = (Number,))
    
    P1.start()
    P2.start()
	
    P1.join()
    P2.join()
    
    
    print("End Of Main")

if __name__ == "__main__":
    start_time = time.process_time()    
    main()
    end_time = time.time()
    print("Execution time is : ",end_time - start_time)
    