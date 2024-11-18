

def showNum(num):
    if(num==0):
        return
    print(num)
    showNum(num-1)
    
showNum(8)   