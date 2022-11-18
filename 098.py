simple_array = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
print(simple_array)
line = int(input("Please enter a line : "))
print(simple_array[line])
answer = int(input("enter a number : "))
simple_array[line].append(answer)
print(simple_array[line])