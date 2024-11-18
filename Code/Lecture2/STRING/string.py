str1="Aditya"
str2='Ruchita'
str3='''hello World'''
print(str1 , str1,str2)

#ExtraLine
str4="HI GUys I am aditya savant I am from Ambavane"
print(str4)

#Length Of String

print(len(str4))

#Slicing in the string
print(str4[2:4])
print(str4[1:])
print(str4[:4])
print(str4[-3:-1])
print(str4[-1:])

##Function For String
print(str4.endswith("vane"))  #return True Or False
print(str4.capitalize())   #Capitialize First Character
print(str4.replace("U","u")) #Replace all occurences of old one with new one
print(str4.find("aditya")) #return the index of the passing strings
print(str4.count("I"))  #Count the how many times charchater length

