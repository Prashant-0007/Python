print("Demonstration of tuple iteration")

# Data : heterogenous
# Ordered : Yes
# Indexed : Yes
# Mutable : No
# Duplicate : Yes 


Data = (11, 21, 51, 100)

print("Output Using for loop")
for no in Data:
    print(no, end=" ")
print()

print("Output Using for loop with index")
for no in range(0,len(Data)):
    print(Data[no], end=" ")
print()

print("Output Using while loop with index")
i = 0
while i < len(Data):
    print(Data[i], end=" ")
    i += 1
print()





