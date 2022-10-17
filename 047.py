num = int(input("Enter a number\n"))
total = num
again = "y"
while again == "y":
    num2 = int(input("Enter a another number\n"))
    total = total + num2
    again = input("would you like to add more numbers (y/n)\n")
print(total)


