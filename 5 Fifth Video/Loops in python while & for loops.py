#loops are used to repeat instructions
#While Loops
count=1
while count <=5:
    print("Hello")
    count+=1
print(count)

i=5
while i >=1:#This is a stopping condition
    print("Hello")
    i-=1
print("loop ended")

#Practice question 1
i=1
while i <=100:
    print(i)
    i+=1
# Practice question 2
i=100
while i >=1:
    print(i)
    i-=1
# Practice question 3
n=int(input("enter your number:"))
i=1
while i <=10:
    print(n*i)
    i+=1
# Practice question 4
nums=[1,4,9,16,25,36,49,64,81,100]
heroes=["ironman","batman","thor","superman"] #traverse
idx=0
while idx <len(heroes):
    print(heroes[idx])
    idx+=1
idx=0
while idx <len(nums):
    print(nums[idx])
    idx +=1
#Practice question 5
nums=(1,4,9,16,25,36,49,64,81,100,36)
x = 36
i=0 #initialization
while i < len(nums):
    if(nums[i] ==x):
        print("Found at idx",i)
        break
    else:
        print("finding")
    i+=1
#(2 Types are loops)
#1 type is (Break) in loops used to terminate the loop when encountered.
i=1
while i <= 5:
    print(i)
    if(i==3):
        break    
    i+=1   
# 2 type is (continue) terminates execution in the current iteration&continue execution of the loop with the next iteration
i=4
while i<=9:
    if(i==6):
        i+=1
        continue #skip
    print(i)
    i+=1

i=1
while i <=10:
    if(i%2==0):   #this sign is used for the check of the even number
        i+=1
        continue
    print(i)
    i+=1
    
i=1
while i <=10:
    if(i%2 !=0):   #this sign is used for the check of the odd number
        i+=1
        continue
    print(i)
    i+=100
#(For loop) are used for sequential traversal. 
nums=[1,2,3,4,5]
for el in nums:
    print(el)
    
#practice question

idx="*"
for el in nums:
        print(idx)
        
number = 0        
        
#Range is (start,stop,step)in loops Rannge functions returns a sequence of number,starting from 0 by default,and increments by 1(by default), and stops before a specified number.
print(range(5))
seq=range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])

seq=range(5) 
for i in seq: #loop applied
    print(i)

#3 types for writing the range 1st is start 2nd is stop and the 3rd is step
#(1st range (start) is optional)
#(2nd range (stop) is compulsory)
#(3rd range (step) is also optional)
for i in  range(10):#range(stop)
    print(i)
for i in  range(2,10):#range(start,stop)
    print(i)
for i in  range(2,10,2):#range(start,stop,step) step mean inccreasing value in start
    print(i)

for i in range(2,100,2): #for printing the even numbers
    print(i)
for i in range(1,100,2): #for printing the odd numbers
    print(i)
for i in range (1, 101):
    print(i)
#practice question 2
for i in range (100,0,-1):
    print(i)
#practice question 3
n=int(input("enter number:"))
for i in range (1,11):
    print(n*i)

#Pass statment in loops(pass is a null statment that does nothing).It is used as a placeolder for future code.
for i in range(1):
    pass

#practice question 1
num=7
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
    print("total sum=",sum) 
#practice question 2
n=5  # solve withe while loop
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
    print("factoral=", fact) 

# solve with the (For loop) 
n=5
fact=1
for i in range (1,n+1):
    fact*=i
print("factorial=",fact)

#practice



for i in range (0,10):
    print("*")