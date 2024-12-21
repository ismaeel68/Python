# list built-in data type that stores set of values it can store elements of different types(integer, float, string, etc.)
marks=[94.3,66.3,78.9]
print(marks)
print(type(marks))
print(marks[0])
print(marks[2])
#(Lists) are mutable but the strings are imutable. In strings i have an access in index but i don't change but in list this is possible i have also access and i also change it
# Exemple of the string 
# str="hello"
# print(str[0])
# str[0]="y"
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
list=("a","b","c","d","e","f")
list.reverse()
print(list)
# #(list method) 4 method is insert 
list=(2,1,3)
list.insert (1,5)
print(list)
#(list method) removes first occurence of element
list=[2,1,3,1]
list.pop(2)
print(list)
