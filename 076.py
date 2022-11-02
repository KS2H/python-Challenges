namelist = []
for i in range(3):
    name = input("Write the name of the person you want to invite to the party")
    namelist.append(name)
answer = input("Will you invite more to the party? (y/n)")
while answer == "y":
    name = input("Write the name of the person you want to invite to the party")
    namelist.append(name)
    answer = input("Will you invite more to the party? (y/n)")
print(len(namelist))