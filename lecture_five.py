# i=1
# while i<=100:
#     print("jyoti")
#     i+=1

# print numbers from 1 to 100
# n=1
# while n<=100:
#       print(n)  
#       n+=1

#print numbers from 100 to 1
# i=100
# while i>0:
#     print(i)
#     i-=1

#print the multplication table of a number n
# n=int(input("Enter number:"))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1
    
#print the element of the following list using a loop
# num=[1,4,6,8,16,25,36,49,64,81,100]
# idx=0
# while idx < len(num):
#     print(num[idx])
#     idx+=1   
# num=[1,4,6,8,16,25,36,49,64,81,100]
# x=64
# i=0 #initialization
# while i<len(num):
#     if(num[i]==x):
#         print("FOUND at idx",i)
#     i+=1
    
# i=1
# while i<=5:
#     print(i)
#     if(i==3):
#         break
#     i+=1
        
# i=1
# while i<=5:
   
#     if(i==3):
#         i+=1
#         continue
#     print(i)
#     i+=1
            
# i=0
# while i<=10:
#     if(i%2==0):
#         print(i)
#     i+=1               
            
# i=0
# while i<=10:
#     if(i%2!=0):
#         print(i)
#     i+=1   
# nums=[1,2,3,4]
# for i in nums:
#     print(i) 
# str="apnacollege"
# for char in str:
#     print(char)  

#Print the element of the following list using a loop          
# list=[1,4,9,16,25,36,49,64,81,100]
# for i in list:
#     print(i)
#Search for a number x in this tuplr using loop
# tup=(1,4,9,16,25,36,49,64,81,100)
# x=25
# idx=0
# for i in tup:
#     if(i==x):
#         print('number found at idx',idx)
#     idx+=1    


# for i in range(2,100,2):  # start?,stop,step?
#     print(i)    

# for i in range(1,100,2):
#     print(i)  

#print numbers from 1 to 100
# for function

# for i in range (1,101):
#     print(i)   

# # print numbers from 100 to 1
# for i in range(100,1,-1):
#     print(i)
    
# print thw multiplication table of a  number n
# n=int(input("enter the number:"))
# for i in range(1,11):
#     print(n*i)   

#WAP to find the sum of first n b=number (using while)
# n=int(input("enter the number:"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print("total sum",sum)    

# n=int(input("enter the number:"))
# i=1
# sum=0
# while i<n:
#     sum+=i
#     i+=1
# print("total sum:",sum)   

n=int(input("enter the number:"))
fact=1
i=1
for i in range(1,n+1):
    fact*=i
    i+=1
print("fact of number:",fact)   

# n=int(input("enter the number:"))
# fact=1
# i=1
# while i<=n:
#     fact *= i 
#     i+=1
# print("factorial of n",fact)    
                     