# If Else
user_input = 19
if user_input <= 18:
    print("Underage")
else:
    print("Allowed")

# If Elif
user_input = 19
if user_input <= 18:
    print("Underage")
elif user_input >= 18:
    print("Allowed")

# If Elif Else
user_input = 19
if user_input <= 18:
    print("Underage")
elif user_input >= 18:
    print("Allowed")
else:
    print("Erorr!")

# Match Case
print("1. Home\n2. About\n3. Contact")
user_input = 3
match user_input:
    case 1:
        print("Home")
    case 2:
        print("About")
    case 3:
        print("Contact")