# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers


"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
import random
#random.seed(0)

bases = "ATCG"
dna= ""
atNum = 0


for i in range(30):
    dna = dna + random.choice(bases)
    if random.choice(bases) == "A" or random.choice(bases) == "T":
        atNum = atNum+1
    i += 1
    

atPercent = atNum/len(dna)

print(len(dna), atPercent, dna)

