#1usd=83Inr

def USDtoINR(usd):
    INR=83.8138
    return usd*INR

usd=int(input("Enter The Money IN USD:"))
print(f"{usd} USD is {USDtoINR(usd)} INR")