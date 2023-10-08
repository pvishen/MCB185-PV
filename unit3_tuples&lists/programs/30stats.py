# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

import sys

num_list = []

for val in sys.argv[1:]:
        val = float(val)
        num_list.append(val)

num_list.sort()
minimum = num_list[0]
maximum = num_list[-1]
mean = sum(num_list)/len(num_list)

'''
minimum = num_list[0]
maximum = num_list[0]

for val in num_list[1:]:
        if val < minimum:
                minimum = val
        if val > maximum:
                maximum = val

'''


print(num_list)


if len(list) % 2 == 1:
        median = list[len(list)//2]


print("Count:", len(num_list))
print("Minimum:")
print("Maximum:")
print("Mean:", mean)
print("Std. dev:")
print("Median:")


"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
