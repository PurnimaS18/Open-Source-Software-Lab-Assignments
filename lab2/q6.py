#Use Python Built-in Functions ‘open’, ‘read’, ‘’readline, ‘write’,’writeline’ to work with files.
new_file = open("theory.txt", 'w')
new_file.write("Be happy\n")
new_file.writelines(["Again Be Happy\n", "Beee happy\n", "Smileeeee"])
new_file.close()
new_file = open("theory.txt", 'r')
print(new_file.readline())
print(new_file.read())
new_file.close()