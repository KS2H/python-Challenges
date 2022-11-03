nums = []
for i in range(3):
    answer = int(input("Enter a number\n"))
    nums.append(answer)
delnum = input("Are you sure you want to save the last number? (y/n(\n")
if delnum == "n":
    nums.remove(answer)
for i in nums:
    print(i)