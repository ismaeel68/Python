# Function in python(Block of statements that perform a specific task)

def calc_sum(a,b):# This is function and first def mean is define
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

#practice question
cities=("Gujrat","Kotla","Bhimber","Kotli","Lahore","Mandi","Karachi")
heroes=("ironman","captain america","thor","batman")
def print_len(list):
    print(len(list))
print_len(cities)
print_len(heroes)
#practice question
cities=("Gujrat","Kotla","Bhimber","Kotli","Lahore","Mandi","Karachi")
heroes=("ironman","captain america","thor","batman")
print(heroes[0],end=" ")
print(heroes[1],end=" ")
def print_len(list):
    print(len(list))
