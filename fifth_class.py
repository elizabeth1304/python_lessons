# a = int(input("Tell the number and get the multiple "))

# for i in range(1,11):
# 	print("{} * {} = {}".format(a, i, a*i))


# import sys 

# number = input("Tell the number and see the multipication tale of it: ")

# if number.isdigit():
# 	number = int(number)
# else:
# 	sys.exit()

# for i in range(1, number+1):
# 	for j in range(1,11):
# 		print(f"{i} * {j} = {i * j}")
# 	print("-"*100)


# import sys 

# number = input("Tell the year and see the sum of the digits: ")

# sum_ = 0 

# for i in number:
# 	sum_+=int(i)
# print(sum_)

# sentence = input("Enter a sentece with numbers.\n\t")

# sum_ = 0 

# for i in sentence:
# 	if i.isdigit():
# 		sum_ +=int(i)
# 	else:
# 		continue
# print(sum_)

# sentence = input("Enter a sentece with numbers.\n\t")

# multiple_ = 1 

# for i in sentence:
# 	if i == "0":	
# 		print("I found zero.")
# 		break		
# 	elif  i.isdigit():
# 		multiple_ *=int(i)
# 	else:
# 		continue
# print(multiple_)

# count_ = 0

# while count_< 5:
# 	print("Count < 5")
# 	count_ += 1

# count_ = 0

# while True:
# 	print("Count < 5")
# 	count_ += 1
# 	if count_ == 5:
# 		break
# text = input("Tell smth and see the sum.\n\t")

# idx = 0
# count_ = 0

# while idx < len(text):
# 	letter = text[idx]
# 	count_ += int(letter)
# 	idx += 1

# print(count_)

# text = input("Tell smth and see the sum.\n\t")

# idx = 0
# count_ = 1

# while idx < len(text):
# 	letter = text[idx]
# 	if letter == '0':
# 		count_ = 1
# 		break
# 		# idx += 1
# 		# continue
# 	count_ *= int(letter)
# 	idx += 1
# else:
# 	print(f"it worked without zeros")

# print(count_)
	

# password = input("password: ")
# while len(password) < 8:
# 	password = input("try again: ")
# print("Everything is done.")

password_check = True

while password_check:
	password = input("Enter password: ")
	password_check = len(password) < 8

