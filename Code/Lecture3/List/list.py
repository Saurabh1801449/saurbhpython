marks=[100,99,98,89,76,54]
print(marks)
print(type(marks))
student=["Aditya",45,"karan",True,None,"Nitya",67.43,"Kartik"]
print(student)
student[2]="Ruchita"
print(student)

#slicing
  #Same as string
print(student[1:4])
print(student[1:])  
print(student[-4:-2])



##List Specfic Functions

list1=[2,1,3]
list1.append(4)
print(list1)
print(list1.sort())
print(list1)
print(list1.sort(reverse=True))
print(list1)
list1.insert(1,45)
print(list1)
list1.remove(45)
print(list1)
list1.pop(1)
print(list1)



#LIST OF STRING
stringlist=["Aditya","Rohit","Ketan","Nachiket","Nitya","Ruchita","Aditi"]
print(stringlist.sort())
print(stringlist)
print(stringlist.reverse())
print(stringlist)

#Copy
list1=stringlist.copy()+list1
print(list1)

#clear
list1.clear()
print(list1)

#EXtend Functions:
list1.extend(stringlist)
print(list1)