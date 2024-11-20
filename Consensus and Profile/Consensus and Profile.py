# A: 5 1 0 0 5 5 0 0
# C: 0 0 1 4 2 0 6 1
# G: 1 1 6 3 0 1 0 0
# T: 1 5 0 0 0 1 1 6

########## ACTUAL CODE ##########

import os
import numpy as np

def open_file(file_location):
    with open(os.path.expanduser(file_location)) as file:
        lines = file.readlines()
        new_sequence = []
        sequence_labels = []
        profile_matrix = []

        for line in lines:
            if line.startswith(">"):
                sequence_labels.append(line)
            else:
                new_sequence.append(line.strip())

        for line in new_sequence:
            profile_matrix.append(line)

        return profile_matrix

# Input new_sequence into a list for each line

fasta_file = open_file("~/Desktop/rosalind_cons.txt")
dna_array = np.array(list(fasta_file))

sequence_length = len(dna_array[0])
final_matrix = ""

profile_matrix = {
     "A": [0]*sequence_length,
     "C": [0]*sequence_length,
     "G": [0]*sequence_length,
     "T": [0]*sequence_length
}

for dna in dna_array:
    for pos, nuc in enumerate(dna):
        if nuc in profile_matrix:
            profile_matrix[nuc][pos] += 1

for nucleotide, counts in profile_matrix.items():
    final_matrix += f"{nucleotide}: {' '.join(map(str, counts))}\n"

consensus_sequence = ""

for pos in range(sequence_length):
    max_count = 0
    most_common_base = ""
    dna_nucleotides = ["A", "C", "G", "T"]
    for nucleotide in dna_nucleotides:
        if profile_matrix[nucleotide][pos] > max_count:
            max_count = profile_matrix[nucleotide][pos]
            most_common_base = nucleotide
    consensus_sequence += most_common_base

print(consensus_sequence.upper())
print(final_matrix)
