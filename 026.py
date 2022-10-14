word = input("Enter a word: ")
woldlength = len(word)
word = word.lower()
firstword = word[0:1]
if firstword == "o"or firstword == "a" or firstword == "e" or firstword == "i" or firstword == "u":
    answer = word+"way"
    print(answer)
else:
    notword = word[1:woldlength]
    answer2 = notword+firstword+"ay"
    print(answer2)