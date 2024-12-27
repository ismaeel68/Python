#(OOPS in python) To map with real world scenarios,we started using object in code.
#(Class & Object) in python 
#Class is a blue print for creating object.
class Student: #This is a class 
    name="Karan"
S1 = Student()#This is a object
print(S1.name)

s2 = Student()
print(s2.name)

class Car:
    color="Black"
    brand="Mercedes"
car1 = Car
print(car1.color)
print(car1.brand)
#(Constructor)is(--init--Function) All classes have a function called _init_(),which is always executed when the object is being initiated.
name="Thora"
class Student:
    #default constructors
    def __init__(self):
        pass 
    #parameterized constructors 
    def __init__(self,name,marks):
        self.name = name
        self.marks=marks
        print("adding new student in Database.")
s1=Student("Thora",97)
print(s1.name,s1.marks)

s2=Student("Kaliya",88)
print(s2.name,s2.marks)

# Class&Instance Attributes
class Student:
    college_name="Punjab college"
    name="anonymous" #class attribute
    def __init__(self,name,marks):
        self.name=name #object attribute => class attribute
        self.marks=marks      
s1=Student("Karan",97)
#methods 
class Student:
    college_name="Punjab college"
    name="anonymous" #class attribute
    def __init__(self,name,marks):
        self.name=name #object attribute => class attribute
        self.marks=marks
    def welcome(self):
        print("welcome student",self.name)
    def get_marks(self):
        return self.marks        
s1=Student("Karan",97)
s1.welcome()
print(s1.get_marks())
#Practice question 1
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
            print("hi",self.name,"your avg score is:",sum/3)
s1=student("tommy",[99,98,97])
s1.get_avg()
#(static methods)that don't use the self parameter(work at class level)
@staticmethod #decorator
def hello():
    print("hello")
    
# (4 important topics of OOPS)Abstraction,Encapsulation,Inheritance,polymorphism
# (Abstraction)hiding the implementation details of a class and only showing the essential features to the user.
class Car:
    def __init__(self):
        self.accelerator=False
        self.brk=False
        self.clutch=False
    def start(self):
        self.clutch=True
        self.accelerator=True
        print("Car started.")
car1=Car()
car1.start()
# (Encapsulation) Wrapping data and functions into a single unit(object)
# Practice question 1
class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
        # debit method
    def debit(self,amount):
        self.balance -=amount
        print("Rs.",amount,"was debited")
        print("total balance=",self.get_balance())
        # credit method
    def credit(self,amount):
        self.balance +=amount
        print("Rs.",amount,"was credited")
        print("total balance=",self.get_balance())
    def get_balance(self):
        return self.balance
        
acc1=Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)  
acc1.credit(40000)   
acc1.debit(10000)    

#(del keyword) Used to delete object properties or object itself.
# class Student:
#     def __init__(self,name):
#         self.name=name
# s1=("Ismaeel")
# print(s1.name)
# del s1.name
#(private attributes & methods)
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass
    def reset_pass(self):
        print(self.__acc_pass)
acc1=Account("12345","abcde")
print(acc1.acc_no)
print(acc1.reset_pass())

class Person:
    __name="anonymous"

    def __hello(self,name):
        print("hello person!")
    def welcome(self):
        self.__hello()

p1=Person()
print(p1.welcome())