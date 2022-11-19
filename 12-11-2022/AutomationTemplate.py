from sys import *
from os import *

#Even number logic
def Script_Task(No):
    No = int(No)
    if(No % 2 == 0):
        print("It is Even number")
    else:
        print("It is Odd number")    

def main():
    print("---------------Demonstration of Automation Script------------------")
    print("Automation Script started with name :",argv[0])
    
    if(len(argv) != 2):
        print("Insufficient Argument")
        print("Use -h for help and use -u for usage of the script")
        exit()
        
    if(argv[1] == "-h" or argv[1] == "-H"):
        print("This Script is used to perform_____________")
        exit()
        
    elif(argv[1] == "-u" or argv[1] == "-U"):
        print("Usage : Provide______number of arguments as")
        print("First Argument as : ______")
        print("second Argument as : _______")
        exit()
    else:
        Script_Task(argv[1])
        print("There is no such option as :",argv[1])
        exit()
    
if __name__ == "__main__":
	main()
    