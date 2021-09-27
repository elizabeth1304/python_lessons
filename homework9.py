# I lost my motivation but then I remembered about not being rich but just buying a Lamborghini that I want.
# And you won't believe but it comes back.
# Okay, let's start, I hope I'll do everything right.
# First task for Ninth lesson.
import sys

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}
dict4 = {6: 50, 7: 60}
print(
    f'First dictionary: {dict1}, \nSecond dictionary: {dict2},\nThird dictionary: {dict3},\nFourth dictionary: {dict4}.')

list_dict = [dict1, dict2, dict3, dict4]
for dict_ in list_dict:
    dict1.update(dict_)

print(dict1)


# def new_dictionaries(new_dict):
#     for i in (dict1, dict2, dict3):
#         new_dict.update(i)
#     return new_dict



print(f'New dictionary from first, second and third dictionaries: {new_dictionaries(list_dict)}.')

# In the example the expected result was {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} that's why I dont concatenate the dict4.

# There are two options here: either I wrote it wrong or it's easy. Hoping for second one.

# Second task for Ninth lesson.
new_dict = {}

n = input('Give a number for a range end: ')

if n.isdigit():
    n = int(n)
else:
    sys.exit()


def create_new_dict(new):
    for i in range(1, n + 1):
        value_ = 1
        value_ = i * i
        new[i] = value_
    return new


print(f'You gave {n} number and the range wil be 1 : {n}.\nHere is the new dictionary: {create_new_dict(new_dict)}.')

# Okay, here is another example for suspicion.

# Third task for Ninth lesson.
original_dictionary = {'c1': 'Red', 'c2': 'Green', 'c3': None, 'c4': None}
print(f'Original dictionary: {original_dictionary}.')

original_dictionary = {key:value for (key, value) in original_dictionary.items() if value is not None}
print(f'New dictionary without "None" items: {original_dictionary}')

# for key, value in a.copy().item():
#     if not value:
#         a.pop(key)
#
# print(a)

# Fourth task for Ninth lesson.
sentence = input("Write a sentence down below:\n\t")

words = []
words = sentence.lower().split()

the_newest_dict = {}

for key in words:
    the_newest_dict[key] = words.count(key)

print("Created dictionary with sentence words will be:  ",  the_newest_dict)

# That's all. Thank you, have a fabulous day.