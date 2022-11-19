def Display(No):
    if(No > 5):
        No = No - 1
        Display(No)
        print(No)   #tail recursion
       
        
        
Display(5)
