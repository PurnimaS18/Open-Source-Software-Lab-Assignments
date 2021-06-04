#Write a program to count frequency of characters in a paragraph.
test_str = "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking."

all_freq = {}

for i in test_str:
	if i in all_freq:
		all_freq[i] += 1
	else:
		all_freq[i] = 1

print ("Count of all characters  :\n "+ str(all_freq))
