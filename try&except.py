try:
    value = 10/0 #ZeroDivisionError

    number = int(input("Enter a number: ")) #ValueError if put string
    print(number)

except ZeroDivisionError as err:
    print(err) #print specific error [Division by zero]
except ValueError:
    print("Invalid Input")