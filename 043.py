answer = input("count up or down u/d\n")
if answer == "u":
    up = int(input("Please enter a number\n"))
    for i in range (1,up+1):
        print(i)
elif answer == "d":
    down = int(input("Please enter a number less than 20\n"))
    for i in range (20,down-1,-1):
        print(i)
else:
    print("i don't understand")