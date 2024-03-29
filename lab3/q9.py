#Write a function ‘nearly_equal’ to test whether two strings are nearly equal. Two strings
#‘a’ and ‘b’ are nearly equal when ‘a’ can be generated by a single mutation on ‘b’.
def mutate(word):
    return {
        value
        for i in range(len(word))
        for letter in 'abcdefghijklmnopqrstuvwxyz'
        for value in [
        word[:i] + word[i + 1:],          # remove
        word[:i] + letter + word[i:],     # insert
        word[:i] + letter + word[i + 1:], # replace
        word[:i] + word[i + 1: i + 2] + word[i:i + 1] + word[i + 2:]
        ]
    }

def nearly_equal(a, b):
    return False if abs(len(a) - len(b)) > 1 else b in mutate(a)

p = nearly_equal('ab', 'bc')
if(p == True):
    print("YES")
else:
    print("NO")