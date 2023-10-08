# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list

import sys

# create a list keeping trrack of birthdays/calendars
# loop through the list and check 

days = float(sys.argv[1])
people = float(sys.argv[2])

pairs = (people * (people - 1))/2

prob_two_diff_birthday = (days - 1)/days

prob_all_diff_birthday = prob_two_diff_birthday ** pairs

prob_same_birthday = 1 - prob_all_diff_birthday

print(prob_same_birthday)

"""
python3 33birthday.py 365 23
0.571
"""

