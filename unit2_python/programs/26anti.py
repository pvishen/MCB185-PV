# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'
dna_reverse_complement = ""


#more efficient if these are elifs
for i in range(len(dna)):
    currReverse = dna[len(dna)-1-i]
    if currReverse == "A":
        dna_reverse_complement = dna_reverse_complement + "T"
    if currReverse == "T":
        dna_reverse_complement = dna_reverse_complement + "A"
    if currReverse == "G":
        dna_reverse_complement = dna_reverse_complement + "C"
    if currReverse == "C":
        dna_reverse_complement = dna_reverse_complement + "G"

print(dna_reverse_complement)

"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
