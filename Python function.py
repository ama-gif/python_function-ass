#!/usr/bin/env python
# coding: utf-8

# # THEORY QUS

# 1. What is the difference between a function and a method in Python?
# 
#  Functions are independent blocks of code that can be called from anywhere, while methods are tied to objects or classes and need an object or class instance to be invoked

#  2. Explain the concept of function arguments and parameters in Python

# In Python, an argument is the value passed to a function when it's called. Fundamentally, parameters are the variables inside a function's parentheses.
# Arguments provide values for those parameters.

#  3. What are the different ways to define and call a function in Python

# define a function with the def keyword, then write the function identifier (name) followed by parentheses and a colon. 

# 4. What is the purpose of the `return` statement in a Python function

# python return statement is used to return the output from a function. We learned that we can also return a function from another function. Also, expressions are evaluated and then the result is returned from the function

#  5. What are iterators in Python and how do they differ from iterables?

# An Iterable is basically an object that any user can iterate over. An Iterator is also an object that helps a user in iterating over another object (that is iterable). We can generate an iterator when we pass the object to the iter() method. We use the __next__() method for iterating.

# 6. Explain the concept of generators in Python and how they are defined

# In Python, a generator is a function that returns an iterator that produces a sequence of values when iterated over. Generators are useful when we want to produce a large sequence of values, but we don't want to store all of them in memory at once.

# 7. What are the advantages of using generators over regular functions

# Advantages of using Generators
# Memory is saved as the items are produced when required, unlike normal Python functions. This fact becomes very important when you need to create a huge number of iterators. This is also considered as the biggest advantage of generators. Can be used to produce an infinite number of items.

#  8. What is a lambda function in Python and when is it typically used

# ambda functions are similar to user-defined functions but without a name. They're commonly referred to as anonymous functions. Lambda functions are efficient whenever you want to create a function that will only contain simple expressions – that is, expressions that are usually a single line of a statement.
# 

#  9. Explain the purpose and usage of the `map()` function in Python.

# Map in Python is a function that works as an iterator to return a result after applying a function to every item of an iterable (tuple, lists, etc.). It is used when you want to apply a single transformation function to all the iterable elements.

#  10. What is the difference between `map()`, `reduce()`, and `filter()` functions in Python?

# map() is used to apply a given function to each element of an iterable and returns a new iterable with the results. filter() is used to filter elements from an iterable based on a given condition or function and returns a new iterable with the filtered elements.

# # Practical Questions:

#  1. Write a Python function that takes a list of numbers as input and returns the sum of all even numbers in the list?
#     

# In[34]:


def sum_of_even_numbers(numbers):
    total = 0
    
    for num in numbers:
        if num % 2 == 0:
            # Add the even number to the total sum
            total += num
    
    return total


# In[35]:


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_of_even_numbers(numbers_list))


#  2. Create a Python function that accepts a string and returns the reverse of that string

# In[36]:


def reverse_string(input_string):
    # Reverse the string using slicing
    reversed_string = input_string[::-1]
    return reversed_string


# In[37]:


example_string = "Aman , Kumar"
print(reverse_string(example_string))


# 3. Implement a Python function that takes a list of integers and returns a new list containing the squares of 
# each number

# In[38]:


def square_numbers(numbers):
    squared_numbers = [num ** 2 for num in numbers]
    return squared_numbers


# In[39]:


numbers_list = [1, 2, 3, 4, 5]
print(square_numbers(numbers_list))


#  4. Write a Python function that checks if a given number is prime or not from 1 to 200.

# In[40]:


def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False

    return True


# In[41]:


for num in range(1, 201):
    print(f"{num} is prime: {is_prime(num)}")


#  5. Create an iterator class in Python that generates the Fibonacci sequence up to a specified number of 
# terms

#  6. Write a generator function in Python that yields the powers of 2 up to a given exponent

# In[42]:


def powers_of_2(max_exponent):
    for exponent in range(max_exponent + 1):
        yield 2 ** exponent


# In[43]:


for power in powers_of_2(10):
    print(power)


#  7. Implement a generator function that reads a file line by line and yields each line as a string.

# In[44]:


def read_file_line_by_line(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()


#  8. Use a lambda function in Python to sort a list of tuples based on the second element of each tuple.

# In[45]:


tuples_list = [(1, 'banana'), (2, 'apple'), (3, 'cherry'), (4, 'date')]


# In[46]:


sorted_tuples = sorted(tuples_list, key=lambda x: x[1])


# In[47]:


print(sorted_tuples)


# 9. Write a Python program that uses `map()` to convert a list of temperatures from Celsius to Fahrenheit.

# In[48]:


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


# In[49]:


celsius_temperatures = [0, 20, 37, 100]


# In[50]:


fahrenheit_temperatures = list(map(celsius_to_fahrenheit, celsius_temperatures))


# In[51]:


print(fahrenheit_temperatures)


#  10. Create a Python program that uses `filter()` to remove all the vowels from a given string

# In[52]:


def is_not_vowel(char):
    return char.lower() not in 'aeiou'
input_string = "This is an example string."
filtered_string = ''.join(filter(is_not_vowel, input_string))


# In[53]:


print(filtered_string)


# In[ ]:





# In[ ]:




