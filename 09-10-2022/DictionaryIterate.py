print("Demostration of Dictionary data types Iteration")

Batches = {"PPA" : 18000, "LB": 16700, "Python": 16500, "Angular" : 15000 }

print("Iterate using for loop")

for x in Batches:
    print(x)
    
print("Data traversal  using for loop")

for x in Batches:
    print(x, " : ",Batches[x])
    
print("Data traversal  using for loop  using get method")

for x in Batches:
    print(x, " : ",Batches.get(x))
    
#If you want take key of
keybatches = Batches.keys()
print("Keys Of Dictionary batches : ",keybatches)
print(type(keybatches))

valuesbatches = Batches.values()
print("values Of Dictionary batches : ",valuesbatches)
print(type(valuesbatches))

