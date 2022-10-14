name = input("what is your name?: ")
count = int(input("How many times will I print your name?: "))
if count < 10:
    for i in range(1, count+1):
        print(name)
else:
    print("Too high")