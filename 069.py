country = ["Korea","Japan","China","France","England"]
for i in country:
    print(i)
enter = input("Please enter any of these countries\n")
for i in country:
    if i == enter:
        print(country.index(enter))