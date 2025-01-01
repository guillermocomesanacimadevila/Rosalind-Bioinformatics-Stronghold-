import os
import numpy as np

def read_file(location):
    with open(os.path.expanduser(location), "r") as file:
        lines = file.read().split()
        tags = ""
        sequence = ""
        for line in lines:
            if line.startswith(">"):
                tags = line
            else:
                sequence += line
        return sequence

def rev_comp(sequence):
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    reverse_complement = ""
    for nuc in range(len(sequence)):
        if sequence[nuc] in complement:
            reverse_complement += complement[sequence[nuc]]
    return "".join(reverse_complement) [::-1]

def find_palindromes(seq, rev_complement):
    pos_length = {}
    for pos in range(len(seq)):
        for length in range(4, 13):
            palindrome = seq[pos:pos+length]
            if len(palindrome) < length:
                break
            if palindrome in rev_complement:
                pos_length[pos] = len(palindrome)
                continue
    return str(np.array(list(pos_length.items()))[:,::-1]).replace("[", "").replace("]", "")

sequence = read_file("~/Desktop/rosalind_revp.txt")
rev_comp_seq = rev_comp(read_file("~/Desktop/rosalind_revp.txt"))

print(sequence)
print(rev_comp_seq)
print(find_palindromes(sequence, rev_comp_seq))

# With example
# sequence1 = "TCAATGCATGCGGGTCTATATGCAT"
# sequence_rev = rev_comp(sequence1)
# print(find_palindromes(sequence1, sequence_rev))