'''def Display(No):
    while(No > 0):
        print(No)
        No = No - 1
        
        
Display(4)
        '''
def Display(No):
    if(No > 5):
        print(No) 
        No = No - 1
        Display(No)
       
        
        
Display(5)
        