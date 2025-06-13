
#Write a program to add the elements of 2 arrays of same dimensions. (Hint: Use map method.)
#Example:
#Input:
#x = [1,2,3,4]
#y = [5,6,7,8]
#Output:
#z = [6,8,10,12]

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
z = list(map(lambda a, b: a + b, x, y))
print("z =", z)