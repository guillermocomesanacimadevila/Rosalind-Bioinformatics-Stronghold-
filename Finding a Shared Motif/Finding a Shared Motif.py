# ========= CODE BELOW ========= #

import os

def read_file(file_location):
    with open(os.path.expanduser(file_location)) as file:
        lines = file.readlines()
        label_seq = {}
        current_label = ""

        for line in lines:
            line = line.strip()
            if ">" in line:
                current_label = line
                label_seq[current_label] = ""
            else:
                label_seq[current_label] += line

        return label_seq


def longest_motif(seq):
    motif = ""
    motifs = {value for key, value in seq.items()}
    motif_list = list(motifs)
    shortest_seq = min(motif_list, key=len) # Element or key within list with the smallest length

    if not motif_list: #If any element in the list = NULL
        return "" # Return empty

    for start in range(len(shortest_seq)): # For every position in shortest_seq
        for end in range(start + 1, len(shortest_seq) + 1): # For each starting index, loop through all possible ending indices
            substring = shortest_seq[start:end] # Substring from start to end
            if all(substring in sequence for sequence in motif_list): # Make sure the substring includes all the seqs in the list
                if len(substring) > len(motif): # if substring is longer than current motif
                    motif = substring

    return motif


fasta_file = read_file(os.path.expanduser('~/Desktop/rosalind_lcsm.txt'))
print(longest_motif(fasta_file))