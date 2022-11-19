#4
# 4*3*2*1->24

def Fact(No):
    if(No <= 0):
        return 0
    else:
        return (No * Fact(No - 1))
    

Ret = Fact(4)

print("Factorial is :",Ret)