"""
Group 8
CSC 256
Prof. Tonya Melvin-Bryant
Lab Intro: Full Retirement Age

Using the Full Retirement Age information at Social Security Administration, this program:
asks the user for a birth year and month,
displays the age (with additional months) for obtaining full SSA benefits
displays the year and month for obtaining full SSA benefits
"""


import sys
from retirement import *


def main():
    print('Social Security Full Retirement Age Calculator')
    x = 0
    while x == 0:
        try:
            birth_year = int(input('Enter the year of birth or Enter to exit:'))
            birth_month = int(input('Enter Birth Month as a number:'))
        except ValueError:
            sys.exit()
        retirement_age_year, retirement_age_month = calculate_retirement_age(birth_year)
        retirement_date_year, retirement_date_month = calculate_retirement_date(birth_year, birth_month, retirement_age_year, retirement_age_month)
        month = {1: 'January',
                 2: 'February',
                 3: 'March',
                 4: 'April',
                 5: 'May',
                 6: 'June',
                 7: 'July',
                 8: 'August',
                 9: 'September',
                 10: 'October',
                 11: 'November',
                 12: 'December'}
        print('Your full retirement age is ' + str(retirement_age_year) + ' and ' + str(retirement_age_month) + ' months.')
        print("This will be in {} of {}\n".format(month[retirement_date_month], retirement_date_year))


if __name__ == "__main__":
    main()
