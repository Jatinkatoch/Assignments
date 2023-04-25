# Q1 What is an Exception in python? Write the differnce between Exceptions and Syntax error?

# Sol. An exception is a Python object which represents an error. As with code comments,
# exceptions helps you to remind yourself of what the program expects. It clarifies the code and
# enhances readability.

# An error is an issue in a program that prevents the program from completing its task.
# In comparison, an exception is a condition that interrupts the normal flow of the program.


# Q2--> What happens when an exception is not handled? Explain with an example?
# If the exception is not handled by an except clause, the exception is re-raised after the finally clause has been executed.

# Q3--> Which Python statements are used to catch and handle exceptions? Explain with an example.
# Sol. try and except  are used to handle exception.

#  Python executes code following the try statement as a “normal” part of the program. The code that
#  follows the except statement is the program's response to any exceptions in the preceding try clause.

# Q4--> Explain with an example:

# a: try and else
# b: finally
# c: raise


# try:
#     f = open("helo.txt", "w")
#     f.write("write into my file")
# except Exception as e:
#     print("this is my except block", e)

# else:
#     f.close()
#     print("this will be excuted once your try will excute without error")

# try:
#     f = open("hello2.txt", "w")
#     f.write("write something")
# finally:
#     print("finally will execute itself in any situation")

# class validate_age(Exception):
#     def __init__(self, msg):
#         self.msg = msg


# def validate_age(age):
#     if age < 0:
#         raise validate_age("Entered age is negative")
#     elif age > 200:
#         raise validate_age("Entered age is very high")
#     else:
#         print("age is valid")


# try:
#     age = int(input("enter your age"))
#     validate_age(age)
# except validate_age as e:
#     print(e)


# Q5-> What are Custom Exception in pyton? Why do we need Custom Exceptions? Explain with an example.

# custom exceptions are named as user-defined exceptions. Here the user-defined exceptions can be built defined
# by using a class declared for it.

# USE:
#  can make your code much more readable and robust, and reduce the amount of code you write later to try and
# figure out what exactly went wrong.

# Example:

# define Python user-defined exceptions
# class InvalidAgeException(Exception):
#     "Raised when the input value is less than 18"
#     pass


# # you need to guess this number
# number = 18

# try:
#     input_num = int(input("Enter a number: "))
#     if input_num < number:
#         raise InvalidAgeException
#     else:
#         print("Eligible to Vote")

# except InvalidAgeException:
#   print("Exception occurred: Invalid Age")

# Q Create a custom exception class. Use this class to handle an Exception?

# define Python user-defined exceptions
# class InvalidAgeException(Exception):
#     "Raised when the input value is less than 18"
#     pass


# # you need to guess this number
# number = 18

# try:
#     input_num = int(input("Enter a number: "))
#     if input_num < number:
#         raise InvalidAgeException
#     else:
#         print("Eligible to Vote")

# except InvalidAgeException:
#  print("Exception occurred: Invalid Age")
