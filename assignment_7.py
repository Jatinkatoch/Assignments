# Q1, Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed
# and average_of_vehicle.


# class vechile:
#     def __init__(self, name_of_vechile, max_speed, average_of_vechile):
#         self.name_of_vechile = name_of_vechile
#         self.max_speed = max_speed
#         self.average_of_vechile = average_of_vechile

#     def return_vechile_details(self):
#         return self.name_of_vechile, self.max_speed, self.average_of_vechile


# obj = vechile("G-Wagon", 220, 8.13)
# print(obj.return_vechile_details())

# Q2. Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class.
# Create a method named seating_capacity which takes capacity as an argument and returns the name of
# the vehicle and its seating capacity.

# Sol:-->
# class vechile:
#     def __init__(self, name_of_vechile, max_speed, average_of_vechile):
#         self.name_of_vechile = name_of_vechile
#         self.max_speed = max_speed
#         self.average_of_vechile = average_of_vechile

#     def return_vechile_details(self):
#         return self.name_of_vechile, self.max_speed, self.average_of_vechile


# class child(vechile):
#     def seating_capacity(self, capacity):
#         self.capacity = capacity
#         return (self.name_of_vechile, self.capacity)


# jatin = child("G-Wagon", 220, 8.13)
# print(jatin.seating_capacity(5))


# Q3. What is multiple inheritance? Write a python code to demonstrate multiple inheritance.
# Sol:--> If a class inherits from more than one class we call it multiple inheritance in Python.

# class class1:
#     def test_class1(self):
#         return "this is class one"


# class class2:
#     def test_class2(self):
#         return "This is class2"


# class class3(class1, class2):
#     pass


# obj_class3 = class3()

# print(obj_class3.test_class1())
# print(obj_class3.test_class2())


# Q4. What are getter and setter in python?  Create a class and create a getter and a setter method in this class.

# Getters and Setters in python are often used when:

# We use getters & setters to add validation logic around getting and
# setting a value.
# To avoid direct access of a class field i.e. private variables cannot be
# accessed directly or modified by external user.


# class car:
#     def __init__(self, year, make, model, speed):
#         self.__year = year
#         self.__make = make
#         self.__model = model
#         self.__speed = 0

#     def set_speed(self, speed):
#         self.__speed = 0 if speed < 0 else speed

#     def get_speed(self):
#         return self.__speed


# c = car(2021, "toyata", "fortuner", 12)
# print(c._car__year)
# (c.set_speed(-3245))
# print(c.get_speed())


# Q5.What is method overriding in python?Write a python code to demonstrate method overriding.

# When a method in a subclass has the same name, same parameters or signature and same return type(or sub-type)
# as a method in its super-class, then the method in the subclass is said to override the method in the
# super-class.

# Example:


# Defining parent class
# class Parent:
#     def __init__(self):
#         self.value = "Inside Parent"

#     def show(self):
#         print(self.value)


# # Defining child class
# class Child(Parent):
#     def __init__(self):
#         self.value = "Inside Child"

#     def show(self):
#         print(self.value)


# obj1 = Parent()
# obj2 = Child()

# obj1.show()
# obj2.show()
