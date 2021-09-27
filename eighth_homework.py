# *ARGS

# def foo(*args):
# 	for a in args:
# 		a = a.upper()
# 		print(a)
# 	print(f"The type of args is {type(args)}")
# 	print(*args)
# foo("a", "b")

# def sum_elements(*elements):
# 	sum_ = 0
# 	for e in elements:
# 		sum_ += e

# 	return sum_

# print(sum_elements(1,2,3,4,5,6))

# name_tuple = ("Name1", "Name1", "Name1", "Name1", "Name1")

# print(*name_tuple, sep='\n')

# END

#ERROR HANDLING

# number = input("Tell me the number and see the half of it\n")

# try:
# 	number = int(number)
# except ValueError:
# 	print("This isn't a number so you get zero.")
# 	number = 0

# half = number / 2

# print(half)

# num_1 = input("Number to devide\n")

# try:
# 	num_1 = int(num_1)
# 	new_value = 4 / num_1
# except ZeroDivisionError:
# 	print("It's zero")
# except (ValueError, TypeError):
# 	print("its not a number")

# new_value = 4 / num_1

# print(new_value)

# password = input("Tell the password.\n\t")

# try:
# 	if len(password) < 8:
# 		raise ValueError("Password should contain at least 8 symbols.")

# 	check = True
# 	for i in password:
# 		if i.isalpha() and i.isupper():
# 			check = False
# 	if check:
# 		raise TypeError("Password should contain at least one uppercase character.")

# 	check_symbols = True
# 	for i in password:
# 		if not i.isalpha() and not i.isdigit() and i != " ":
# 			break
# 	else:
# 		raise TypeError("Password should contain at least one symbol.")
# except ValueError as error:
# 	print("Please provide larger password.")
# 	print(error)
# except TypeError as error:
# 	print(error)
# else:
# 	print("password is accepted")
# finally:
# 	print("Bye")


password = input("Tell the password.\n\t")

try:
	errors = []
	if len(password) < 8:
		errors.append(ValueError("Password should contain at least 8 symbols."))

	check = True
	for i in password:
		if i.isalpha() and i.isupper():
			check = False
	if check:
		errors.append(TypeError("Password should contain at least one uppercase character."))

	check_symbols = True
	for i in password:
		if not i.isalpha() and not i.isdigit() and i != " ":
			break
	else:
		errors.append(TypeError("Password should contain at least one symbol."))
	if errors:
		raise Exception("Wrong password")
except ValueError as error:
	print("Please provide larger password.")
	print(error)
except TypeError as error:
	print(error)
except Exception as error:
	for error in errors:
		print(error)
else:
	print("password is accepted")
finally:
	print("Bye")