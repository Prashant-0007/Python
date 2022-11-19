#List Data type in python...

from logging.config import valid_ident


values  = [10, 20, 30, 40]  #list data type []..
print(values)
print(type(values))
print(len(values))

print(values[0])
print(values[1])
print(values[2])
print(values[3])

#Jar samja 4th index ;a 50 takaycha prayatn akela tar te error deil 
#karan out of index jatoy tu tyamule..

#value last la index madhe insert karanyasathi
values.append(50)
print(values)

#remove 20 at index 1 by using remove in-build functiom
values.remove(20)
print(values)

#check list datatype supports duplicate element or not
values.append(40)
print(values)

#check the type of list
print(type(values[0]))

#check along with interger can we add float value..
values.append(98.88)
print(values)

#how to insert new element at any randon index
values.insert(2,11)
print(values)

#outof index la value takun baghu 
values.insert(15,11)        #it work like append jas append madhe last la list chya data takato...
print(values)

#size of list
print("values of list",len(values))




#
