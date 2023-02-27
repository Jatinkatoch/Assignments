# Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the
#  range of 1 to 25.
 
# Sol def keyword is used to create a function.
def odd():
    l=list(range(0,25))
    l1=[]
    for ele in l:
        if(ele%2!=0):
            l1.append(ele)
    return l1

print(odd())