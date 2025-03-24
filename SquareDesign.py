#Solid Square
n = 4

for i in range(n):
    print("*" * n)

# Right-Angled Triangle

n = 5

for i in range(1, n+1):
    print("*" * i)

#Inverted Right-Angled Triangle

n = 5

for i in range(n , 0 , -1):
    print("*" * i)

#Hollow Square
n = 6

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end = " ")
        else:
            print(" ", end=" ")
    print()