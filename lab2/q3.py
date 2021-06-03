#Write a function group (list, size) that take a list and splits into smaller lists of given size.
my_list = ['have', 'a', 'nice', 'day', 'people', 'and', 'keep', 'going', 'because', 'you', 'have', 'no', 'option']
def divide_chunks(l, n):
    for i in range(0, len(l), n): 
        yield l[i:i + n]
  


n = int(input())
x = list(divide_chunks(my_list, n))
print (x)