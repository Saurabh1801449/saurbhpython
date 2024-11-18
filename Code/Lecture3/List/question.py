# #Q1.WAP to ask  the user to enter name of their 3 favourite movies and store them in list
# movie1=input("Enter the first Movie:")
# movie2=input("Enter the Second Movie:")
# movie3=input("Enter the Third Movie:")
# list1=[]
# list1.append(movie1)
# list1.append(movie2)
# list1.append(movie3)
# print(list1)

#Q2.WAP To Check Palindrome Of String
orginalList=[1,"abc","abc",1]
new=[]
copyList=orginalList.copy()
print(orginalList.reverse())
print(orginalList)
new=orginalList.copy()
print(new)
# new=orginalList.reverse().copy()
# print(new)
if(copyList==new):
    print("It Is Palindrome!")
else:
    print("It is not plaindrome")