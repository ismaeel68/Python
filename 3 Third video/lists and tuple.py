# list built-in data type that stores set of values it can store elements of different types(integer, float, string, etc.)
marks=[94.3,66.3,78.9]
print(marks)
print(type(marks))
print(marks[0])
print(marks[2])
#(Lists) are mutable but the strings are imutable. In strings i have an access in index but i don't change but in list this is possible i have also access and i also change it
# Exemple of the string 
# str="hello"
# print(str[o])
# str[o]="y"
#Exemple of the list
student=["Thora", 67.9 , 42, "Hospitalet de llobregat"]
print(student[0])
student[0]="Kaliya"
print(student)
# list slicing 
marks=(85,89,76,78,90)
print(marks[-3:-1])
#(list Methods)
#1 (list method) adds one element at the end 
list=[2,1,3]
list.append (4)
print(list)
#(sort method) sort in ascending order 
list=[2,1,3]
print(list.append(4))
print(list.sort() )
print(list)
#(sort method) sort in descending order 
list=[2,1,3]
print(list.append(4))
print (list.sort(reverse=True))
print(list)
#(list methods) 3 metthod is reverse
# list=("a","b","c","d","e","f")
# list.reverse()
# print(list)
#(list method) 4 method is insert 
# list=(2,1,3)
# list.insert (1,5)
# print(list)
#(list method) removes first occurence of element
list=[2,1,3,1]
list.pop(2)
print(list)
list[0]=4
#(Tuple) is a built-in data type that lets us create immutable sequences of values
tuple=(2,1,3,1)
print(tuple[0])
print(tuple[3])
#In (tuple) we can also print an empty tuple
tuple=()
print(tuple)
print(type(tuple))
#When you add the single type of the element in tuple you must add,to separate the tuple and then you print it and it give you the correct output
tuple=(1,)
print(tuple)
tuple=(1, 2, 3, 4)
print(tuple[1:3])
#(Tuple methods) (1 method is index)returns index of first occurrence
tuple=(1,2,3,4)
print(tuple.index(2))
#(Tuple methods) (2 method is count) counts total occurence
tuple=(1,2,2,2,3,4)
print(tuple.count(2))
#practice question
movies=[]
mov1= input("enter 1st movie:")
mov2= input("enter 2st movie:")
mov3= input("enter 3rd movie:")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

grade =("C","D","A","A","B","B","A")
print(grade.count("A"))

list=["C","D","A","A","B","B","A"]
list.sort()
print(list)

#Practice
marks=[94.3,66.3,78.9]
print(marks)
print(type(marks))
print(marks[0])
print(marks[2])

# str="Hello"
# print(str[0])
# str(0)=[y]

student=["Thora", 67.9 , 42, "Hospitalet de llobregat"]
print(student[0])
student[0]="Kaliya"
print(student)
marks=(85,89,76,78,90)
print(marks[-3:-1])
list=[2,1,3]
list.append (4)
print(list)
list=[2,1,3]
print(list.append(4))
print(list.sort() )
print(list)
list=[2,1,3]
print(list.append(4))
print (list.sort(reverse=True))
print(list)

list=[2,1,3,1]
list.pop(2)
print(list)
list[0]=4

tuple=(2,1,3,1)
print(tuple[0])
print(tuple[3])
movies=[]
mov1= input("enter 1st movie:")
mov2= input("enter 2st movie:")
mov3= input("enter 3rd movie:")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

grade =("C","D","A","A","B","B","A")
print(grade.count("A"))

list=["C","D","A","A","B","B","A"]
list.sort()
print(list)
tuple=(1,)
print(tuple)
tuple=(1, 2, 3, 4)
print(tuple[1:3])