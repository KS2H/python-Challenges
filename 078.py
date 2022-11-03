tvlist = ["cooking show","making show","talent show","story broadcasting"]
for i in tvlist:
    print(i)
anothertvshow = input("Please enter another broadcast program")
whereshow = int(input("What number should I add to the TV show list?"))
tvlist.insert(whereshow-1,anothertvshow)
for i in tvlist:
    print(i)