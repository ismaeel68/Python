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
#(Dictionary methods) 3rd dictionary method is (Dictt.items) returns all(key,value) pairs as a tuples
student={
    "name":"Raul",
    "Subjects":{
        "phy":97,
        "Chem":89,
        "Maths":78
    }
    }
pairs=list(student.items())
print(pairs[0])