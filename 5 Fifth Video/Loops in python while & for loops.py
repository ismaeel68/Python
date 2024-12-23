#While Loops
count=1
while count <=5:
    print("Hello")
    count+=1
# print(count)

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
    else:
        print("finding")
    i+=1

#(Break and Continue) in loops used to terminate the loop when encountered.
