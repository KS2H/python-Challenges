password1 = input("Set your password")
password2 = input("enter a again password")
if password1 == password2:
    print("Thank you")
elif password1.lower() == password2.lower():
    print("They must be in the same case")
else:
    print("Incorrect")