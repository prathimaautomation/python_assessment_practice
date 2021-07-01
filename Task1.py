# Task 1: Declare a functioon called username that takes one argument as a string and return the name

# def username(name):
#     return name;
#
# print(username("Prathima"))

#Task 2: Declare a list with number 1 to 5, iterate through the list and display the list

# ls = [1, 2 ,3, 4, 5]
#
# for i in ls:
#     print(i)

# #Task 3: Create AND - && and ==, which one returns a bool value?
#
# name = "Prathima"
# if name == "Prathima": # == returns bool value and is a keywork
#     print(name)
#
# #Task 4: What is the difference between a list and a tuple
#
# # A tuple immutable {} & list is mutable, uses [], can use different types(int, string, bool)
#
# # Task 5:Can we add an element to a list? Ans: Yes
#  # Can we add an element to a tuple? Ans: No
#  #Can the element of a tuple be different types? Ans: Yes
#
# # Task 6: Create a dictionary with key value firstname and lastname
# dictionary = {
#     "firstname": "Prathima",
#     "lastname": "Joginipelly"
#         }
# #
# # print(type(dictionary))
#
# # Task 7: Let's append to the course & DevOps to the above dictionary
# dictionary["course"] ="DevOps"
# print(dictionary)

# Task 8: Create a class called student, initialise class and create an object of the class
# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     def greeting(self):
#         print("Hello", self.name)
#
# s = Student("Prathima")
# s.greeting()

# Task 9: Create two functions that take two arguments each. function1 called add_values() & function2 called subtract_values() and return the addition and subtraction
# def add_values(num1, num2):
#     return num1 + num2
#
# def subtract_values(num1, num2):
#     return num1 - num2
#
# print(add_values(2, 4))
# print(subtract_values(5, 2))

# Task 10: Declare a dictionary with 3 shopping items with cost, eggs is 1.20, milk is 2.30, bread is 1.00
# Write a function that return the total value

# shopping_items ={
#     "eggs": 1.20,
#     "milk": 2.30,
#     "bread": 1.00
#     }
#
# def total_value():
#     total = 0
#     for i in shopping_items.values():
#         total += i
#     return total
#
# print(total_value())

# #Task 11: Prompt the user to enter an integer, declare a function that checks if the number is odd or even. Display back to the user with the message "the number you chose is odd/even"
#
# # user_input = input("Please enter any number: ")
# #
# # def check_odd_even(number):
# #     if number % 2 == 0:
# #         return "even"
# #     else:
# #         return "odd"
# #
# # print("The number you chose is " + check_odd_even(user_input))
#
# #Task 12: select the correct syntax-
# #1 -super.__init().
# # 2- super()__init().
# # 3 super().__init().
# # 4 - Super().__init__()
#
# #Task 13: Declare a tuple with three values and iterate through the tuple and display the values, then delete last index
#
# # tuple1 = {"apple" , 6, True}
# # for item in tuple1:
# #     print(item)
#
# #Task 14: Create a class called Student with one method called student_data that method return student_name, create an object called devops_student and inherit Student class inside devops_student and print student name
#
# # class Student:
# #
# #     def student_data(self):
# #         return "Prathima"
# #
# # class Devops_Student(Student):
# #     def __init__(self):
# #         super().__init__()
# #
# # s = Devops_Student()
# # print(s.student_data())
#
# #Task 15: Declare a variable called city, declare a method that takes city as an argument and value of the city as London and method checks if value is london then return true if city is not London false
#
# city = "London"
#
# def check_cityname(cityname):
#     if cityname == "London":
#         return True
#     else:
#         return False
#
# print(check_cityname(city))
#
###Task 16: import sys module, import math, print random method. Create a function that takes two arguments, calculates the percentage of these arguments
import sys
import math
import random

print(random.randint(0, 25))

def percentage(num1, num2):
    return (num1 / num2) *100

print(percentage(5, 10))










