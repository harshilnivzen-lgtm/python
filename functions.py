# # # # def greet(first_name, last_name):
# # # #     print(f"Hi {first_name}, {last_name}")
# # # #     print("Welcome abroad")


# # # # greet("John", "Den")


# # # # def greeting(name):
# # # #     return f"hi {name} "


# # # # message = greeting("Magnus")
# # # # print(message)


# # # # def increment(number, by):
# # # #     return number + by


# # # # print(increment(2, by=2))
# # # def increment(number, by=1):
# # #     return number + by


# # # print(increment(2))
# # def multiply(*numbers):
# #     total = 1
# #     for number in numbers:
# #         total *= number
# #      return total


# # print(multiply(2, 3, 4, 5))
# def save_user(**user):
#     print(user["age"])


# save_user(id=2, name="Den", age=20)
# message = "a"

# def greet(name):
#     global message
#     message = "b"


# print(greet("john"))
# print(message)


# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print("start")
# print(multiply(2, 3, 4, 5))

def fizz_buzz(input):

    if input % 3 == 0 and input % 5 == 0:
        print("fizz_buzz")
    elif input % 3 == 0:
        print("fizz")
    elif input % 5 == 0:
        print("buzz")
    else:
        print(input)


fizz_buzz(15)
