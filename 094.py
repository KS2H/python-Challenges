from array import *
num1 = array('i',[12,15,25,67,95])
for i in num1:
    print(i)
answer = int(input("enter a number from the array : "))
while True:
    if answer in num1:
        print("this is position",num1.index(answer))
        break
    else:
        print("not in array")
        answer = int(input("enter a number from the array : "))