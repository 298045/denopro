# class Student:
#     name="jyoti"
# s1 = Student()
# print(s1.name)  

# s2=Student()
# print(s2.name) 

# class car:
#     color="blue"
#     brand="mercedes"
# car1 = car()
# print(car1.color)    
# print(car1.brand)

# class Student:
#     name="jyoti"
#     def __init__(self ):
#         print(self)
#         print("adding new student in database..")
        
# s1 = Student()
# print(s1.name) 

class Student:
    
    def __init__(self , fullname ):
        self.name = fullname
        print("adding new student in database..")
        
s1 = Student("jyoti")
print( s1.name) 

s2 = Student ("kittu")
print(s2.name)