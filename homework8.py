# First task for 8th lesson.
# Wait for it maybe I'll get smarter at night and do this thousand-line program.

# Second task for 8th lesson.
sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print(f'First list without changes: {sample_list}')
sample_list.sort()

def duplicates(fake_list):
    fake_list = []
    for i in sample_list:
        if i not in fake_list:
            fake_list.append(i)
    return fake_list


print(f'New list: {duplicates(sample_list)}')

print('-'*100)
# Third task for 8th lesson.
original_list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
print(f'First list without changes: {original_list}')

def flatten_list(fake_list):
    new_list = []
    for item in fake_list:
        if type(item) is list:
            for i in item:
                new_list.append(i)
        else:
            new_list.append(item)
    return new_list

print(f"Flatten list: {flatten_list(original_list)}")

print('-'*100)
# Fourth task for 8th lesson.
original_list_2 = [1, 1, 2, 3, 4, 4, 5, 1]
print(f'First list without changes: {original_list_2}')
#I have the most creative teacher that's why the name of my list will be original_list_2)))

def split_list(fake_list, len):
    return fake_list[:len], fake_list[len:]

first_list_length = 3

print(f"Length of the first part of the list: {first_list_length}")
print(f"Splited the said list into two parts: {split_list(original_list_2, first_list_length)}")

print('-'*100)

# Idk why, but my brain refuses to work today. Sorry for that.
# Have a fabulous day.


