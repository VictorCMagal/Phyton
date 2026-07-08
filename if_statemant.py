is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
elif is_male and not(is_tall): #else if
    print("You are a short male")
elif not(is_male) and is_tall: #else if
    print("You are a short male")
else:
    print("You are not male and not tall")