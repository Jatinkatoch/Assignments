import pandas as pd
import logging as log

# Q1. List any five functions of the pandas library with execution.
# log.basicConfig(filename="assignment.log", level=log.NOTSET)
# data = {"Name": ["jatin", "katoch"], "Age": [10, 1]}
# df = pd.DataFrame(data)

# log.info(df.sort_values("Name"))
# log.info(pd.Categorical(data))
# log.info(df["Name"])
# print(df.groupby(["Age"]).sum())


# Q2. Given a Pandas DataFrame df with columns 'A', 'B', and 'C', write a Python function to re-index the
# DataFrame with a new index that starts from 1 and increments by 2 for each row.

log.basicConfig(filename="assignment1.log", level=log.NOTSET)


# def reindex_with_increment(df):
#     new_index = pd.Series(range(1, len(df) * 2, 2), name="new_index")
#     df = df.set_index(new_index)
#     return df


# df = pd.DataFrame({"A": [10, 20, 30], "B": [40, 50, 60], "C": [70, 80, 90]})
# df = reindex_with_increment(df)
# log.info(df)


# Q3. You have a Pandas DataFrame df with a column named 'Values'. Write a Python function that
# iterates over the DataFrame and calculates the sum of the first three values in the 'Values' column. The
# function should print the sum to the console.


# def sum_of_three(df):
#     req = df["Values"].iloc[:3]
#     sum = req.sum()
#     return sum


# data = {"numbers": [1, 2, 3, 4, 5], "Values": [10, 20, 30, 40, 50]}
# df = pd.DataFrame(data)
# ans = sum_of_three(df)
# log.info(ans)


# Q4. Given a Pandas DataFrame df with a column 'Text', write a Python function to create a new column
# 'Word_Count' that contains the number of words in each row of the 'Text' column.


# data = {"Text": ["Hello my name is jatin katoch"]}
# df = pd.DataFrame(data)
# df["Word_Count"] = df["Text"].apply(lambda x: len(x.split()))
# log.info(df["Word_Count"])


# Q5. How are DataFrame.size() and DataFrame.shape() different?

# DataFrame.size provides the total number of elements (cells) in the DataFrame.
# DataFrame.shape provides the dimensions of the DataFrame in terms of the number of rows and columns.


# Q6 Which function of pandas do we use to read an excel file?
# pd.read_excel()


# Q7. You have a Pandas DataFrame df that contains a column named 'Email' that contains email
# addresses in the format 'username@domain.com'. Write a Python function that creates a new column
# 'Username' in df that contains only the username part of each email address.


# data = {"Email": ["jatin@gmail.com", "katoch@gmail.com", "sakshi@gmail.com"]}
# df = pd.DataFrame(data)
# df["Username"] = df["Email"].apply(lambda email: email.split("@")[0])
# log.info(df["Username"])


# Q8. You have a Pandas DataFrame df with columns 'A', 'B', and 'C'. Write a Python function that selects
# all rows where the value in column 'A' is greater than 5 and the value in column 'B' is less than 10. The
# function should return a new DataFrame that contains only the selected rows.

# data = {
#     "A": [3, 8, 6, 2, 9],
#     "B": [5, 2, 9, 3, 1],
#     "C": [
#         1,
#         7,
#         4,
#         5,
#         2,
#     ],
# }


# def check(df):
#     selected_rows = df[(df["A"] > 5) & (df["B"] < 10)]
#     return selected_rows


# df = pd.DataFrame(data)
# ans = check(df)
# log.info(ans)


# Q9. Given a Pandas DataFrame df with a column 'Values', write a Python function to calculate the mean,
# median, and standard deviation of the values in the 'Values' column.


# data = {"Values": [1, 2, 3, 4, 5, 6, 7, 8, 9]}
# df = pd.DataFrame(data)
# log.info(df["Values"].mean())
# log.info(df["Values"].median())
# log.info(df["Values"].std())


# Q10. Given a Pandas DataFrame df with a column 'Sales' and a column 'Date', write a Python function to
# create a new column 'MovingAverage' that contains the moving average of the sales for the past 7 days
# for each row in the DataFrame. The moving average should be calculated using a window of size 7 and
# should include the current day.


# data = {
#     "Date": ["2023-07-23", "2023-07-24", "2023-07-25", "2023-07-26", "2023-07-27"],
#     "Sales": [10, 15, 20, 25, 30],
# }
# df = pd.DataFrame(data)
# df["Date"] = pd.to_datetime(df["Date"])
# df["Moving_Average"] = df["Sales"].rolling(window=7, min_periods=1).mean()
# log.info(df)

# Q11. You have a Pandas DataFrame df with a column 'Date'. Write a Python function that creates a new
# column 'Weekday' in the DataFrame. The 'Weekday' column should contain the weekday name (e.g.
# Monday, Tuesday) corresponding to each date in the 'Date' column.


# data = {"Date": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05"]}
# df = pd.DataFrame(data)
# print(df)
# df["Date"] = pd.to_datetime(df["Date"])
# df["Weekday"] = df["Date"].dt.day
# log.info(df)


# Q12. Given a Pandas DataFrame df with a column 'Date' that contains timestamps, write a Python
# function to select all rows where the date is between '2023-01-01' and '2023-01-31'.

# df = pd.DataFrame(
#     {"Date": ["2022-12-15", "2023-01-05", "2023-01-20", "2023-02-10", "2023-03-01"]}
# )
# df["Date"] = pd.to_datetime(df["Date"])
# start_date = "2023-01-01"
# end_date = "2023-01-31"
# df["mask"] = (df["Date"] >= start_date) & (df["Date"] <= end_date)
# log.info(df["mask"])

# Q13. To use the basic functions of pandas, what is the first and foremost necessary library that needs to
# be imported?

# import pandas as pd
