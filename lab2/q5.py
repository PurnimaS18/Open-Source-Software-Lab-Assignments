#Write a function extsort to sort a list of files based on extension.
import os

def extsort(files):
    return sorted(files,key=lambda x: os.path.splitext(x)[1])
print (extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']))