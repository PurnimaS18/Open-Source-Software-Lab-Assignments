#Provide an implementation for map using list comprehensions.
def cube(n):
    return n*n*n

ls = [int(i) for i in range(1, 10)]


newls = list(map(cube, ls))
print(newls)
