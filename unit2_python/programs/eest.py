
dna = 'ATGGCCTTT'

for frame in range(3):
	for position in range(frame, len(dna) -2, 3):
		codon = dna[position:position+3]
		if codon == 'ATG':
			print(f'start codon at {position+1} in frame {frame+1}')
		elif codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
			print(f'stop codon at {position+1} in frame {frame+1}')
