# Python Program to Print X Star Pattern
 
rows = int(input("Enter X  Rows = "))

print("X Star ") 

for i in range(0, rows):
    for j in range(0, rows):
        if(i == j or j == rows - 1 - i):
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
