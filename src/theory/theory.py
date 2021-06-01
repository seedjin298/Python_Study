# import math # importing everything
# from math import ceil, fsum # import only what you use
# from math import fsum as sexy_sum # can change name
from calculator import plus, minus # can import from other file

# Theory

# #1.0 Data Types of Python
# # super_long_variable: use _  
# # for javascript it was superLongVariable but for python use _
# a_string = "like this" # string
# a_int = 3 # int
# a_float = 3.12 # float
# a_boolean = True # True = 1, False = 0, must be uppercase: ture false (x)
# a_none = None # nothing, not true not false just nothing

# print(type(a_float))

# #1.1 Lists in Python
# days = ["Mon", "Tue", "Wed", "Thur", "Fri"]

# # print(type(days))

# # look at common, mutable(list is mutable) of
# # https://docs.python.org/3/library/stdtypes.html#list
# print("Mon" in days)

# #1.2 Tuples and Dicts
# # tuples is immutable, so there is only common
# # days = ("Mon", "Tue", "Wed", "Thur", "Fri")

# # print(type(days))

# # dictionary
# nico = {
#     "name": "Nico",
#     "age": 29,
#     "korean": True,
#     "fav_food": ["Kimchi", "Sashimi"]
# }

# # print(type(nico))
# # print(nico["fav_food"])
# print(nico)
# nico["handsome"] = True
# print(nico)

# #1.3 Built in Functions
# print(len("awhefuuiawefah"))

# age = "18"
# print(type(age))
# n_age = int(age)
# print(type(n_age))
# print(n_age)

#1.4 Creating a Your First Python Function
# def say_hello(): # python works with space/tabs not {}
#     print("hello") 
#     print("bye")

# say_hello() # say_hello: button, (): pressing the button
# say_hello()
# say_hello()
# say_hello()

# #1.5 Function Arguments
# # def say_hello(who): # who: argument
# #     print("hello", who)

# # say_hello("Nicolas")

# def plus(a, b=0): 
#     #b=0: b default value is 0, if b is not given b will be defined 0
#     print(a + b)

# def minus(a, b=0):
#     print(a - b)

# plus(2, 5)
# minus(2) # gets error if default value not defined
# minus(2, 5)

#1.6 Returns
# #if you want to save the result use return
# def p_plus(a, b):
#     print(a + b)

# def r_plus(a, b):
#     return a + b
#     # print("aefawf awfaw") # code after return doesnt get executed, function ends after return

# p_result = p_plus(2, 3) # prints 5 here, nothing gets saved at p_result
# r_result = r_plus(2, 3) # returns 5 here -> r_result = 5 

# print(p_result, r_result)

# #1.7 Keyworded Arguments
# # useful if you forgot the order of the argument but know the name of argument
# # def plus(a, b):
# #     return a - b

# # result = plus(b=30, a=1) 
# # print(result)

# def say_hello(name, age):
#     return f"Hello {name} you are {age} years old"
#     # "Hello " + name + " you are " + age + " years old"

# # hello = say_hello("nico", "12")
# hello = say_hello(age="12", name="nico")
# print(hello)

# #1.8 Code Challenge!
# def plus(a, b):
#     return a + b
# try:
#     test = plus(10, 1.1)
#     print(test)
# except:
#     print("Enter a number")

# #1.9 Conditionals part One
# def plus(a, b):
#     if type(b) is int or type(b) is float:
#         return a + b
#     else:
#         return None

# plus(12, 1.2)

# #1.10 if else and or
# def age_check(age):
#     print(f"you are {age}")
#     if age < 18:
#         print("you cant drink")
#     elif age == 18 or age == 19:
#         print("you are new to this!")
#     elif age > 20 and age < 25:
#         print("you are still kind of young")
#     else:
#         print("enjoy your drink")

# age_check(18)

# #1.11 for in
# days = ("Mon", "Tue", "Wed", "Thur", "Fri")

# # for day in [1, 2, 3, 4, 5]:
# #     print(day)

# for day in days:
#     if day is "Wed":
#         break
#     else:
#         print(day)

# for letter in "Nicolas":
#     print(letter)

#1.12 Modules
# import math at the top

# #for import math
# print(math.ceil(1.2))
# print(math.fsum(-1.2))

# #for from math import ceil, fsum
# print(ceil(1.2))
# print(fsum([1,2,3,4,5,6,7]))

# #for math import fsum as sexy_sum
# print(sexy_sum([1,2,3,4,5,6,7]))

#for from calculator import plus
print(plus(1,2), minus(1,2))