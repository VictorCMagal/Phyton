
'''
import os
from pathlib import Path

print(Path(__file__).resolve())
print(Path(__file__).parent)

arquivo = Path(__file__).parent / "employees.txt"

print("Existe?", arquivo.exists())
print("Caminho:", arquivo)

print("Diretório atual (cwd):", os.getcwd())
print("Pasta do script:", Path(__file__).parent)
print("Arquivo existe no cwd?", Path("employees.txt").exists())
print("Arquivo existe na pasta do script?", (Path(__file__).parent / "employees.txt").exists())
'''

employee_file = open("employees.txt","r") # "r" = read only // "w" = write only // "a" = add new info (at end) // "r+" = read & write

print(employee_file.readable())

#print(employee_file.read()) # Read all archive

#print(employee_file.readline())

#print(employee_file.readlines())

for employee in employee_file.readlines():
    print(employee)

employee_file.close()