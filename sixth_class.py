# full_name = input("Tell me the name.\n\t")

# def happy_birthday(name):
# 	text = f"Happy Birthday {name}!!!"
	
# 	return text

# greeting = happy_birthday(full_name)

# print(greeting)

# second_name = input("Tell the name.\n\t")
# print(happy_birthday(second_name))



# def is_even(num):
# 	if num % 2 == 0:
# 		return True
# 	else:
# 		return False

# print(is_even(2))

# def print_is_even(num, text, end_="\t"):
# 	print(text)
# 	print(num % 2 == 0, end=end_)


# print_is_even(5, "smth", "\n")

# print("dfdfg")


# num = 5

# def id_odd():
# 	global num
# 	num = 4
# 	print(num % 2 == 1)

# id_odd()

# print(num)
# def print_is_even(num, end_="\t"):
# 	"""
# 	Takes two args and prints true if num is given else prints false. 
# 	You can pass end arg for print() fun.
# 	param_num: int
# 	param_end: str
# 	return None
# 	"""
# 	print(num % 2 == 0, end=end_)

# print(print_is_even)
# print(help(print_is_even))


from random import randint
for i in range(10):
	number = randint(4, 10)
	print(number)
