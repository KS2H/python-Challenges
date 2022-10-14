name = input("Please enter your name: ")
namelength = len(name)
if namelength < 5:
    firstname = input("Please enter your firstname: ")
    fullname = firstname+name
    fullname = fullname.upper()
    print(fullname)
else:
    name = name.lower()
    print(name)
