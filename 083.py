enter = input("Please enter capital letters")
while True:
    if enter.islower():
        print("try again")
        enter = input("Please enter capital letters")
    else:
        break
print("thank you")
