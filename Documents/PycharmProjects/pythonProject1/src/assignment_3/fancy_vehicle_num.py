#Write a program to generate a fancy number for a new vehicle considering the following
#restraints:
#1)a. b. c. d. The fancy number should have 4-digits.
#2)The sum of these 4-digits should be 12.
#3)The 3rd digit should be equal to the difference between the 1st and the 2nd digit.
#4)The 4tth digit should be equal to the sum of the 1st and the 3rd digit.
#5)The program should print all the fancy numbers that satisfy these conditions.

def generate_fancy_numbers():
    fancy_numbers = []

    for i in range(1000, 10000):
        digits = [int(d) for d in str(i)]

        if sum(digits) == 12 and \
                digits[2] == abs(digits[0] - digits[1]) and \
                digits[3] == (digits[0] + digits[2]):
            fancy_numbers.append(i)

    return fancy_numbers

print("Fancy Vehicle Numbers that satisfy all constraints:")
print(generate_fancy_numbers())