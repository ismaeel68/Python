str1= "Thora.\nwe creating it in python"
str2= "Pagal.\t we creating in pyhton"
str3= "Kaliya"
print(str1,str2,str3)
# #lenght function
str1="Thora"
print(len(str1))
str2="kaliya"
print(str1+str2)
# Indexing [in indexing starting with the 0 not with the 1]
str="Thora"
ch = str[4]
print(ch)
# # positive Slicing [in silicing has starting_idx:but it has no ending idx]
str="Thora"
print(str[0:5])# if i miss te first letter o the last letter python know about the last o the first and he write it himself
# negative slicing [in the negative silicing is start from the last number with the -1]
str="Thora"
print(str[-3:-1])
#Function (ends with) if i check my string is end with this letter if this is correcct give me the output True and if it is incorrect give me the output False
str="I am studing python"
print(str.endswith("hon"))
#Function (capitalize)  In my string if i write my first letter in small and i write this capitalize in the command it shows into the Capital letter its create a new string not modifed the original string
str="i am studying python"
print(str.upper())
#Function (replace)
str ="I am studing python"
print(str.replace("puthon", "javascript"))
#Function (Find)
str="Thora na Roger ki t-shirt sale ki 40 euro ma"
print(str.find("s"))
#Function (count)
str="I am from studying python from Shrada khapra"
print(str.count("from"))

name= input("enter your name:")
print("lenght of your name", len (name))

str="Hi $i am the $symbol $99.99"
print(str.count("$"))
# (Conditional Statments) 3 tyoes of the conditional statment is 1 is (if) 2 is (elif) 3 is (else)
# 1 conditional statment is (If)
age=16
if(age >= 18):
    print("can vote & apply for license")   
# 2 conditional statment is (elif)i rite this how many times i want but the first statment is started with the (if)
light="green"

if(light == "red"):
    print("stop")
elif(light=="Green"):
    print("Go")
elif(light=="Yellow"):
    print("look")
#else this i write only in 1 time in the code this work when the upper 2 condition give the output False
light="Blue"

if(light == "red"):
    print("stop")
elif(light=="Green"):
    print("Go")
elif(light=="Yellow"):
    print("look")
else:
    print("the light is broken")

#nesting in 1 statment you add another statment
age=96
if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")

num=14
rem=num % 2
if(rem==0):
    print("Even")
else:
    print(ODD)


a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
if(a>=b and a>=c):
    print("first number is largest", a)
elif(b >= c):
    print("second number is largest", b)
else:
    print("third is largest", c)