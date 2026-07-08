friends = ["Jim","Karen","Kevin"]

# -------------------------------------------

for letter in "Giraffe Academy":
    print(letter)

for buddys in friends:
    print(buddys)

for index in range(5):
    print(index)

for index in range(50,55):
    print(index)

for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("First Iteration!")
    else:    
        print(str(index)+" Not first")