# Q1. Create a Pandas Series that contains the following data: 4, 8, 15, 16, 23, and 42. Then, print the series.
import pandas as pd
import logging
import numpy as np

logging.basicConfig(filename="assignment.log", level=logging.NOTSET)

data = np.array([4, 8, 15, 16, 23, 72])
ser = pd.Series(data)
logging.info(ser)


# Q2. Create a variable of list type containing 10 elements in it, and apply pandas.Series function on the
# variable print it.

logging.basicConfig(filename="assignment.log", level=logging.NOTSET)
s = ["j", "a", "t", "i", "n", 1, 2, 3, 4, 5]
ser = pd.Series(s)
logging.info(ser)

# Q3. Create a Pandas DataFrame that contains the following data:

# Name = Alice,bob,claire
# age=25,30,27
# Gender=Female,Male,Female
# Then print the dataframe

logging.basicConfig(filename="assignment.log", level=logging.NOTSET)
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 27],
    "Gender": ["Female", "Male", "Female"],
}
df = pd.DataFrame(data)
logging.info(df)

# Q4. What is ‘DataFrame’ in pandas and how is it different from pandas.series? Explain with an example.

# Sol A dataframe is a two dimensional data structre which can be created from list, dictionary and list of dictionaries,etc.
# while series is a one dimensional array capable of holding data of any type(int ,str,float)

# data = [1, 2, 3, 4]
# ser = pd.Series(data)
# print(ser)

#  data = {
#     "Name": ["Alice", "Bob", "Charlie"],
#     "Age": [25, 30, 27],
#     "Gender": ["Female", "Male", "Female"],
# }
# df = pd.DataFrame(data)
# print(df)

# What are some common functions you can use to manipulate data in a Pandas DataFrame? Can
# you give an example of when you might use one of these functions?

# function like dtypes,columns,new_columns,etc can be used to  manipulate data in Pandas
# data = {
#     "Name": ["Alice", "Bob", "Charlie"],
#     "Age": [25, 30, 27],
#     "Gender": ["Female", "Male", "Female"],
# }
# df = pd.DataFrame(data)

# print(df.dtypes)
# print(df.columns)

# Which of the following is mutable in nature Series, DataFrame, Panel?

# Sol dataframe is mutuable


# Create a DataFrame using multiple Series. Explain with an example.

logging.basicConfig(
    filename="assignment.log", level=logging.NOTSET, format="%(asctime)s"
)
s1 = pd.Series([10, 20, 30, 40, 50], name="Numbers")
s2 = pd.Series(["apple", "orange", "banana", "grape", "watermelon"], name="Fruits")
df = pd.concat([s1, s2], axis=1)
logging.info(df)
