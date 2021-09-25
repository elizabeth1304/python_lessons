# First exercise for Fourth lesson. Remember that you're not dumb Elizabeth. Thank you.
word = input("Enter a word: ")

if len(word) > 2:
	if word[-3:] == "ing":
		print(word + "ly")
	else:
		print(word + "ing")
else:
	print(word)

# Second exercise for Fourth lesson. 
sentence = input("Write a sentence. /it'll be cool if you use words 'not' or 'poor' or 'not' and 'poor' together, thank you/\n\t")

word_not = sentence.find('not')
word_poor = sentence.find('poor')

if word_poor > word_not and word_not>0 and word_poor>0:
    new_sentence = sentence.replace(sentence[word_not:(word_poor+4)], 'good')
    print(new_sentence)
else:
     print(sentence)

# Yes, I'm not dumb at all. Proud of me.

# Third exercise for Fourth lesson. Just a lil bit more and I can say you're the best.
vocable = input("Enter a word: ")
new_vocable = vocable[0] 
vocable = vocable.replace(new_vocable, "$")
vocable = new_vocable + vocable[1:]
print(vocable)

# Vocable means word, I've already used that word that's why we start learning another english words.

# Fourth exercise for Fourth lesson.
preposition = input("Write a sentence. /it'll be great if you enter number too/\n\t")
letters = 0
digits = 0
other = 0
for i in preposition:
    if i.isalpha():
	    letters += 1
    elif i.isdigit():
        digits += 1
    else:
        other += 1

print("The length of the string will be: ", letters + digits + other)

# I can't understand the difference between this 2.
copy_preposition = input("Write a sentence. /it'll be great if you enter number too/\n\t")
print(len(copy_preposition))

# And the question is what is the difference? Thank you.
# And yeah about the word 'preposition': the same shit as vocable.

# Fifth exercise for Fourth lesson. The last one.
another_sentence = input("Write a sentence.\n\t")
for i in range(len(another_sentence)):
	if i % 2 == 0:
		print(another_sentence[i], end='')

# Goolge has no another word for me. 

# That's all. Thank you, have a nice day.