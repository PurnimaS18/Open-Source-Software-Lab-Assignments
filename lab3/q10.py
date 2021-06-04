#Write a program to find anagrams in a given list of words. Two words are called
#anagrams if one word can be formed by rearranging letters of another. For example
#‘eat’, ‘ate’ and ‘tea’ are anagrams.
def anagrams(words):
    helper = {}
    for item in words:
        tmp = list(item)
        tmp.sort()
        word = ''.join(tmp)
        if word in helper:
            helper[word].append(item)
        else:
            helper[word] = [item]
    r = []
    for key in helper.keys():
        r.append(helper[key])
    return r

ls = ["i", "am", "ma", "smart", "trams"]
print(anagrams(ls))