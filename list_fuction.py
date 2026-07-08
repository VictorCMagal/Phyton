lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin","Karen","Jim","Oscar","Toby","Toby"]
#INDEX :      0       1      2...

#Add another element to the list
friends.append("Creed")

#Add 2x list thogeda
#friends.extend(lucky_numbers) 

print(friends)
print("\n")

#Add after index [1]
print("--INSERT AFTER 1 ------------------\n")
friends.insert(1, "Inserty") 

print(friends)
print("\n")

#Remove "Jim"
friends.remove("Jim") 

print(friends)
print("\n")

#friends.clear() # Drop DB

# Remove the last of the list
friends.pop() 

print(friends)
print("\n")

# Show the "Oscar"'s Index Number
print(friends.index("Oscar")) 
print("\n")

# Count how many "Toby"s
print(friends.count("Toby")) 
print("\n")

# ----- ORDER --------------------------
print("---------------------------------\n")

# Sort the list with ascendent order
friends.sort() 

print(friends)
print("\n")

# Sort the list with reserse order
lucky_numbers.reverse() 

print(lucky_numbers)
print("\n")

# ----- COPY LIST ---------------------------
print("--COPY--------------------------\n")

friends2 = friends.copy()

print("FRIENDS: "+str(friends))
print("FRIENDS COPY: "+str(friends2))

print("\n")

      