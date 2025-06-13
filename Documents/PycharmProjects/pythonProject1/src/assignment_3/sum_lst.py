#Write a program to find the sum of the given elements of the list. (Hint: Use reduce method.)
#Example:
#Input:
#lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Output:
#res_sum = 45

from functools import reduce


def sum_of_elements(lst):
	res_sum = reduce(lambda x, y: x + y, lst)
	return res_sum
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res_sum = sum_of_elements(lst)

print("res_sum =", res_sum)