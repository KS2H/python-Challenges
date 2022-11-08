name = input("enter a name")
count = 0
for i in name:
    if i == "a" or name == "e" or name == "i" or name == "o" or name == "u":
        count = count + 1
print("There is",count,"English vowel")