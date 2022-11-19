import sys

print("Recusion Limit :",sys.getrecursionlimit())
sys.setrecursionlimit(3001)
print("New Recusion Limit :",sys.getrecursionlimit())
'''
def Display(No):
    iCnt = 0
    
    while(iCnt < No):
        print("Hello!!")
        iCnt += 1
        Display(5)

Display(5)'''
