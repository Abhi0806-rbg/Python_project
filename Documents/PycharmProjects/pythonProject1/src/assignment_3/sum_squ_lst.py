#Write a program to find the sum of squares of only the even numbers in the given list. (Hint:Use the methods filter, map, reduce.)
#Example:
#Input:
#lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Output:
#120
from functools import reduce

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = filter(lambda x: x % 2 == 0, lst)
squared_even_numbers = map(lambda x: x ** 2, even_numbers)
sum_of_squares = reduce(lambda x, y: x + y, squared_even_numbers)
print(sum_of_squares)