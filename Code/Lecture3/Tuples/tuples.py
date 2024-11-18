tuple1=(2,1,3,5,1,1,1)
print(tuple1)

#class
print(type(tuple1))

#Access Of Tuples Like List

print(tuple1[0])
print(tuple1[1])

##Immuatble 

##Empty Tuple
tup=()
print(tup)
tup1=(1,)  #If We avoid the comma then interpreter think like tuple is number
print(tup1)


##Slicing Workd Like List and string

#index
# tuple1.index(5)
print(tuple1.index(2))

#Count 
print(tuple1.count(1))