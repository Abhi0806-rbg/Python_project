
#Write a program to get the vowels and their count in the given string. (Hint: Use filter method.


def get_vowels_and_count(input_string):
	vowels = 'aeiou'
	filtered_vowels = list(filter(lambda char: char in vowels, input_string.lower()))
	return filtered_vowels, len(filtered_vowels)
input_string = "quintessential"
vowels, count = get_vowels_and_count(input_string)
print(vowels, count)