import os
import collections

# print(__file__)
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.join(base_dir, 'templates'))
# print('Monty Python'.rstrip('on'))
# s = [('Japanese', 1), ('Cheinese', 2), ('American', 3), ('French', 4), ('Betonam', 1)]
data = collections.defaultdict(int)
# for k, v in s:
#     data[k].append(v)


test = "hello world"
print(test.title())


# data["test1"] += 1

# data["test2"] += 1

# print(data)
dict = {}
dict["test1"] += 1
dict["test2"] += 1
print(dict)
