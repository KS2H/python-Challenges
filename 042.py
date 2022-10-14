total = 0
for i in (1,6):
    num = int(input("Enter a number: "))
    answer = input("Will you do more numbers, yes or no?: ")
    if answer == "yes":
        total = (total+num)
    else:
        total = total