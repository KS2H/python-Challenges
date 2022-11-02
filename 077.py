namelist = []
for i in range(3):
    name = input("Write the name of the person you want to invite to the party\n")
    namelist.append(name)
answer = input("Will you invite more to the party? (y/n)\n")
while answer == "y":
    name = input("Write the name of the person you want to invite to the party\n")
    namelist.append(name)
    answer = input("Will you invite more to the party? (y/n)\n")
for i in namelist:
    print(i)
delname = input("Please enter a name from the list\n")
party = input("Are you really going to invite this person to the party? (y/n)\n")
if party == "n":
    namelist.remove(delname)
for i in namelist:
    print(i)