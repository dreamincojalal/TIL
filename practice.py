# my_str = 'banana'

# #find
# print(my_str.find('a')) # 1
# print(my_str.find('z')) # -1

# #index
# print(my_str.index('a')) # 1
# print(my_str.index('z')) # error

#isalpha
# string1 = 'Hello'
# string2 = '123'
# print(string1.isalpha())
# print(string2.isalpha())

#isupper(), islower()
# string1 = 'Hello'
# string2 = 'HELLO'
# print(string1.islower()) # False
# print(string1.isupper()) # False
# print(string2.islower()) # False
# print(string2.isupper()) # True

#replace
#.replace(old, new[, count]) [,count] 선택인자임을 뜻함. 배커스 나우르 표기법

# #strip
# print(s.strip()) # 

# # #split
# # print(s.split())

# #'separator.join([iterable])
# a = [1, 3, 4, 6, 14, 3]
# b = list(reversed(a))
# print(b)

# a = [1,2,3,4]
# b = a

# b[0] = 100
# print(a)

# a = 100
# b = a
# b = 9

# print(a)
# print(b)

class Person:
    def __init__(self, name, age, email, number):
        self.name = name
        self.age = age
        self.email = email
        self.number = number
        
class Student(Person):
    def __init__(self, name, age, gpa, abc):
        super().__init__(name, age)
        self.gpa = gpa
        self.abc = abc
        
kkk = Student('aa', 20, 3.5, 'mola')
print(kkk)