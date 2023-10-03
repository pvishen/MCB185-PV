# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'

gcNum = 0

for i in range(len(dna)):
    if dna[i] ==  "G" or dna[i] == "C":
        gcNum = gcNum +1

gcPercent  = gcNum/len(dna)
print(f'{gcPercent:.2f}')

"""
python3 24gc.py
0.42
"""
