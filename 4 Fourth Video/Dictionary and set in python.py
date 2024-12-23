#Dictionary in Python (Dictionaries are used to store data values in key:value pairs) dictionary are unordered dictionary are mutable and don't allow duplicate keys.

info={
    "name":"dictionary",
    "subjects":["Python","C","Java"],
    "topics":("dict","set"),
    "age":16,
    "is_adult":True,
    "12":94.4}
print(info["name"])
print(info["topics"])
print(info["age"])
info["name"]="Ismaeel"
info["surname"]="Raja"
print(info)
#Nested Dictionaries
student={
    "name":"Raul",
    "Subjects":{
        "phy":97,
        "Chem":89,
        "Maths":78
    }
    }
print(student["Subjects"] ["phy"])
#(Dictionary methods) 1st dictionary method is (Dict.keys) returns all the keys
student={
    "name":"Raul",
    "Subjects":{
        "phy":97,
        "Chem":89,
        "Maths":78
    }
    }
print(list(student.keys()))
#(Dictionary methods) 2nd dictionary method is (Dict.values) returns all values
student={
    "name":"Raul",
    "Subjects":{
        "phy":97,
        "Chem":89,
        "Maths":78
    }
    }
print(list(student.values()))
#(Dictionary methods) 3rd dictionary method is (Dict.items) returns all(key,value) pairs as a tuples
student={
    "name":"Raul",
    "Subjects":{
        "phy":97,
        "Chem":89,
        "Maths":78
    }
    }
pairs=list(student.items())
print(pairs[1])
#(Dictionary methods) 4th dictionary method is (Dict.get) returns the key according to value
student={
    "name":"Raul",
    "Subjects":{
        "phy":97,
        "Chem":89,
        "Maths":78
    }
    }
print(student["name"]) #if by mistakely i add 2 with the name and this print give me the error 
print(student.get("name")) #but this not give me the error this print give me the none
#(Dictionary methods) 5th dictionary method is (Dict.update) inserts the specified items to the dictionary
student={
    "name":"Raul",
    "Subjects":{
        "phy":97,
        "Chem":89,
        "Maths":78
    }
    }
student.update({"City" : "Gujrat"})
print(student)
#set in python (set is the collection of the unordered items),Each element is the set must be unique &immutable 
collection={1,2,3,4}
print(collection)
print(type(collection))
collection=set() #this is used for the empty set
print(type(collection))
#(set methods) 1st (set method) is (set.add) adds an element
collection=set()
collection.add(1)
collection.add(2)
#(set methods) 2nd (set method) is (set.remove) remove an element
collection.remove(1)
collection.remove(2)
print(collection)
#(set methods) 3rd (set method) is (set.clear) empties the set 
collection=set()
collection.add(3)
collection.add(7)
collection.add("Helloworld")
collection.add((1,2,3,4))
collection.clear()
print(len(collection))
#(set methods) 4th (set method) is (set.pop) removes a random value 
collection={"Hello","Python","coding","world"}
print(collection.pop())
print(collection.pop())
#set.union (combines both set values & returns new)
set1={1,2,3}
set2={2,3,4}
print(set1.union(set2))
print(set1)
print(set2)
#set.intersection(combines common values & returns new)
set1={1,2,3}
set2={2,3,4}
print(set1.intersection(set2))
#practice questions 
dictionary={
    "cat":"a small animal",
    "table":["a piece of furniture","list of facts & figures"]
}
print(dictionary)
#practice questions 
subjects={
    "python","java","c++","python","javascript","java",
    "python","java","c++","C"
}
print(subjects)
print(len(subjects))
#practice question
marks={}
x=int(input("enter phy:"))
marks.update({"phy":x})

x=int(input("enter maths:"))
marks.update({"maths":x})

x=int(input("enter chem:"))
marks.update({"chem":x})
print(marks)
#practice question
values={
    ("float",9.0),
    ("int",9),
}
print(values)



#practice 
