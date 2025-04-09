#Problem 1

your_Name = input('Enter Your Name: ')
print('Hello, ' + your_Name)

your_Age = input('Enter Your Age: ')
print('You are'  + your_Age)

your_Name = "Your Name"   #String
your_Name_type = type(your_Name)
print(your_Name_type)

your_Age = "Your Age"     #String
your_Age_type = type(your_Age)
print(your_Age_type)

#Problem 2

first_number = input ('Enter First Number: ')
second_number = input ('Enter Second Number: ')

first_number = int(first_number)
second_number = int(second_number)

if first_number > second_number:
    print("The first number is larger")
elif first_number < second_number:
    print("The second number is larger")
else:
    print("Both numbers are equal")

#Problem 3

favorite_color = input ('Enter your favorite color: ')
favorite_color_type = type(favorite_color)
print('Your favorite color is '  + favorite_color)
print(favorite_color_type)

#Problem 4

first_number_2 = input('Enter a decimal number ')
first_number_2 = float(first_number_2)
first_number_2_type = type(first_number_2)
print('Your decimal number is '  + str(first_number_2))
print(first_number_2_type)

#Problem 5

full_Name = input ('Enter your full name ')
name_Length = len(full_Name)
name_Length_type = type(name_Length)
print('The length of your name is ' + str(name_Length))
print(name_Length_type)




