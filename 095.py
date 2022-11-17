from array import *
num = array('d',[35.45,47.12,14.56,86.15,99.18])
answer = int(input("enter a number 2 beetwen 5"))
while True:
    if answer >= 2 and answer <= 5:
        break
    else:
        print("Try again")
        answer = int(input("enter a number 2 beetwen 5"))
for i in range(0,5):
    innum = round(num[i]/answer,2)
    num.append(innum)
for j in range(5):
    del num[j-1]
num = sorted(num)
for y in num:
    print(y)