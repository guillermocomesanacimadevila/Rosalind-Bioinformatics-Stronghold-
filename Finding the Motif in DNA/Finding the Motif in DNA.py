# GATATATGCATATACTT
# ATAT [2, 4, 10] = i + 1

import os
with open(os.path.expanduser("~/Desktop/rosalind_subs.txt")) as f:
    sequence = f.readline().replace("\n", "")
    # sequence = f.read().replace("\n", "") # Read "f" into another variable "sequence" and chuck all lines into a single line

def motif_in_seq(seq): # Calling "motif_in_seq" taking an input sequence (seq) as the unique argument
    motif_index = [] # Empty list
    motif_seq = "GTACGGCGT" # Chosen motif for identification within the chosen file
    motif_length = len(motif_seq) # Individualising motif length to whichever number of nucleotides the motif has

    for i in range(len(seq) - motif_length + 1): # For nucleotide in seq (- motif length + 1) = set adequate index
        motif = seq[i:i+motif_length] # Setting "i" to the actual individualised motif length
        if motif == motif_seq: # If motif == to the set sequence
            motif_index.append(i + 1) # Append the index of the motif + 1 - because index in python begins at 0
    return " ".join(map(str, motif_index)) # Joining an empty string to a mapped(change motif_index - int into str)

print(motif_in_seq(sequence))
