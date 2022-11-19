import schedule
import time
import datetime

def Fun():
    print("Inside Fun")
    #Delay Might Be Here According to OS clock speed
    print("Current Time :",datetime.datetime.now())
    
def main():
    print("Inside Task Scheduler")
    print("Current Time :",datetime.datetime.now())
    
    schedule.every(1).minutes.do(Fun)
    while(True):
        schedule.run_pending()
        time.sleep(1)
    
    
if __name__ == "__main__":
    
    main()