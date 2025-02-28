#Write a function pascals_triangle(rows) that prints the first rows of 
# Pascal’s Triangle using nested for loops.
# pascals_triangle(5) 
# Output:
#  1
#  1 1
#  1 2 1
# 1 3 3 1
# 1 4 6 4 1
def pascals_triangle(rows):
    for i in range(rows):
        number = 1
        for j in range(i + 1):
            print(number, end=" ")
            number = number * (i - j) // (j + 1)  
        print()
pascals_triangle(5)


# 2. Explain how the continue statement works in a loop. What are some 
# scenarios where using continue is more beneficial than restructuring 
# the loop?
# - Coding Challenge: Write a Python program that iterates through a list 
# of numbers and prints only those numbers that are divisible by 3, using 
# the continue statement.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 3 != 0:
        continue  # Skip the rest of the loop if num is not divisible by 3
    print(num)


#3. Use list comprehension to generate all Pythagorean triplets (a, b, c) 
#where a² + b² = c² and a, b, c ≤ 50.
triplets = [(a, b, c) for a in range(1, 51) for b in range(a, 51) for c in range(b, 51) if a**2 + b**2 == c**2]
print(triplets)


#4. Write a function max_consecutive_sum(nums, k) that finds the 
#maximum sum of k consecutive elements in a list.
def max_consecutive_sum(nums, k):
    max_sum = float('-inf')  
    for i in range(len(nums) - k + 1):
        current_sum = sum(nums[i:i + k])
        max_sum = max(max_sum, current_sum)
    return max_sum
nums = [2, 1, 5, 1, 3, 2]
k = 3
print(max_consecutive_sum(nums, k)) 


# 5. Write a function that takes a list as an argument and modifies it by 
# appending a new item. Demonstrate how changes to the list inside the 
# function affect the list outside the function.
def append_item(lst, item):
    lst.append(item)
my_list = [1, 2, 3]
append_item(my_list, 4)
print(my_list)  


#6.Take a number as input and print the Fibonacci sequence up to that 
#many terms using User-defined functions.
def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
num_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))
fibonacci_sequence(num_terms)
