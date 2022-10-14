
rain = input("Is it raining now?")
rain = str.lower(rain)
if rain == "yes":
    windy = input("Is it windy now?")
    windy = str.lower(windy)
    if windy == "yes":
        print("It is too windy for an umbrella")
    else:
        print("take an umbrella")
else:
    print("Enjoy your day")