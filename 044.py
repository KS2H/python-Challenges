people = int(input("How many people will you invite to the party?\n"))
if people < 10:
    for i in range (1,people+1):
        name = input("What is the name of the friend you want to invite?")
        print(name,"has been invited")
else:
    print("too many people")