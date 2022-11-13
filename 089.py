from array import *
import random
nums = array('i',[])
for i in range(5):
    num = random.randint(0,100)
    nums.append(num)
for j in nums:
    print(j)
