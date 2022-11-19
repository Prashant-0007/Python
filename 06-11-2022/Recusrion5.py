def Display(No):
    if(No < 5):
        print(No)   #Head Recusion...
        No = No + 1
        Display(No)
       
        
        
Display(1)