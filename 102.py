list = {}
for i in range(4):
    name = input("Please enter your name : ")
    age = int(input("Please enter your age : "))
    shoe = int(input("Please enter your shoe size : "))
    list[name]={"Age":age,"Shoe_size":shoe}
name = input("Please enter any list name : ")
print(list[name])