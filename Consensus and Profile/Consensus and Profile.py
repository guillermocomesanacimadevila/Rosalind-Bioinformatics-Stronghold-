# A: 5 1 0 0 5 5 0 0
# C: 0 0 1 4 2 0 6 1
# G: 1 1 6 3 0 1 0 0
# T: 1 5 0 0 0 1 1 6

########## ACTUAL CODE ##########

import os

def open_file(file_location):
    with open(os.path.expanduser(file_location)) as file:
        lines = file.readlines()
        sequences = []
        current_sequence = ""

        for line in lines:
            if line.startswith(">"):
                if current_sequence:
                    sequences.append(current_sequence)
                    current_sequence = ""
            else:
                current_sequence += line.strip()
        if current_sequence:  # Add the last sequence
            sequences.append(current_sequence)

        return sequences

# Parse the file
fasta_file = open_file("~/Desktop/rosalind_cons-2.txt")

# Determine sequence length
sequence_length = len(fasta_file[0])

# Initialize the profile matrix
profile_matrix = {
    "A": [0] * sequence_length,
    "C": [0] * sequence_length,
    "G": [0] * sequence_length,
    "T": [0] * sequence_length
}

# Build the profile matrix
for dna in fasta_file:
    for pos, nuc in enumerate(dna):
        if nuc in profile_matrix:
            profile_matrix[nuc][pos] += 1

# Generate the consensus sequence
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

# Format the profile matrix output
final_matrix = ""
for nucleotide in "".join(dna_nucleotides):
    counts = ' '.join(map(str, profile_matrix[nucleotide]))
    final_matrix += f"{nucleotide}: {counts}\n"

# Print results
print(consensus_sequence)
print(final_matrix)
