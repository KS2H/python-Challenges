from array import *
num1 = array('i',[])
for i in range(5):
    answer = int(input("enter a number : "))
    num1.append(answer)
num1 = sorted(num1)
for j in num1:
    print(j)
answer2 = int(input("select a number form the array : "))
if answer2 in num1:
    num1.remove(answer2)
    num2 = array('i',[])
    print(num1)
    num2 = array('i',[])
    num2.append(answer2)
    print(num2)
else:
    print('error')