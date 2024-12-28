# #(File Input/Output) Python can be used to perform operations on a file.(read & write data)
# # In reading mode
# f=open("demo.txt","r")
# data=f.read() #f.read is used for read  the file and return all the data of the file
# print(data)
# print(type(data))
# f.close() #for closing the file

# f=open("demo.txt","r")
# data=f.read(5) #I also use your number from which number to which you want to read your file.
# print(data)
# f.close()

# f=open("demo.txt","r")
# line1=f.readline() #If i want to learn only 1 line so only i write the name of the line and this command 
# print(line1)
# line2=f.readline() 
# print(line2)
# f.close()

# f=open("demo.txt","r")
# data=f.read() #If first i read all the data of my file and next i want to read it line by line this is not poossible for this i close this file and reopen it 
# print(data)
# f.close()
# #In writing mode 
# f=open("demo.txt","w") # This (w) mean i overwrite in my file 
# f.write("I want to learn JavaScript tomorrow.12908") 
# f.close()
# #For writing a new line in same file we use (a)
# f=open("demo.txt","a") 
# f.write("\n Then I'll move to ReactJS") 
# f.close()
# #(R+ mode)
# f=open("demo.txt","r+")#This (R+) mode is over write the first letter of my file in this mode not truncate in my file
# f.write("Thora")
# print(f.read())
# f.close
# #(w+ mode)
# f=open("demo.txt","w+")#With (w+) mode my file is open in truncate mode means it deleted my all previous data and after i write what i want but i print nothing 
# f.write("abcd")
# print(f.read())
# f.close
# #(a+ mode)
# f=open("demo.txt","a+")#(a+) mode is open for reading and writing.The stream is positioned at the end of the file in this mode not truncate in my file
# print(f.read())
# f.write("\nThora")
# f.close()
# #(With Syntax)
# with open("demo.txt","r") as f:
#     data=f.read()
#     print(data)
# with open("demo.txt","w") as f:
#     f.write("new data")
# #(For deleting a File) using the os module
# import os
# os.remove("practice.txt")
# # practice question 1
# with open("practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learning file I/O\n")
#     f.write("using Java.\nI like programming in Java.")
# #practice question 2
# with open("practice.txt","r") as f:
#     data=f.read()
# new_data=data.replace("Java","Python")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)
# #practice question 3
# def check_for_word():
#     word="learning"
# with open("practice.txt","r") as f:
#     data=f.read()
#     if(data.find("word")):
#         print("Found")
#     else:
#         ("Not found")
# check_for_word()
# #practice questionn 4:
# def check_for_line():
#     word="programming"
#     data=True
#     line_no=1
#     with open ("practice.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no +=1
#     return-1
# check_for_line()
# #practice question 5:
# count=0
# with open("practice.txt","r") as f:
#     data=f.read()
    
    
#     num=""
#     for i in range(len(data)):
#         if (data[i]==","):
#              print(int(num))
#              num=""
#         else:
#             num+=data[i]
            
#     nums=data.spilt(",")
#     for val in nums:
#         if(int
#            (val)%2==0):
#             count+=1
# print(count)
# import os
# os.remove("some practice question")