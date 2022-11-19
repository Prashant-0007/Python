#Instance Variable : Name, Amount, Address, AccountNo
#Instance Method : CreateAccount(),Display_Acc_Info()
#Class Variable : Bank_Name, ROI_ON_FD
#class Variable : Bank_Name
#class Method : Bank_Information()
#static Method : DisplaKYCInfo()



class Bank_Account:

    #Class Variable
    Bank_Name = "HDFC Bank PVT LTD"
    ROI_ON_FD = 6.7
    
    def __init__(self):
    
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0
    
    def CreateAccount(self):
        print("Enter your name: ")
        self.Name = input()
        
        
        print("Enter your Initial Amount :")
        self.Amount = int(input())
        
        print("Enter your Address : ")
        self.Address = input()
        
        print("Please Enter your Account Number : ")
        self.AccountNo = int(input())
        
    def Display_Acc_Info(self):
        print("------Your Account information As Below------")
        print("Name Of Account Holder is :",self.Name)
        print("Account Number :",self.AccountNo)
        print("Address Of Account Holder is :", self.Address)
        print("Current Amount in account :",self.Amount)
    
    @classmethod
    def Bank_Information(cls):
        print("Welcome To Banking Console")
        print("Name Of our bank :",cls.Bank_Name)
        print("rate Of Interest on FD :",cls.ROI_ON_FD)
        
    @staticmethod
    def DisplaKYCInfo():
        print("Please consider below KYC Information ")
        print("According to the rules of Gov O India you have to Submit below Documents")
        print("1 : Clear And Recent password size photo")
        print("2 : Photo Of Aadhar Card ")
        print("3 : Photo Of PAN Card")
        
                       

def main():

    Bank_Account.DisplaKYCInfo()
    
    print("Name Of Bank :",Bank_Account.Bank_Name)
    print("Rate Of Annual Interest On Fixed Deposite : ",Bank_Account.ROI_ON_FD)
    
    Bank_Account.Bank_Information()
        
    User1 = Bank_Account()
    User2 = Bank_Account()
    
    User1.Bank_Information()
    
    print("Creating the Fisrt Account :")
    User1.CreateAccount()
    print("Creating the Second Account :")
    User2.CreateAccount()
    
   
    User1.Display_Acc_Info()
    
    User2.Display_Acc_Info()   


if __name__ == "__main__":
	main()
	