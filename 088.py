from array import *
nums = array('i',[])
for i in range(5):
    newValue = int(input("Enter number\n"))
    nums.append(newValue)
nums = sorted(nums)
print(nums)