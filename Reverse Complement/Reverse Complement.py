import os
f = open(os.path.expanduser("~/Desktop/rosalind_revc.txt"))
sequence = f.read().replace("\n", "")

def rev_comp(seq): # Call Reverse Complement Function that takes the input sequence as the only argument
    reverse_comp_dictionary = {"A": "T", "T": "A", "C": "G", "G": "C"} # Dictionary to equate each nucleotide to its reverse complement
    reverse_complement_sequence = "" # Empty string

    for i in range(len(seq)): # For nucleotide in the whole length of the sequence
        reverse_complement_sequence += reverse_comp_dictionary[seq[i]]  # Replace each nucleotide with the reverse complement from the dictionary and replace it into the empty string
    return reverse_complement_sequence [::-1] # Return the empty string "reversely"

print(sequence)
print(rev_comp(sequence))



