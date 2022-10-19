cunpnum = 50
num = 0
count = 0
while cunpnum != num:
    num = int(input("enter a number"))
    if num > cunpnum:
        print("less than this number try again")
    elif num < cunpnum:
        print("more than this number try again")
    count = count + 1
print("Well done, you took",count,"attempts")