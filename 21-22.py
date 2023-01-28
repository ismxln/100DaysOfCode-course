    # 21
# two_digit_number = input('Type 2 digit num: ') # 98
#
# first = int(two_digit_number[0])  # 9
# second = int(two_digit_number[1])  # 8
#
# print(first + second)  # 17
    # 22
""" PEMDAS: # order of execution
1. () 2. ** 3. * 4. / 5. + 6. -
"""
# weight = float(input('enter your weight: '))
# height = float(input('enter your height: '))
# bmi = weight / (height * height)
# print(bmi)

# how many days, weeks, month we have left if we live until 90 yo
age = int(input('What is your current age? '))

years_remaining = 90 - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f'You have {years_remaining} years or {months_remaining} months or {weeks_remaining} weeks or {days_remaining}'
      f' days, to reach 90years old')