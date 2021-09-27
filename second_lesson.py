# import variables 

# from variables import current_year_of_21_th as year, month, day
# if you want all variables just put *

# print("Today is", year, month, day)

# from datetime import datetime
# import time
# current_time = datetime.now()
# print(current_time)
# time.sleep(1)
# print("Today is", current_time.year, current_time.month, current_time.day)
# current_time2 = datetime.now()
# print(current_time2)

# from datetime import datetime
# import time
# current_time = datetime.now()
# per_yer = input("How years old are you?\n\t")
# minus1 = 100 - int(per_yer)
# age = current_time.year + minus1 

# print("You will be 100 years old in ", age)

# num = int(input("tell the number?\n\t"))
# bool_var = num < 10 and num < 15
# bool_var2 = num < 10 or num < 15

# print("for fist comparison ", bool_var)
# print("for second comparison ", bool_var2)

# word = "hello"

# print(word * 0)
# print("h" in word)

# a = 0
# if a > 0:
# 	print("A is positive.")
# elif a == 0:
# 	print("A is equal to zero.")
# else:
# 	print("A is negative.")

# question = input("What's the weather today?\n\t")

# if question == "rainy":
# 	question2 = input("Is it raining hard or not?\n\t")
# 	if question2 == "yes":
# 		print("Stay at home!")
# 	else:
# 	    print("Take an umbrella.")
# elif question == "shiny":
# 	question3 = int(input("what's the tempreature?\n\t"))
# 	if question3 > 40:
# 		print("Stay at home!")
# 	else:
# 		print("It's shinny have a nice day.")

choice = int(input("Hello the menu is 1 for kebab(1000), 2 for Pizza(3000) what you want?\n\t"))
choice2 = int(input("mayonez(50) or ketchup(100) 1 or 2\n\t"))
pizza_price = 3000
kebab_price = 1000
mayo_price = 50
ketchup_price = 100

print(("You ordered pizza with mayonez " + str(pizza_price + mayo_price)) * (choice == 2 and choice2 == 1), end="")
print(("You ordered pizza with ketchup " + str(pizza_price + ketchup_price)) * ( choice == 2 and choice2 == 2), end="")
print(("You ordered kebab with mayonez " + str(ketchup_price + mayo_price)) * (choice == 1 and choice2 == 1), end="")
print(("You ordered kebab with ketchup " + str(ketchup_price + ketchup_price)) * ( choice == 1 and choice2 == 2), end="")

