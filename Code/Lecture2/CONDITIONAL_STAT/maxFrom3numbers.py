a=int(input("Enter the Firts numbers:"))
b=int(input("Enter the Second numbers:"))
c=int(input("Enter the third numbers:"))
print()
if(a>b and a>c):
    print(f"{a} is greater among three")  #Here we use indentation for proper spacing!
elif(b>a and b>c):
    print(f"{b} is greater among three")
else:
    print(f"{c} is greater among three")
print("Thank You!")    