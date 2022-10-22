import random
num = random.randint(1,5)
answer = int(input("Enter a number 1 ~ 5"))
if answer < num:
    print("higher than this anmswer")
    answer = int(input("try again"))
    if answer == num:
        print("Correct")
    else:
        print("You lose")
elif answer > num:
    print("lower than this number")
    answer = int(input("try again"))
    if answer == num:
        print("Correct")
    else:
        print("You lose")
elif answer == num:  
    print("Well done")