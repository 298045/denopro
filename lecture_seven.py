# f= open("demo.txt","r")
# data =f.read()
# print(data)
# print(type(data))
# f.close()

# f= open("demo.txt","r")
# line1=f.readline()
# print(line1)
# print(type(line1))

# line2=f.readline()
# print(line2)
# print(type(line2))

# line3=f.readline()
# print(line3)
# print(type(line3))

# f.close()

# f=open("sample.txt","w")

# f.write("this is the new line")

# f.write("\n i will learn tommarow DSA \n")
# f.close()

# f=open("sample.txt","a")
# f.write(" \n the process of creating and publishing written content ")
# f.close()

# f=open("demo.txt","r+")
# f.write("abc")
# print(f.read())
# f.close()

# f=open("demo.txt","w+")
# # f.write("abc")
# print(f.read())
# f.write("abc")
# f.close()

# f=open("demo.txt","a+")
# print(f.read())
# f.write("abc")
# f.close()

# with open("demo.txt","r") as f:
#     data=f.read()
#     print(data)
    
    
# with open("demo.txt","w") as f:
#     f.write("new data")
  
# import os
# os.remove("sample.txt")  

# f=open("practice.txt","a")
# f.write("Hi everyone \nwe are learning file I/O ")
# f.write("using Java. \nI like programming in Java")
# f.close() 

# with open("practice.txt","r") as f:
#     data = f.read()
# new_data= data.replace("Java" ,"Python")
# print(new_data) 

# with open("practice.txt","w") as f:
#     f.write(new_data)
    
# word="learning"
# with open("practice.txt","r") as f:
#      data = f.read()
#      if(data.find(word) != -1):
#          print("Found")
#      else:
#          print("not found")          
# def check_for_word():
#     word="learning"
#     with open("practice.txt","r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#            print("Found")
#         else:
#            print("not found")
# check_for_word()       

 # WAF to find in which line of the file does the worrd "learning " occur first. print -1 if word     not found
     
# def check_for_line():
#     word= "learning"
#     data=True
#     line_no_1 = 1
#     with open ("practice.txt" , "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no_1)
#                 return
#             line_no_1 +=1
            
#     return -1
# print(check_for_line())  

#From a file   containig numbers separated by comma, print the count of even numbers.
count=0
with open("practice.txt","r") as f:
    data =f.read()
    print(data) 
    nus=data.split(",")
    for val in nus:
        if(int(val)%2==0):
            count+=1
print(count)              