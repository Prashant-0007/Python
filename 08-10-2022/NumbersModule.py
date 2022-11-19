#display the factors of number
def DisplayFactors(No):
    print("Factors are: ")
    #Ithe aapan divide by 2 karun time complexities kami keli..
    i = 1
    while i < int((No/2)+1):
        if No % i == 0:
            print(i)
        i = i + 1
        