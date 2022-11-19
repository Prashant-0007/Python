values = [10, 20 ,30, 40, 50]

print(values[0])
print(values[1])
print(values[2])
print(values[3])
print(values[4])

#traverse list by using for
for i in range(0, len(values), 1):
    print("i : ",i)
    print("value[i] : ", values[i])

for no in values:
    print(no)
