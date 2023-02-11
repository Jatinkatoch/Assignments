# Q1--> Write a program to accept percentage from the user and display the grade 
# according to the following criteria:

# Marks>90 Grade=A
# >80 and <=90 Grade=B
# >=60 and <=80 Grade =C
# below 60 Grade =D

#Sol--> marks=int(input("Enter your marks:"))
# if(marks>90):
#     Grade="A"
# elif(marks>80):
#     Grade="B"
# elif(marks>=60):
#     Grade="C"
# else:
#     Grade="D"
# print("Grade=",Grade)
# -----------------------------------------------------------------------------------------------------------------------------------


# Q2--> Write a program to accept the cost price of a bike and display the road tax to be paid 
# according to the following criteria:

# Tax= 15% Cost price>10000
# Tax=10%  Cost price>50000 and<=10000
# Tax=5% Cost price<=50000


# sol--> cp=int(input("Enter the cost of your bike:"))
# if(cp>100000):
#     tax=0.15
# elif (cp>50000):
#     tax=0.1
# else:
#     tax=0.5
# rt=cp*tax
# print("The road tax to be paid is:",rt)

# ----------------------------------------------------------------------------------------------------------------------------------


# Q3--> Accept any city from the user and display monuments of that  city .
# City    Monuments

# Delhi    Red fort
# Agra     Taj mahal
# Jaipur   Jal Mahal


# sol--> City =  input("Enter the name of your city:")
# if (City=="Delhi" or City=="delhi"):
#     Monument="Red Fort"
# elif(City=="Agra" or City=="agra"):
#     Monument="Taj Mahal"
# elif (City=="Jaipur" or City=="jaipur"):
#     Monument="Jal Mahal"
# else:
#     print("Choose between Delhi,Agra and Jaipur")
#     
    
# print("Famous Monument in your city is:",Monument)

# ---------------------------------------------------------------------------------------------------------------------------------


# Q4--> Check how many times a given number can be divided by 3 before it is less than or equal to 10?
# sol-->num=int(input("Enter the number:"))
# count=0
# while num>=10:
#     if(num%3==0):
#         count+=1
#     else: pass

#     num-=1

# print(count)

# -------------------------------------------------------------------------------------------------------------------------------------

# Q7--> Reverse a while loop to display numbers from 10 to 1.
#  sol-->i=10
# while i>0:
#     print(i)
#     i-=1
#Q6--> Why and when to use while loop in python give a detailed description with example?
# sol--> Python while loop is used to run a block code until a certain condition is met.
# ---------------------------------------------------------------------------------------------------------------------------------------------------
#Q6--> Use nested while loop to print different patterns?

# n=5
 
# i=1;j=0

# while(i<=n):
#     while(j<=i-1):
#         print("* ",end="")
#         j+=1
#     print("\r")
#     j=0;i+=1