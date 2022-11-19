import os

def main():
	print("PID of current : ",os.getpid())
	print("PID of parent process :",os.getppid())
	
if __name__ == "__main__":
	main()
	
