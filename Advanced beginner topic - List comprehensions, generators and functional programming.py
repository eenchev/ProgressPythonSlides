
# coding: utf-8

# List Comprehensions
# --------------------------------------------------------------------------------
# 
# You know for loops, right?
# 
# ```python
# list_values = []
# for x in range(10):
#     list_values.append(x*2)
# print(list_values)
# ```
# Using python syntax (syntactic sugar), the previous expression can be flattened to:
# 
# ```python
# list_values = [x*2 for x in range(10)]
# ```
# Here is an example which keeps only the even numbers from a list:
# 
# ```python
# even = [x for x in list_values if x % 2 == 0]
# ```

# # Understanding Generator Expressions (Generators)
# --------------------------------------------------------------------------------
# 
# ![](https://dbader-static-defugurjmqrkjo.netdna-ssl.com/figures/python-generator-expressions.jpg)

# # In-memory vs Lazy
# -----------------------------------------------------------------------------
# * Many functions in Python use or generate in-memory lists for iteration.  This is fine for relatively small list, but for large lists it becomes a problem.
# * List expressions are all created at once and kept in memory.
# 
# ```python
# >>>import sys 
# >>>sys.getsizeof([x for x in range(0,1000000)])
# >>>4348736
# ```
# 
# * 4+ MegaBytes of memory just for this. And what if we don't need it all at once?
# 

# # Laaaazy
# ---------------------------------------------------------------------------------
# 
# * Lazy Lists
# 
# > A lazy list is when the next item is supplied when needed, and not before.  If we stop processing before reaching the end of the list then those unused items will never be generated or use up resources. It is also possible to run an endless list. Lazy lists are implemented by supplying an iterator to the list, rather than the whole list itself.
# 
# ```python
# def simp():
#     yield 10
#     yield 20
#     yield 30
#  
# it=simp()
# print(next(it)) # print(it.next()) would be the Python 2 syntax
# print(next(it)) # 20
# print(next(it)) # 30
# ```

# # Careful! Don't iterate over the generator itself
# ----------------------------------------------------------------
# 
# ```python
# def simp():
#     yield 10
#     yield 20
#     yield 30
#  
# simp()
# print(next(simp())) # print(it.next()) would be the Python 2 syntax
# print(next(simp())) # 10
# print(next(simp())) # 10
# ```

# # Generator for a list
# ------------------------------------------------------------------------------------------------
# We can use the generator like a list object:
#     
# ```python
# for item in simp():
#     print(item)
# ```
# 
# Here's some code returning a list without generator:
# ```python
# def nogen(num):
#     res=[]
#     i=0
#     while i<num:
#         i+=1
#         res.append(i)
#     return res
#  
# s=nogen(10);
# print (s)
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]
#  
# for i in nogen(5):
#    print(i)
# ```
# Try to implement it with now.

# # Generator for a list cont.
# -------------------------------------------------------------------------------------------
# 
# Solution:
# 
# ```python
# def withgen(num):
#     i=0;
#     while i<num:
#         i+=1
#         yield i
#  
# s=withgen(10);
# print (s)
# # <generator object withgen at 0x1093786e0>
#  
# for i in s:
#     print(i)
# ```
# 

# # Implementing an endless sequence
# -----------------------------------------------------------------------
# 
# ```python
# def simp():
#     num = 0;
#     while True: # endless loop
#         num+=10
#         yield num
#  
# it=simp()
# print(it.next()) # 10
# print(it.next()) # 20
# print(it.next()) # 30
# ```
# 
# Sometimes we receive data from a stream and want to handle it like a sequence , with generator its easy. You can replace yielding a number with a function that receives a message from a network socket or a queue and return it etc.

# # Factorial
# ----------------------------------------------------------
# 
# ```python
# def factorial(n):
#     first = 1
#     next = 1
#     while first <= n :
#        yield next
#        first = first + 1
#        next = next * first
#        
# gen = factorial(100)
# for i in gen:
#     print(i)
# ```

# # Fibonacci number generator
# --------------------------------------------------------
# 
# ```python
# def fib():
#     a, b = 0, 1
#     while 1:
#         yield a
#         a, b = b, a + b
# ```
# 
# TODO for homework : try to implement a Prime numbers generator

# # Generator expressions
# ------------------------------------------------------------
# Check this out. Looks like a list expression with a small difference, right?
# 
# ```python
# generator = ('Hello' for i in range(0,1000))
# ```
# 
# It is called a generator expression. Check the size in memory of our generator and the corresponding llist comprehension.

# # Exhausting generators
# -----------------------------------------
# 
# ```python
# def generator():
#     yield 10
#     
# gen = generator()
# print(next(gen))
# print(next(gen))
# ```
# 
# How should we handle **StopIteration** error?

# # Functional programming
# -----------------------------------------------------------
# 
# ![](http://www.foxydatascience.com/uploads/7/4/5/8/74585969/fun-prog_orig.jpg)

# > Functional programming is a paradigm which concentrates on computing results rather than on performing actions.  That is, when you call a function, the only significant effect that the function has is usually to compute a value and return it. 
# 
# Until now we concentrated on the imperative style of programming e.g. describing the actions which need to be executed in an order to process the input and get the desired output.

# # map()
# -----------------------------------------------------------
# 
# Map takes a function and a list of items. It makes a new, empty list, runs the function on each item in the original list and inserts each return value into the new list. It returns the new list.
# 
# 
# ```python
# name_lengths = map(len, ["Alice", "Bob", "Mary"])
# ```
# 
# * Try to implement a map expression which multiplies a list by two. Can't? Let me explain about lambda functions.
# 
# * Okay now create a fahrenheit to celsius converter using map().

# # filter()
# ------------------------------------------------------------------------
# 
# Filter extracts each element in the sequence for which the function returns True.
# Sample filter function which checks if numbers in a list are even:
# ```python
# filter(lambda x: x%2==0, [3,4,2,7])
# ```
# 
# * Filter only the non-negative values from a list of integers.
# 
# * Now filter only the elements from list A which are present in some list B, too.(Find the intersection between the two lists)

# # reduce()
# ----------------------------------------------------------------------------------
# 
# * Warning! From Python 3.0 is part of functools library and must be imported first.
# 
# It accepts an iterator to process, but it's not an iterator itself. It returns a single result.
# 
# ```python
# reduce( (lambda x, y: x * y), [1, 2, 3, 4] )
# ```
# 
# At each step, reduce passes the current product or division, along with the next item from the list, to the passed-in lambda function. By default, the first item in the sequence initialized the starting value. 
# 
# * Concatenate of list of strings using reduce.
