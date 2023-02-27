# # Q1--> Explain with an example each when to use a for loop and a while loop?

# For Loop: A for loop is an iteration method that is best used when you know the number of iterations ahead of time.
#  It’s always followed by the initialization, expression and increment statements.

# While Loop: A while loop is an iteration method that is best used when you don't know the number of iterations ahead
#  of time. The contents of the loop are executed as long as the expression evaluates to true.

# Q2--> Write a python program to print the sum and the product of the first 10 natural numberers 
# usig for and while loop ?

# Sol. using for loop 
# sum=0
# product =1
# for i in range(1,11):
#     sum+=i
#     product*=i
# print(f"sum={sum}\nproduct={product}")
    
# Sol. using while loop

# i=1
# sum=0
# product=1
# while i<=10:
#     sum+=i
#     product*=i
#     i+=1
# print(f"sum={sum}\nproduct={product}")

# Q3--> Create a python program to compute the electricity bill for a household?

# The per-unit charges in rupees are as follows: For the first 100 units, the user will be charged Rs. 4.5 per
# unit, for the next 100 units, the user will be charged Rs. 6 per unit, and for the next 100 units, the user will
# be charged Rs. 10 per unit, After 300 units and above the user will be charged Rs. 20 per unit.
# You are required to take the units of electricity consumed in a month from the user as input.
# print("Enter the unit consumed:\n")
# unit=int(input())
# if(unit>=0 and unit<=100):
#     bill= unit*4,5
#     print("The electricity bill is:",bill)
# elif(unit>100 and unit <=200):
#     bill=(100*4.5)+(unit-100)*6
#     print("The electricity bill is:",bill)
# elif(unit>200 and unit<=300):
#     bill=(100*4.5)+(100*6)+(unit-200)*10
#     print("The electricity bill is:",bill)
# elif unit>300:
#     bill = (100*4.5)+(100*6)+(100*10)+(unit-300)*20
#     print("The electricity bill is:",bill)

# Q4--> Create a list of numbers from 1 to 100. Use for loop and while loop calculate the cube of each number and 
# if the cube of that number is divisible by 4 or 5 then append that number in a list and print that list?

# Sol--> Using for loop

# lst=list(range(1,100))
# # print(lst)
# lst_cube=[]
# for ele in lst:
#     num= ele*ele*ele
#     if num%4==0 or num%5==0:
#         lst_cube.append(ele)
#     else:
#         continue
# print(lst_cube)

# Sol--> Using while loop
# lst=list(range(1,100))
# lst_cube=[]
# i=1
# while i<=len(lst):
#     num= i*i*i
#     if num%4==0 or num%5==0:
#         lst_cube.append(i)
#     else:
#         continue
#     i+=1
# print(lst_cube)

# Q5--> Write a program to filter count vowels in the below-given string.
# string="I want to became a data scientist"

# str="I want to became a data scientist"
# print(str.count("a"))
# print(str.count("e"))
# print(str.count("i"))
# print(str.count("I"))
# print(str.count("o"))
# print(str.count("u"))



