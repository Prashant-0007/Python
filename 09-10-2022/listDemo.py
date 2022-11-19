print("demostration of list data-type")

# Data : heterogenous
# Ordered : Yes
# Indexed : Yes
# Mutable : Yes
# Duplicate : Yes 

data = [11, 21, 51, 10]

data1 = [11, 90, 80, True, "hello"] #Heterogenous.
data1 = [11, 90.60, True, "Hello There!!"]

print("Data is heterogenous : ", data1)
print("Data is ordered :",data1)
print("Data at index 2:", data1[2])
print("Data with duplicate elements: ",data1)

print("List is mutable")
data.append(201)
print("data after append : ",data)
data.pop()
print("data after pop : ",data)