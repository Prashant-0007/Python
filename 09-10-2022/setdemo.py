print("demostration of set data-type")

# Data : heterogenous
# Ordered : No
# Indexed : No
# Mutable : Yes
# Duplicate : No 

data = {11, 21, 51, 10}

data = {11, 90, 80, True, "hello",11,80, 90}         #No Duplicate
data1 = {11, 90.60, True, "Hello There!!"}  #Heterogenous.

print("First set data : ",data)
print("Length of data : ",len(data))
print("Data is heterogenous : ", data1)
print("Data is unordered :",data1)
#print("Data at index 2:", data1[2])    [] this bracket means data is not subcriptable in python..
print("Data with unique elements: ",data1)

print("set is mutable")
#Insert element in set
data.add(211)
print("Data after insertion : ", data)
#remove element from set
data.discard(211)   #Note discard function will remove element if there present if not then it simply go ahead.

print("Data after removal : ", data)