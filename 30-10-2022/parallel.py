import os
import multiprocessing

def Square(No):
    print("PID of worker process id {} for the input {}".format(os.getpid(),No))
    
    return (No*No)
    

def main():
    print("Process ID of our application is :",os.getpid())
    Data = [ 1, 2, 3, 4]
    Result = []
    
    pool = multiprocessing.Pool()
    
    Result = pool.map(Square, Data)
    
    print("Result after square operation is :",Result)
	
	
if __name__ == "__main__":
	main()
	
