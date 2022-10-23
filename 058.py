import random
truecount = 0
for i in range(1,6):
    num1 = random.randint(1,9)
    num2 = random.randint(1,9)
    print(num1,"+",num2,"=")
    answer = int(input("enter a answer"))
    true = num1 + num2
    if true == answer:
        print("correct!")
        truecount += 1
    else:
        print("wrong")
print("you got the answer right",truecount,"times")
    