phrase = "Giraffe Academy"
print(phrase + " is cool.")

print("Giraffe\"Academy\"")
print("Giraffe\nAcademy")

#lowercase
print(phrase.lower())
#uppercase
print(phrase.upper())

#Bolean
print(phrase.isupper())
print(phrase.upper().isupper())

#len function = conta quantas letras tem
print(len(phrase))

#pegar Letras
print(phrase[0]) # 0 = G

#index
print(phrase.index("G")) # G = 0
print(phrase.index("Acad")) # Acad = 8

#Replace
print(phrase.replace("Giraffe","Elephant"))