# Write a program to print each line of a file in reverse order.

file = open("theory.txt", 'r')
lines = file.readlines()

for line in lines:
    words = line.split()
    print(*words[::-1])