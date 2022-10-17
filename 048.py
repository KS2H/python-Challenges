count = 0
again = "y"
while again == "y":
    name = input("What is the name of the friend you want to invite?\n")
    print(name,"has been invited")
    count += 1
    again = input("Will you invite more people? (y/n) \n")
print(count,"people join the party")