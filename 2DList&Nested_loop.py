number_grid = [
    [1,2,3],#row 0
    [4,5,6],#row 1
    [7,8,9],#row 2
    [0]
#cln:0,1,2
]

# print position at row[2] and cln[1] = 8
print(number_grid[2][1])

# print rows
for row in number_grid:
    print(row)

# print all info
for row in number_grid:
    for cln in row:
        print(cln)