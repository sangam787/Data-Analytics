# _________________________________________________________________________________________________________________________________________________________
#Question-1 Explain the key features of Python that make it a popular choice for programming.
"""
Answer-1
Python is the one of the most popular programming language. 
Below, its some key feature described, why it is popular.

1-Python is easiest programing language, it is very easy to read and understand. Its syntax are very simple similar like english words.
2-Python has one of the largest collections of free libraries.
3-Python is free to use. We can download and modify.
4-Python is designed around classes and object, which allows for reusable code.
5-Python is a High Level Language.
6-Python is portable and integrated programing language. 
"""
# _________________________________________________________________________________________________
#Question-2 Describe the role of predefined keywords in Python and provide examples of how they are used in a program.

"""
Answer-2
There are a set of keywords that are reserved words in Python. These words can not be used as variable names, function names, or any other identifiers.
The role of predefined keywords are for working on programs that have a specific meaning.
Now we are going to describe the keywords and their roles with examples.
(1)- and (A logical operator):- Return True if both statements are True:
example-
""" 
# x = (3 < 7 and 5 < 8)
# print(x)


"(2)- elif (Used in conditional statements, same as else if)"
# light = input("enter color name: ")
# if light == "red":
#     print("stop")
# elif light == "green":
#     print("go")
# elif light == "yellow":
#     print("wait")

"""
(3)- True (The True keyword is a Boolean value, and result of a comparison operation.
Print the result of the comparison "7 is larger than 6":
"""
# print(7 > 6)
# The True keyword is the same as 1 (False is the same as 0).

"""
(4)- False (The False keyword is a Boolean value, and result of a comparison operation.
Print the result of the comparison "5 is larger than 6"
"""
# print(5 > 6)
# The False keyword is the same as 0 (True is the same as 1).

"""
(5)- For (The for keyword is used to create a for loop.)
Example
Loop through all items in a list:
"""
# fruits = ["apple", "banana", "mango"]

# for x in fruits:
#   print(x)


"(6)- while (The while keyword is used to create a while loop. A while loop will continue until the statement is false.)"

# x = 0

# while x < 5:
#   print(x)
#   x += 1
  
"""
(7)- None (The None keyword is used to define a null value, or no value at all.)
example
"""
# x = None
# print(x)

"""
(8)- If (The if keyword is used to create conditional statements (if statements), 
and allows you to execute a block of code only if a condition is True.)
example
"""
# x = 5
# if x > 4:
#   print("YES")

"""
(9)- not (The not keyword is a logical operator.

The return value will be True if the statement(s) are not True, otherwise it will return False.)
example
"""
# x = False

# print(not x)

"""
(10)- or 
The or keyword is a logical operator.
Logical operators are used to combine conditional statements.
The return value will be True if one of the statements return True, otherwise it will return False.
example
"""
# x = (5 > 3 or 5 > 10)

# print(x)

"Thus, there are more keywords which are used in Python."

# ____________________________________________________________________________________________________________________________
#Question-3 Compare and contrast mutable and immutable objects in Python with examples.
"""
Answer:-3
In Python, An object that can be modified is called a mutable object and this process is mutability. And the object that can not be modified is called immutable, this process is called immutability.
Example of mutable objects:-
"""
"(1) Lists :- We can add, remove, or modify elements within a list after it's created."

# my_list = [1, 2, 3]
# my_list.append(4)  # Now my_list is [1, 2, 3, 4]
# print(my_list)

"(2) Sets :- Elements can be added or removed from a set."
# setA = {1, 2, 3}
# setA.add(4)  # Now setA is {1, 2, 3, 4}
# print(setA)

"Example of immutable objects:-"

"""
(1) Strings: Once a string is created, individual characters cannot be directly changed."""
# strA = "Good"
# strA[0] = "h"  # This will throw an error

# (2) Tuples: Tuples are like lists but cannot be modified after creation. 
# tupA = (1, 2, 3)

# tupA[0] = 5  # This will raise an error



#_________________________________________________________________________________________________________________________________________________________

#Question-4 Discuss the different types of operators in Python and provide examples of how they are used.
"""
Answer-4
An operator is a symbol that performs a certain operation between operands.
There are different types of operators in Python.

(1):- Arithmetic Operators (+, -, *, /, %, **)
Arithmetic Operators generally used to perform on mathematical operations.
For Example :- 
"""
# a = 5
# b = 4
# print(a + b)   # similarly we can use others Arithmetic Operators in place of "+" 

"""
(2):- Relational Operators (==, !=, >, <, >=, <=)
this operator is used for comparison of two values
For Example :-
"""
# a = 5                
# b = 4               # In relational operators we get answer in boolean data tpye, that is 'True' or 'False'.
# print(a == b)       # similarly we can use others Relational Operators in place of "==" .
                  
"""
(3):- Assignment Operators (=, +=, -=, /=, %=, **=)      
In Assignment Operators we assign the values to the variables.
For Example :-
"""
# a = 5
# a += 5 
# print(a)    # similarly we can use others Assignment Operators in place of "= or +=" .

"""
(4):- Logical Operators ( not , and , or )
Logical operators works on boolean values.
(a)-Not operator:- we use 'not' for find opposite values
example:- 
"""
# a = 5
# b = 4
# print(not(a > b))

"""
(b)-And operator:- In 'And Operator' we get true value only both values are true.
example:-
"""
# a = True
# b = False
# print(a and b)

"(c)-Or Operators:- In 'Or Operator' we get true value if any one value is true."
# a = True
# b = False
# print(a or b)

"""
(5):- Identity operators ( is ,  is not)
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
'is' operator:- Returns True if both variables are the same object
example
"""
# a = 20-10
# b = 5+5
# print(a is b)  # similarly we can use 'is not'


# ___________________________________________________________________________________________________________________________
#Question-5 Explain the concept of type casting in Python with examples.

"""
Answer-5
When we convert one data type into another data type, then this process is called type casting.
for example
a = "4"    
b = 5       
if we print(a + b) then it will throw an error. So for solution we convert the data type of a 
"""
# a = int("4")
# b = 5
# print(a + b)   # now we will find the answer.


# _________________________________________________________________________________________________________________________________________
#Question-6 How do conditional statements work in Python? Illustrate with examples.

"""
Answer-6
The most common conditional statements in Python are if , elif , and else . We use conditional statements to execute a specific block of code that is based on truth values of conditions. 

 'if' condition
"""
# a = 50     
# b = 100
# if b > a:       # Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. 
#   print("b is greater than a")

# a = 50
# b = 100
# if b > a:       # if we don't use indentation then we will get an error             
# print("b is greater than a") # we will get an error


#  'elif' condition
# a = 50
# b = 50
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")

# 'else' condition
# a = 100
# b = 50
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")


# ____________________________________________________________________________________________________________________
#Question-7 Describe the different types of loops in Python and their use cases with examples.

"""
Answer-7
There are mainly two tpyes of loops.
1. While Loops     2. For Loops
(1) While Loops:-
The while loop is used to execute a set of statements as long as a condition is true.
for example
"""
# i = 1          # if we want to print number series so we can use while loop. in this example we took a variable 'i'. 
# while i < 6:   # whose value is 1, now we can set limit how many numbers we want, here we set 5. 
#   print(i)     # now we can print(i) with 'updation' like i += 1
#   i += 1

"""
(2) For Loops:-
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
for example
"""
# list = [1, 2, 3, 4, 5]
# for num in list:
#     print(num)



