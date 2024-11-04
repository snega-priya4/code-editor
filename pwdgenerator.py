import random

size = int(input("Enter Password Size , Not Less Than 8 characters: "))

caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small = "abcdefghijklmnopqrstuvwxyz"
num = "1234567890"
symbol = "!@#$%^&*?"

password = ""

if(size < 8):
    print("Invalid size.Size must be atleast 8 characters ")
else:
    for i in range(2):
        password = password + caps[random.randint(0,len(caps))]
    
    for i in range(2):
        password = password + num[random.randint(0,len(num))]
    
    for i in range(2):
        password = password + symbol[random.randint(0,len(symbol))]

    size -= 6

    while(size > 0):
        password = password + small[random.randint(0,len(small)-1)]
        size -= 1

print("Your Password Is : ",password)

    