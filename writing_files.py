employee_file = open("employees.txt","w") # "r" = read only // "w" = write only // "a" = add new info (at end) // "r+" = read & write
#print(employee_file.read())

employee_file.write("\nToby - Human Resources")
employee_file.close()