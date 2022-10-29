subject = ["국어","수학","영어","체육","사회","과학"]
for i in subject:
    print(i)
print("이 과목중에서 좋아하지 않는 과목 하나를 쓰세요")
guess = int(input("ex)146 국어 1 수학 2 영어 3 체육 4 사회 5 과학 6\n"))
guess = guess-1
del subject[guess]
for i in subject:
    print(i) 