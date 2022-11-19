import schedule
import time
import datetime
   
def Task_Minute():
    print("Task Based On Minutes Scheduled at :",datetime.datetime.now())

def Task_Hour():
    print("Task Based On Hours Scheduled at :",datetime.datetime.now())
    
def Task_Day():
    print("Task Based On Day Scheduled at :",datetime.datetime.now())
   
   
def main():
    print("Inside Task Scheduler")
    print("Current Time :",datetime.datetime.now())
    
    schedule.every(1).minutes().do(Task_Minute)
    schedule.every(1).hour().do(Task_Hour)
    schedule.every().saturday.at("18:00").do(Task_Day)
  
    while(True):
        schedule.run_pending()
        time.sleep(1)
    
    
if __name__ == "__main__":
    
    main()