# # # # # # class Car:
# # # # # #     pass


# # # # # # my_car = Car()

# # # # # # print(type(my_car))
# # # # # # class Car:

# # # # # #     def __init__(self, brand, color):
# # # # # #         self.brand = brand
# # # # # #         self.color = color


# # # # # # my_car = Car("Toyota", "Suzuki")
# # # # # # print(my_car.brand, my_car.color)

# # # # # # class Car:
# # # # # #     def __init__(self, brand, color):
# # # # # #         self.brand = brand
# # # # # #         self.color = color

# # # # # #     def describe(self):
# # # # # #         print(f"This is a {self.color} {self.brand}")


# # # # # # my_car = Car("Toyota", "Red")
# # # # # # my_car.describe()
# # # # # # class Car:
# # # # # #     total_cars = 0

# # # # # #     def __init__(self, brand):
# # # # # #         self.brand = brand
# # # # # #         Car.total_cars += 1


# # # # # # c1 = Car("Toyota")
# # # # # # c2 = Car("Suzuki")
# # # # # # print(Car.total_cars)
# # # # # # class Device:
# # # # # #     def turn_on(self):
# # # # # #         print("Device is on")


# # # # # # class Phone(Device):
# # # # # #     def make_call(self):
# # # # # #         print("Calling...")


# # # # # # my_phone = Phone()
# # # # # # my_phone.turn_on()
# # # # # # my_phone.make_call()
# # # # # class Appliance:
# # # # #     def plug_in(self):
# # # # #         print("Plugged in")


# # # # # class WashingMachine(Appliance):
# # # # #     def wash(self):
# # # # #         print("Washing clothes")


# # # # # class SmartWashingMachine(WashingMachine):
# # # # #     def connect_wifi(self):
# # # # #         print("Connected to Wifi")


# # # # # my_SmartWashingMachine = SmartWashingMachine()
# # # # # my_SmartWashingMachine.plug_in()
# # # # # my_SmartWashingMachine.wash()
# # # # # my_SmartWashingMachine.connect_wifi

# # # # class Animal:
# # # #     def sound(self):
# # # #         print("Some sound")


# # # # class Dog(Animal):
# # # #     def sound(self):
# # # #         print("Woof Woof")


# # # # class Cat(Animal):
# # # #     def sound(self):
# # # #         print("Meow Meow")


# # # # dog = Dog()
# # # # cat = Cat()

# # # # dog.sound()
# # # # cat.sound()
# # # class Bird:
# # #     def speak(self):
# # #         print("Chirp")


# # # class Cow:
# # #     def speak(self):
# # #         print("Moo")


# # # def make_sound(animal):
# # #     animal.speak()


# # # bird = Bird()
# # # cow = Cow()

# # # make_sound(bird)
# # # make_sound(cow)

# # class Student:
# #     def __init__(self, marks):
# #         if marks >= 0:
# #             self.__marks = marks
# #         else:
# #             print("Invalid marks")
# #             self.__marks = 0

# #     def get_marks(self):
# #         return self.__marks

# #     def set_marks(self, score):
# #         if score >= 0:
# #             self.__marks = score
# #         else:
# #             print("marks entered are invalid")


# # total = Student(1)
# # print(total.get_marks())

# def make_sound(animal):
#     animal.sound()


# class Fish:
#     def sound(self):
#         print("swimming")


# make_sound(Fish())
