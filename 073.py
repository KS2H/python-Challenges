food = {"라면":1,"볶음밥":2,"햄버거":3,"피자":4}
for key , value in food.items():
    print(key, value)
fooddel = input("삭제할 음식의 이름은 무엇인가요")
food.pop(fooddel)
for key , value in food.items():
    print(key, value)