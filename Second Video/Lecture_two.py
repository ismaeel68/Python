str1= "Thora.\nwe creating it in python"
str2= "Pagal.\t we creating in pyhton"
str3= "Kaliya"
print(str1,str2,str3)
#lenght function
str1="Thora love you"
print(len(str1))
str2="kaliya loves ismaeel"
print(str1+str2)
# #Indexing [in indexing starting with the 0 not with the 1]
str="Thora"
ch = str[4]
print(ch)
# positive Slicing [in silicing has starting_idx:but it has no ending idx]
str="Thora"
print(str[0:5])# if i miss te first letter o the last letter python know about the last o the first and he write it himself
# #negative slicing [in the negative silicing is start from the last number with the -1]
str="Thora"
print(str[-3:-1])
#function if i check my string is end with this letter if this is correcct give me the output True and if it is incorrect give me the output False
str="I am studing python"
print(str.endswith("hon"))
#capitalize In my string if i write my first letter in small and i write this capitalize in the command it shows into the Capital letter its create a new string not modifed the original string
str="you am studying python"
print(str.upper())