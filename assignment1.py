# Ques1) How do lists and tuples differ in terms of mutability and performance.When would you choose one over the other.
# Ans)Difference Between Lists and Tuples:
# Mutability:

# List: A list is mutable, meaning you can modify its elements, add new elements, or remove existing ones. For example, you can change the value of a list element or append new elements.
# Tuple: A tuple is immutable, meaning once it's created, you cannot modify it. You can't change, add, or remove elements after creation.
# Performance:

# List: Lists generally have more overhead in terms of performance due to their mutability. They consume more memory and are slower in comparison to tuples for operations that don't involve modification (like iteration).
# Tuple: Since tuples are immutable, they are usually faster and require less memory than lists. This makes tuples more efficient when you don't need to modify the data.
# Use Cases:

# List: You would choose a list when you need to modify the collection (add, remove, or change elements). Lists are ideal for dynamic data where the size or content might change over time.
# Tuple: You would choose a tuple when you need an unchangeable collection of data. Tuples are better suited for fixed collections of items, like storing coordinates, function return values, or keys for dictionaries.
# When to Choose One Over the Other:
# Choose a list when:

# You need a collection that can grow or shrink dynamically.
# You want to perform operations like append, remove, or change elements.
# Performance is not as critical, and flexibility is more important.
# Choose a tuple when:

# You need a collection that will not be modified.
# You want to use the data as a key in a dictionary (since tuples are hashable, while lists are not).
# You want better performance and memory efficiency.

# Ques2)Explain how Pythgon handles conversion between different data types,such as between integers and floats or between strings and lists.
# Ans)1. Converting Between Integers and Floats:
a = 5    # int
b = 2.0  # float
result = a + b  
print(result)  

#Float to Integer:
a = 5.75  # float
b = int(a)  
print(b)  

#2. Converting Between Strings and Numbers (Integers/Floats):
#String to Integer or Float
s1 = "123"
num1 = int(s1)  # string to integer
print(num1)  

s2 = "45.67"
num2 = float(s2)  # string to float
print(num2)  

#Integer or Float to String
num = 456
str_num = str(num)  # integer to string
print(str_num)  

f_num = 3.14
str_f_num = str(f_num)  # float to string
print(str_f_num) 

#3. Converting Between Strings and Lists:
#String to List
s = "hello"
list_s = list(s)  # converts string to list of characters
print(list_s)

#List to String
lst = ['h', 'e', 'l', 'l', 'o']
str_lst = ''.join(lst)  # converts list of characters to a string
print(str_lst)  



#Ques3)Take a number and use the +=operator to increase its value by 10.
a = 15
a += 10
print(a) 

#Ques4)Write a Python program to check if a given year is a leap year or not.
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


#Ques5)Write a program that asks the user to enter their marks and displays their grades:
#90-100:A
#80-89:B
#70-79:C
#60-69:D
#BElow 60:F
def calculate_grade(marks):
    if 90 <= marks <= 100:
        return "A"
    elif 80 <= marks <= 89:
        return "B"
    elif 70 <= marks <= 79:
        return "C"
    elif 60 <= marks <= 69:
        return "D"
    else:
        return "F"
marks = float(input("Enter your marks: "))
if 0 <= marks <= 100:
    grade = calculate_grade(marks)
    print(f"Your grade is: {grade}")
else:
    print("Invalid marks entered. Please enter a number between 0 and 100.")
