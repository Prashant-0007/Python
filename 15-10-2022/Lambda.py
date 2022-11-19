#Lambda Function Is Also Called as Anonymous Function in python

#Normal Function / Named Function
def Add(No1, No2):
    return No1+No2

#Lambda functions/unamed function
#Lambda parameters : body

AddFunction = lambda A, B : A+B

Ans1 = Add(10,11)
Ans2 = AddFunction(10,12)

print("Addition using normal functions : ", Ans1)
print("Addition using lambda function :", Ans2)

print("Type Of lambda functions is:",type(AddFunction))

