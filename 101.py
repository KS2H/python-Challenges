sales = {"Jone":{"N":3056,"S":8463,"E":8441,"W":2649},"Tom":{"N":4832,"S":6786,"E":4737,"W":3612},
"Anne":{"N":5239,"S":4802,"E":5820,"W":1859},"Fiora":{"N":3904,"S":3645,"E":8821,"W":2451}}
print(sales)
name = input("Enter a name : ")
region = input("Enter a region : ")
print(sales[name][region])
answer = input("Are you going to change the data? (y/n) : ")
while True:
    if answer == "y":
        name = input("Enter the name of the data you want to change : ")
        region = input("Enter the name of the region you wish to change : ")
        for i in sales:
            print(sales[i][region])
        new = input("Enter a value to replace : ")
        (sales[name][region]) = new
        for i in sales:
            print(sales[i][region])
        break
    elif answer == "n":
        break
    else:
        print("error try agian")
        answer = input("Are you going to change the data? (y/n) : ")

