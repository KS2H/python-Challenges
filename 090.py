from array import *
nums = array('i',[])
while True:
    if len(nums) < 5:
        num = int(input("enter a number between 1 and 20\n"))
        if num > 0 and num < 20:
            nums.append(num)
        else:
            print("outside the range")
    else:
        break
for j in nums:
    print(j)