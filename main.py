import math
print("Hello World!")
print("*" * 10)
x = 1
y = 2
unit_price = 3
students_count = 999
rating = 5.5
is_published = True
course_name = "Python Programming"
print(students_count)
course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:2])
print(course[0:])
print(course[:3])
print(course[:])
# \'
# \"
course = "Python \'Programming"
print(course)
course = "  Python \nProgramming"
print(course)
first = "John"
last = "Ash"
full = first + " " + last
print(full)
first = "Jk"
last = "Hg"
full = f"{len(first)} {last}"
print(full)
print(course.upper())
print(course.lower())
print(course.strip())
print(course.rstrip())
course = "Python Development"
print(course.find("Dev"))
print("Pro" in course)
print("Dev" in course)
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 % 3)
print(10 // 3)
print(2 ** 3)

x = 10
x += 3
print(x)

x = 7.5
print(math.ceil(x))
x = 7.4
print(math.ceil(x))
y = 7
print(math.pow(x, y))

x = input("x: ")
y = int(x) + 1
print(x)
print(y)
print(f"x: {x}, y: {y}")
print(bool("False"))
"bag" > "Bag"

temperature = 20
if temperature > 15:
    print("Its good")
elif temperature < 20:
    print("Its chill")
print("Thank you")
age = 19
message = "Eligible to vote" if age >= 18 else "Not Eligible to vote"
print(message)

high_income = True
good_credit = False
good_score = True
if (high_income and good_credit) or not good_score:
    print("Eligible")
else:
    print("You are not eligible")

age = 18
if 18 >= age <= 65:
    print("You are eligible")

for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

for number in range(1, 10, 2):
    print("Attempt", number, number * "$")
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")
command = ""
while command.lower() != "quit":
    command = input("<>")
print("ECHO", command)
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        count += 1
print(f"We have {count} even numbers")
