num = int(input("enter a number 10 beetween 20\n"))
while num <= 10 or num >= 20:
    if num <= 10:
        print("too low")
    elif num >= 20:
        print("too high")
    num = int(input("try again\n"))
print("Thank you")