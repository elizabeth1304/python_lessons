# First task for 6th lesson. I didn't ask any question about this task, don't forget.
base = input("How do you work out the area of a triangle? It's so simple, just enter the base and the height of triangle.\n\tThe Base: ")
height = input("\tThe Height: ")

if base.isdigit():
	base = int(base)
else:
	sys.exit()

if height.isdigit():
	height = int(height)
else:
	sys.exit()

def area_of_triangle(a:int, h:int) -> int:
	"""
	Takes two args and returns the values of the parameters.
 	param_a: int
 	param_h: int
 	return int
 	"""
	area = 1/2 * a * h

	return area

print(f"The area of triandle will be {area_of_triangle(base, height)}.")

# And definitely I know how to calculate the area of ​​a triangle.

# Second task for 6th lesoon.
reversed_text = input("Write a text to reverse.\n\t")

def reverse_function(sentence):
 	text = ""
 	for i in sentence:
 		text = i + text

 	return text


print(f"The reversed text will be: {reverse_function(reversed_text)}.")

# Third task for 6th lesson.
preposition = input("Enter  a sentence and see how many upper case and lower case letters are in your sentence.\n\t")

def uppercase_lowercase_function(sentence):
	text = {"Upper case letters":0, "Lower case letters":0}
	for i in sentence:
		if i.isupper():
			text["Upper case letters"] += 1
		else:
			text["Lower case letters"] += 1

	return text

print(uppercase_lowercase_function(preposition))


# Fourth task for 6th lesson.
def isPalindrome(word):
	first = 0
	last = len(word) - 1
 
	while last >= first:
		if not word[first] == word[last]:
			return False
		first += 1
		last -= 1
	return True

print(isPalindrome('madam')) 

# Fifth task for 6th lesson.
import random

the_word = input("Enter a word rock, paper or scissors: ")
can_be = ["rock", "paper", "scissors"]
random_choice = random.choice(can_be)

print(f"\nYou choose {the_word}, computer choose {random_choice}.\n")

if the_word == random_choice:
    print(f"Both of you selected {the_word}. It's a tie!")
elif the_word == "rock":
    if random_choice == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif the_word == "paper":
    if random_choice == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif the_word == "scissors":
    if random_choice == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

# I think that for this task we didn't need function.

# That's all. Good night.	
