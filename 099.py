simple_array = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
print(simple_array)
line = int(input("Please enter a print line : "))
print(simple_array[line])
column = int(input("Please enter print column : "))
print(simple_array[line][column])
answer = input("Are you going to change this number? (y/n) : ")
while True:
    if answer == "y":
        number = int(input("enter a new number : "))
        simple_array[line][column]= number
        break
    elif answer == "n":
        break
    else:
        print("error try again")
        answer = input("Are you going to change this number? (y/n) : ")
print(simple_array[line])