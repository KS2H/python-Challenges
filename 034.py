import math
anynum = int(input("1) Square\n2) Triangle\n\nEnter a number: "))
if anynum == 1:
    square = int(input("Enter one side of the rectangle: "))
    answer = square*square
    print(answer)
elif anynum ==2:
    trianglebase = int(input("Enter the base of the triangle: "))
    triangleheight = int(input("Enter the height of the triangle: "))
    answer = (trianglebase*triangleheight) // 2
    print(answer)
else:
    print("Error messeage")