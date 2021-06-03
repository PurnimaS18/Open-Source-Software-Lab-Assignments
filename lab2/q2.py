#Write a function “duplicate” to find all duplicates in the list.
some_list=[1, 2, 3, 4, 5, 6, 1, 2, 3]
my_list=sorted(some_list)
duplicates=[]
for i in my_list:

    if my_list.count(i)>1:

        if i not in duplicates:

            duplicates.append(i)

print(*duplicates)