# my_dictionary = {'bmw': 'x6', 'ford': 'fusion', (1,2): [1, 2, 3]}
#
# # print(my_dictionary['bmw'])
# # print(my_dictionary[(1, 2)])
# # print(f' Dictionary keys {my_dictionary.keys()}')
# # print(f' Dictionary values {my_dictionary.values()}')
# # print(f' Dictionary value with get {my_dictionary.get("ford")}')
# # print(f' Dictionary value with get {my_dictionary.get("eraz", "no product")}')
#
# for value in my_dictionary.values():
#     print(value)
#
# for key, value in my_dictionary.items():
#     print('key is: {} value is: {}'.format(key,value))
#
# new_dict = {}
# new_dict['name_count'] = 0
# print(new_dict)
# new_dict['name_count'] = 1
# print(new_dict)
#
first = {'name1': 'banana', 'name2': 'popok', 'name3': 'cream'}
second ={'name2': 'apple', 'name4': 'orange'}
second.update(first)
print(second)
#
# for key in second:
#     first[key] = second[key]
# print(first)
# first = {'name1': 'banana', 'name2': 'popok', 'name3': 'cream'}
# second ={'name2': 'apple', 'name4': 'orange'}
# for key in second:
#     if key not in first.keys():
#         first[key] = second[key]
# print(f'first after{first}')
#
# fruit_basket = {0: 'pineapple', 1: 'banana', 2: 'apple', 3: 'orange'}
#
# fruit_basket = dict(zero='pineapple', one='banana', second='apple')
#
# print(fruit_basket.pop(2), fruit_basket)
# print(fruit_basket.pop(2, False), fruit_basket)
# print(fruit_basket.popitem(), fruit_basket)

# new_set = set()
# new_set.add(1)
# new_set.add('grapes')
# new_set.add('pinepale')
# print(new_set)
#
# my_list = [1, 1, 1, 2, 4]
#
# without_duplicates = list(set(my_list))
# print(without_duplicates)
set_one = {1, 2, 3}
set_two = {4, 5, 3}
set_three = {3}

print(set_one.difference_update(set_two, set_three))
print(set_one)
print(set_one.isdisjoint(set_three))
print(set_one.issubset(set_three))
print(sorted(list(set_two), reverse=True)[1])
