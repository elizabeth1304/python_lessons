# list_1 = []
# for i in range(11):
#     list_1.append(i)

# list_1 = [i for i in range(11) if i % 2 ==0]
# list_1 = [[j for j in range(10)] for i in range(11)]
# print(f"List values are: {list_1}")

# a = int(input("Tell number and see the half.\n"))
# half_number = a / 2 if a % 2 == 0 else a // 2
# print(f"the half of {a} is {half_number}")

# list_1 = [i if i == 0 else i*i for i in range(11) if i % 2 ==0]
# print(f"List values are: {list_1}")

# dict_1 = {key:key if key ==0 else key*key for key in range(11) if key % 2 == 0}
# print(dict_1)

import sys
#
# gen_1000 = (i if i == 0 else i*i for i in range(5))
# list_1000 = [i if i == 0 else i*i for i in range(5)]
# print(f"generator: {sys.getsizeof(gen_1000)},\n list: {sys.getsizeof(list_1000)}")
# try:
#     print(next(gen_1000))
#     print(next(gen_1000))
#     print(next(gen_1000))
#     print(next(gen_1000))
#     print(next(gen_1000))
#     print(next(gen_1000))
# except StopIteration:
#     print("Generator is exhausted!")
#     gen_1000.throw(ValueError)
#
# gen_1000 = (i if i == 0 else i*i for i in range(5))
# print(next(gen_1000))
# gen_1000.close()
# # gen_1000.throw(ValueError)
# print(next(gen_1000))

# word = input("Tell a word and see it in uppercase: ")
# gen_upper = (letter for letter in word if letter.isupper())
# # for item in gen_upper:
# #     print(item)
#
# print(next(gen_upper))
#
# list_2 = list(gen_upper)
# print(list_2)
#
# def my_generator():
#     print(10)
#     yield
#     print(20)
#     yield
#     print(30)
#     yield

# def my_generator():
#     yield 10
#     yield 20
#     yield 30

# first_one = my_generator()
# print(first_one)
# print(next(first_one))
# print(next(first_one))
# print("Here can be bunch of code:")
# print(next(first_one))
#
# g_1 = (i for i in range(10))
#
# def my_generator(end, start=0, step=1):
#     for ele in range(start, end, step):
#         yield ele
#
# g_2 = my_generator(5)
# g_3 = my_generator(start=10, end=0, step=-1)
#
# print(next(g_2))
# print(next(g_2))
# print(next(g_3))

def my_generator():
    i = 0
    b = 1
    while True:
        check = yield i
        i, b = b, i + b
        if check == 'restart':
            i = 0
            b = 1

# gen_4 = my_generator()
# print(next(gen_4))
# print(next(gen_4))
# print(next(gen_4))
# print(next(gen_4))
# print(next(gen_4))
# print(next(gen_4))

fibo = my_generator()
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(fibo.send('restart'))
print(next(fibo))

# import random
#
# def random_char():
#     while True:
#         order = random.randint(67, 96)
#         yield chr(order)
#
# rand_char = random_char()
# i = 0
# for j in rand_char:
#     print(j)
#     if i >= 5:
#         break
#     i += 1
