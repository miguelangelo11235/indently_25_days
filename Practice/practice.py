set_1 : set[int] = {1, 2, 3, 4}
set_2 : set[int] = {4, 5, 6, 7}
set_1.add(5)
set_1.remove(1)
# print(set_1.union(set_2))
# print(set_1.intersection(set_2))
# print(set_1.difference(set_2))
# print(set_1.symmetric_difference(set_2))

# fs: frozenset[int] = frozenset({1, 2, 3})

people: dict[str, str | int] = {"name": "John", "age": 18}
# print(people)
# people["name"] = "Bob"
# print(people)

# del people["name"]
# people.pop("name")
# print(people)

dict_1: dict[str, int] = {"mike": 34, "leonard": 25}
dict_2: dict[str, int] = {"louise": 30, "kate": 22}
dict_3: dict[str, int] = dict_1 | dict_2
# print(dict_3)

# print(set_1)
# set_1 |= set_2
# print(set_1)

x = 20
print(not (10 > x > 0) )