# Function in python(Block of statements that perform a specific task)

def calc_sum(a,b):# This is function and def mean is define
    sum=a+b
    print(sum)
calc_sum(5,10)

calc_sum(2,10)

calc_sum(12,7)

def calc_sum(a,b):#(a ,b) is parameters 
    return a+b
sum=calc_sum(156,3892) #function call;(156,3892)caleed arguments
print(sum)

def print_hello():
    print("hello")
print_hello()
print_hello()
print_hello()

#average of 3 numbers
def calc_avg(a,b,c):
    sum=a + b +c
    avg=sum/3
    print(avg)
    return avg

calc_avg(98,97,95)    

#(Types of the function) 2 types of the function 1 type is (built-in Functions) / (User defined Function)
#(print(),len(),type(),range()) These are (built-in Functions)
print("apnacollege",end="") # Write end for combining 2 lines 
print ("Ismaeel")
# len()
# range()
#user define Functions
def cal_prod(b,a=2):
    print(a+b)
    return a*b
cal_prod(1)

#practice question 1
cities=("Gujrat","Kotla","Bhimber","Kotli","Lahore","Mandi","Karachi")
heroes=("ironman","captain america","thor","batman")
def print_len(list):
    print(len(list))
print_len(cities)
print_len(heroes)
#practice question 2
cities=("Gujrat","Kotla","Bhimber","Kotli","Lahore","Mandi","Karachi")
heroes=("ironman","captain america","thor","batman")
print(heroes[0],end=" ")
print(heroes[1],end=" ")
def print_len(list):
    print(len(list))
#practice question 3

def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
cal_fact(6)

#practice question 4
def converter(usd_val):
    pkr_val=usd_val*278
    print(usd_val,"USD=",pkr_val,"PKR")

converter(100)
#practice question
n=int(input("enter your num:"))
def odd_or_even(n):
    if(n%2==0):
        print("Even")
    else:
        print("Odd")
odd_or_even(n)
#(Recursion) When a function calls itself repeatedly
#Recursive function
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
    print("End")
show(3)
def fact(n):
    if(n==1 or n==0):
        return 1    
    return fact(n-1)*n
print(fact(4))
def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n
print(fact(3))
#practice question 1
def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1) +n
sum=calc_sum(5)
print(sum)
#practice question 2
def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

Fruits=["mango","litchi","apple","banana"]
print_list(Fruits)

num = 14
if num % 2 == 0:
    print("Even")
else:
    print("Odd")