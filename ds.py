# letters = ["a", "b", "c"]
# matrix = [[0, 1], [1, 1]]
# zeros = [0] * 5
# combined = zeros + letters
# print(combined)
# chars = list("Hello world")
# print(len(chars))
# numbers = list(range(10))
# print(numbers[::5])
# numbers = [1, 2, 3]
# first, second, third = numbers
# print(first)
# numbers = [1, 2, 3, 4, 5]
# first, second, * others = numbers
# print(first)
# print(others)
# letters = ["a", "b", "c"]
# for letter in enumerate(letters):
#     print(letter[0], letter[1])
# letters = ["a", "b", "c"]
# letters.append("d")
# print(letters)
# letters = ["a", "b", "c"]
# letters.insert(0, "-1")
# print(letters)
# letters = ["a", "b", "c"]
# letters.pop(0)
# letters.remove("b")
# del letters[0:2]
# print(letters)
# letters = ["a", "b", "c", "c"]
# print(letters.index("a"))
# print(letters.count("c"))
# numbers = [1, 3, 25, 7, 243]
# numbers.sort(reverse=True)
# print(numbers)
# items = [
#     ("product", 10),
#     ("product", 9),
#     ("product", 12),
# ]


# def sort_item(item):
#     return item[1]


# items.sort(key=sort_item)
# print(items)

# items = [
#     ("product", 10),
#     ("product", 9),
#     ("product", 12),
# ]

# items.sort(key=lambda item: item[1])
# print(items)

# items = [
#     ("product", 10),
#     ("product", 9),
#     ("product", 12),
# ]

# x = list(map(lambda item: item[1], items))
# print(x)

# items = [
#     ("product", 10),
#     ("product", 9),
#     ("product", 12),
# ]

# filtered = list(filter(lambda item: item[1] >= 11, items))
# print(filtered)

# items = [
#     ("product", 10),
#     ("product", 9),
#     ("product", 12),
# ]

# # prices = list(map(lambda item: item[1], items))
# prices = [item[1] for item in items]

# # filtered = list(filter(lambda item: item[1] >= 9, items))
# filtered = [item[1] for item in items if item[1] >= 10]

# print(prices)
# print(filtered)
# list1 = [1, 2, 3]
# list2 = [10, 20, 30]

# print(list(zip("abc", list1, list2)))
# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
# print(browsing_session)
# last = browsing_session.pop()
# print(last)
# print(browsing_session)
# if browsing_session:
#     print("Disable")
# from collections import deque
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()
# print(queue)
# point = (1, 2)
# print(type(point))
# print(point[0:2])
# x, y = point
# if 10 in point:
#     print("Got it")
# else:
#     print("Not found")
# x = 10
# y = 5
# z = x
# x = y
# y = z
# print(x)
# print(y)
# numbers = [1, 2, 2, 3, 4]
# first = set(numbers)
# second = {1, 4}
# print(first | second)
# print(first & second)
# point = dict(x=1, y=2)
# point["X"] = 10
# point["y"] = 20
# for key, value in point.items():
#     print(key, value)
# values = {x: x * 2 for x in range(5)}
# print(values)
a = [1, 2]
b = [3, 4]
combined = [*a, *b]
print(combined)
x = {"name": "john", "age": "18"}
y = {"place": "india"}
combined = {**x, **y}
print(combined)
