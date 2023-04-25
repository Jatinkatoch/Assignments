# Q1. Explain why we have to use the Exception class while creating a Custom Exception.
# Built-in exceptions offer information about Python-related problems, and custom exceptions will add
# information about project-related problems. That way, you can design your code (and traceback, if an
# exception is raised) in a way that combines Python code with the language of the project.

# Q2--> Write a Python Program to print Python Exception Hierarchy
# # import inspect module
# import inspect

# # our treeClass function
# def treeClass(cls, ind = 0):

#       # print name of the class
#     print ('-' * ind, cls.__name__)

#     # iterating through subclasses
#     for i in cls.__subclasses__():
#         treeClass(i, ind + 3)

# print("Hierarchy for Built-in exceptions is : ")

# # inspect.getmro() Return a tuple
# # of class  cls’s base classes.

# # building a tree hierarchy
# inspect.getclasstree(inspect.getmro(BaseException))

# # function call
# treeClass(BaseException)


# What errors are defined in the ArithmeticError class? Explain any two with an example.

# ArithmeticError types in Python include:

# OverFlowError
# ZeroDivisionError
# FloatingPointError

# try:
#     a = 10 / 0
# except ZeroDivisionError as e:
#     print(e)

# j = 5.0

# try:
#     for i in range(1, 1000):
#         j = j**i
#         print(j)
# except OverflowError as e:
#     print("Overflow error happened")
#     print(f"{e}, {e.__class__}")


# Q4. Why LookupError class is used? Explain with an example KeyError and IndexError.

# You can use LookupError exception class to handle both IndexError and KeyError exception classes.

# --> LookupError
#  --> IndexError
#  --> KeyError


# x = [1, 2, 3, 4]
# try:
#     print(x[10])
# except LookupError as e:
#     print(e)


# try:
#     d = {"key": "jatin", 1: [2, 3, 4]}
#     print(d["key2"])
# except LookupError as e:
#     print(e)

# Q5. Explain ImportError. What is ModuleNotFoundError?
# try:
#     import jatin
# except ImportError as e:
#     print(e)

# ModuleNotFoundError is same as Import error

# Q6. List down some best practices for exception handling in python.


# use always a specifice exception
# print always a proper message
# always try to log your error
# always avoid to write multiple exception handling
# Document all the error
# cleanup all the resource
