import os

def Delet_File(FileName):
    if(os.path.exists(FileName)):
        os.remove("Prashant.txt")
        
    else:
        print("File is not existing")
        return  #there is no need to write return but for sake of understanding
	
def main():
    print("Enter the file name to delete")
    Name = input()
    
    Delet_File(Name)
    

if __name__ == "__main__":
	main()

