def Hello(FPTR):
    print("Inside Hello")
    FPTR()

def Fun():
    print("Inside Fun")
    
def Demo():
    print("Inside Demo")
    

Hello(Demo)
Hello(Fun)
