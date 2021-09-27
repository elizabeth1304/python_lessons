# my_tupple = (1, "text", True, 1)
# my_tupple_2 = 1, "text", True, 1
# single_tuple = (1,)

# print(type(my_tupple))
# print(len(my_tupple_2))

# for item in my_tupple:
#   print(item)

# print('text' in my_tupple)

# text = 'text'
# new_tuple = tuple(text)
# print(new_tuple)
# print(my_tupple_2.count(1))
# print(my_tupple_2.index(1, 1))
# # del my_tupple

# new_str = ""
# for i in new_tuple:
#   new_str += i    
# print(new_str)

# def tuple_to_string(my_tupple: tuple) -> str:
#   new_str = ""

#   for i in new_tuple:
#       new_str += i 

#   return new_str

# print(tuple_to_string(new_tuple))

# print(''.join(new_tuple))


# new_tuple = (1, "fdfv")
# second_tuple = (1, 3)
# result = new_tuple + second_tuple
# print(result)

# my_list = [1, 2, 3, 4, 5, "asad", True, 1.2]

# def list_function(my_list):
# 	sum_ = 0
# 	for x in my_list:
# 		if type(x) == int or type(x) == float:
# 			sum_ += x 

# 	return sum_

# print(list_function(my_list))

# my_list = []
# print(id(my_list))

# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.append(4)
# my_list.append(5)
# my_list.append(6)
# my_list.append(7)
# my_list.append(8)
# my_list.append(10)

# print(my_list, id(my_list))

# my_list.insert(1, 4)

# print(my_list)

# my_list.remove(5)

# print(my_list)

# my_list.pop()

# print(my_list)

# del my_list[1:6]

# print(my_list)

# my_list.clear()

# print(my_list)
# from copy import deepcopy

# my_list = [(1, [5, 6])]

# print(my_list[0])
# print(my_list[0][1])
# print(my_list[0][1][1])

# sample_list = [[4,5], 4, "name"]
# sample_list_2 = sample_list
# sample_list.append(5)
# print(sample_list_2 is sample_list)

# sample_list_3 = sample_list.copy()
# sample_list.append(9)
# print(sample_list_3)
# print(sample_list_2)
# print(sample_list_2 is sample_list)

# sample_list[0].append('wonder')
# print(sample_list, sample_list_3)

# sample_list_4 =deepcopy(sample_list)
# sample_list.clear()
# print(sample_list, sample_list_4)

# sample_list =[[4, 5], 5, "name"]

# sample_list.append([4, 5])
# sample_list.extend([4, 5])

# print(sample_list)


import random

check_to_play = True
rounds = 0
computer_score = 0
user_score = 0
while check_to_play:
	# write the game
	user_choice = "test"
	# validation of input
	while user_choice not in ('1', '2', '3'):
		user_choice = input('1 for Rock 2 for Paper 3 for Scissors\n')
	else:
		user_choice = int(user_choice)

	# computer choice
	computer_choice = random.randint(1, 3)

	if computer_choice == user_choice:
		print("Draw")
	elif (computer_choice == 1 and user_choice ==2) or (computer_choice == 2 and user_choice == 3) or (computer_choice == 3 and user_choice == 1):
		print("You won!")
		user_score += 1
	else:
		print("You lost.")
		computer_score += 1
	rounds += 1
	check_input = input("Wanna play?")
	if check_input == "no":
		check_to_play = False

print(f"user score - {user_score} and computer score - {computer_score} total score - {rounds}")