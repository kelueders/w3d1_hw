# def sort_by_last(x):
#     return author[1]

# print(author.sort(key = sort_by_last))


# new = []

# def last_name(a):
#     for a in author:
#         new += new.append()
#         return a.split()[-1]
    
# print(last_name(author))

# # SPACE

# new = []

# for place in places:
#     temp = place[-1]
#     cel_to_far(temp)
#     new += new.append(temp)
# return new

# print(new)

# SPACE

my_dict = {
    "Ryan": 10,
    "Alex": 20,
    "Kate": 30
}

dict_map = list(map(lambda x: x + 5 if x < 15 else x, my_dict.values()))
print(dict_map)

dict_map2 = list(map(lambda x: my_dict[x] + 10, my_dict))
print(dict_map2)

dict_map3 = list(map(lambda x: (x, my_dict[x] + 5), my_dict))
print(dict_map3)

# SPACE

def add_two(x):
    return x + 2

print(add_two(4))

# lambda syntax
print((lambda x: x+2)(5))