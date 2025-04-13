# def calc_sum(a,b):
#     sum=a+b
#     print(sum)
#     return sum
# calc_sum(2,4)
# calc_sum(12,17)
# calc_sum(6,7)

#OR
#function definition
# def calc_sum(a,b):#parameters
#     return a+b

# sum=calc_sum(178,278)#function call; arguments
# print(sum)

# def print_hello():
#     print("hello")
    
# print_hello()  
# def print_hello():
#     print("hello")
    
# sum=print_hello()
# print(sum)

#average of numbers
# def calc_avg(a,b,c):
#     sum=a+b+c
#     avg=sum/3
#     print(avg)
#     return avg
# calc_avg(3,4,5)

# def calc_num(a=1,b=8):
#     print(a*b)
#     return a*b
# calc_num()

# WAF to print the length of a list(list is a parameter)
# cities=["delhi","noida","bangluro","pune"]
# heros=["salman khan","sharukh khan","shushant singh rajput","rajkumar"]
# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heros)  

#WAF to print the element of a list in single line(list is the parameter)
# name=["jyoti","kshamta","pallavi","kavita","priyanka","laxmi"]
# def print_list(list):
#     for i in list:
#         print(i,end=" ")
         
# print_list(name)   


 
# def cal_fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)
        
# cal_fact(5)    

#WAF to convert USD to INR
# def converter(usd_val):
#     inr_val = usd_val *83
#     print(usd_val , "USD =" , inr_val, "INR")
# converter (100)   

# n=int(input("En ter the number:"))
# def func_num(n):
#     if(n%2==0):
#         print("EVEN")
#     else:
#         print("ODD")
# func_num(n) 

# RECURSION
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(5)     

# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     return fact(n-1)*n
# print(fact(4))            
       
# Write a recursive funciton to calculate the sum of first n natural numbers
# def natural(n):
#     if(n==0):
#         return 0
#     return natural(n-1)+n
# sum=natural(4)
# print(sum) 

# write a recursive function to print all element in a list
# def print_list(list, idx=0):
#     if(idx == len(list)):
#         return 
#     print(list[idx])
#     print_list(list,idx+1)
# fruits = ["mango","litchi","banana","apple","pineapple"]     
# print_list(fruits) 
               
               