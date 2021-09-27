# I'm not in the mood today, that's why we won't have commets.

# It's not the homework, just from slide. 
# First one.
# sum_ = 0
# for i in range(1,21):
# 	if i !=  3 and i != 13:
# 		sum_ += i
# print(sum_)

# Second one.
# add = 0
# for j in range(1,20):
# 	add += j
# 	if j == 15:
# 		break
# print(add)

# And they're commented because I'm very lazy person today and I don't wanna find new variable names. Sorry for that.

# Okay, let's start the HOMEWORK. I hope I'll finish it today.
# First exercise for Fifth lesson.
# for i in range(0, 5):
# 	for j in range(0,i):
# 		print("*", end=" ")
# 	print("")

# for i in range(5, 0, -1):
# 	for j in range(i):
# 		print("*", end=" ")
# 	print("")


num = input("Tell hight of the pyramid: ")

if num.isdigit():
	num=int(num)
else:
	sys.exit()

num = num + 1  if num % 2 ==0 else num

mid_row = num // 2 + 1
for i in range(1, num + 1):
	if i < mid_row:
		print(i * "* ")
	else:
		j = mid_row * 2 - i
		print(j * "* ")

# Second exercise for Fifth lesson.
sum_ = 0
previous = 1

for x in range(1,11):
	if x == 1:
		 previous = 1
	else:
		previous =  x-1
	sum_ = previous + x
		
	print(f"{previous} + {x} = {sum_}")

# The important fact is that my problem was solved no matter how.

# Third exercise for Fifth lesson.
number = input("Enter a number and see all the divisors of that number.\n\t Number: ")

if number.isdigit():
	number = int(number)

for index in range(1,number+1):
	if number % index == 0:
		print(index)

# Fourth exercise for Fifth lesson.
factorial_number = input("Enter a number and see all the factorial of that number.\n\t Number: ")
factorial = 1
if factorial_number.isdigit():
	factorial_number = int(factorial_number)
for n in range(1,factorial_number+1):
	factorial = factorial * n
print(f"The factorial of {factorial_number} is {factorial}.")

# Fifth exercise for Fifth lesson. 
number1, number2 = 0, 1

while number2 <= 50:
    print(number2, end=" ")
    number1, number2 = number2, number1 + number2

# That's all. Have a great day.