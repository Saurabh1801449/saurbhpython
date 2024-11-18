def factorialNumber(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact    

print(f"The Factoral Of 5 is {factorialNumber(4)}")