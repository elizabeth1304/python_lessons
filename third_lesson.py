# import sys
# word = "hello python indees"

# word_ = "t" + "e" + "x" + "t" + " "
# negative_idx_of_first_el = len(word) * (-1)
# print(len(word))
# print(word[negative_idx_of_first_el])

# new_text = word[::-1]
# print(new_text)

# word =  "Armenia"

# print(word.index("meni"))
# print(word.find("Arm"))
# print(word.endswith("e"))

# year = input("Enter the year: ")

# if year.isdigit():
# 	year = int(year)
# else:
# 	print("Wrong vallue.")
# 	sys.exit

# if (year % 4) == 0:
#    if (year % 100) == 0:
#        if (year % 400) == 0:
#            print(year, "is a leap year.")
#        else:
#            print(year, "is not a leap year.")
#    else:
#        print(year, "is a leap year.")
# else:
#    print(year, "is not a leap year.")	
# print(word.isalpha())
# print(word.isdigit())

# sentence = "Erevan is the capital of Armenia"
# new_string = sentence.replace("Erevan", "Yerevan")

# print(new_string)

# name = input("Input name: \n")
# age = input("Input age: \n")


# text = "Hello I'm {} I'm {} years old".format(name, age)
# text = "Hello I'm {0} I'm {1} years old".format(name, age)
# text = "Hello I'm {name_user} I'm {age_user} years old".format(name_user=name, age_user=age)
# text_ = f"Hello I'm {name} I'm {age} years old"
# print(text_)

# my_range = range(5)
# # print(my_range)

# name = "John"
# i = "hello"
# for i in my_range:
# 	print(f"hello {name}")
# print(i)

my_number = input("Input number: ")

for num in range(1, my_number):
	if num % 15 == 0:
		print("FizzBuzz")
	elif num % 5 == 0:
		print("Buzz")
	elif num % 3 == 0:
		print("Fizz")
	else:
		print(num)

