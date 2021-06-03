#Write a function “lensort” to sort a list of strings based on length.
ls = ["Give", "me", "some", "sunshine", "Give", "me", "some", "rain"]

def lensort(ls):
    newls = sorted(ls, key = len)
    return newls


print(lensort(ls))