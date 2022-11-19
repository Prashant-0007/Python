def Outer():
    print("Inside Outer")
    
    def Inner():
        print("Inside Inner")
    
    print(id(Inner))    
    return Inner
ret = Outer()
print("type of ret:",type(ret))
print("ID of ret :",id(ret))
ret()
