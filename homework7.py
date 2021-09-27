# First point of First task for 7th lesson.
list_ = [1, 1, 13]
print(f"First List: {list_}")
list_2 = ['true', 'false', 'true']
print(list_2)

def remove_duplicates(duplicates):
	for i in duplicates:
		if list(set(duplicates)):
			duplicates.remove(list[i])
	return duplicates

print(f"Second List: {remove_duplicates(list_) }")
print(f"Second List_2: {remove_duplicates(list_2) }")

print("-"*100)
# Second point of First task for 7th lesson.

first_list = [1, 1, 2, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(f"First List: {first_list}")

second_list = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(f"Second List: {second_list}")

new_list = []

def common_elements(new_value):
	for i in second_list:
	    if i in first_list:
	        if i in new_value:
	            new_value.remove(i)
	        else:
	            new_value.append(i)
	return new_value

print(f"Here is the new list with common elements without duplicates {common_elements(new_list)}")

print("-"*100)
# Second task for 7th lesson.
list_3 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(f"List with all elements: {list_3}")

new_list3 = []

def divisors(new_value):
	for i in list_3:
		if i % 5 == 0:
			new_value.append(i)
	return new_value

print(f"New list with only divisors of 5: {divisors(new_list3)}")

print("-"*100)
# Third task for 7th lesson.
sentence = input("Enter a sentence.\n\t")

def split_function(fake):
	fake = sentence.split()
	fake = fake[::-1]
	string = " "

	return string.join(fake)

print(f"Same string just in backwords: {split_function(sentence)}")

print("-" * 100)
# Fourth task for 7th lesson.
original_tuple = (1, 'asd', 'sjh')
print(f"Original tuple: {original_tuple}")

def reverse_tuple(fake_tuple):
	another_fake_tuple = fake_tuple[::-1]
	return another_fake_tuple

print(f"Reversed tuple: {reverse_tuple(original_tuple)}")
# Fifth task for 7th lesson.
another_list = [13, 24, 61, 9, 2, 133, 4, 3, 9, 0, 15, 20]
print(f"The List before sorting: {another_list}")

sorted_list = []
def sorting_function(fake_list):
	while another_list:
		minimum = another_list[0]
		for i in another_list:
			if i < minimum:
				minimum = i
		fake_list.append(minimum)
		another_list.remove(minimum)
	return fake_list

print(f"The sorted List: {sorting_function(sorted_list)}")

print("-"*100)
# Sixth task for 7th lesson.
another_list_for_second_max = [13, 24, 61, 9, 2, 133, 4, 3, 9, 0, 15, 20]
print(f"The List: {another_list_for_second_max}")

second_maximum = []

def second_largest_value(fake_list):
	second_max = another_list_for_second_max[0]
	maximum = another_list_for_second_max[0]
	for i in another_list_for_second_max:
		if i > maximum:
			maximum = i

	for i in another_list_for_second_max:
		if i > second_max and i != maximum:
			second_max = i

	return second_max

print(f"Second Largest Value: {second_largest_value(second_maximum)}")

# In case, I see everything like in four pieces, I hope I've done everything right. Thank You. Good Night.