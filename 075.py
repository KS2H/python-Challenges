numberlist = [123,456,789,159]
for i in numberlist:
    print(i)
answer = int(input("enter a three digit number"))
if answer in numberlist:
    print(numberlist.index(answer))
else:
    print("That is not in the list")