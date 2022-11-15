from array import *
nums1 = array('i',[])
nums2 = array('i',[12,56,78,45,125])
for i in range(3):
    answer = int(input("enter a number : "))
    nums1.append(answer)
for j in nums1:
    nums2.append(j)
nums2 = sorted(nums2)
for y in nums2:
    print(y)