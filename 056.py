import random
num = random.randint(1,10)
answer = int(input("Enter a number 1 ~ 10\n"))
while num != answer:
    answer = int(input("try again\n"))
print("Thank you")