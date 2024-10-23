import os # Import "os" library

f = open(os.path.expanduser("~/Desktop/rosalind_prot-2.txt")) # Open the relevant file into a temporary variable in python, named "f"
f = f.read().replace("\n", "") # Combine all lines within the file into a single line

def RNA_protein_translation(seq):
    codon_protein_dictionary = {"AUG":"M","UUU":"F","UUC":"F",'UUA':'L','UUG':'L','UCU':'S',
                  'UCC':'S','UCA':'S','UCG':'S','CUU': 'L','AUU': 'I','GUU': 'V',
                  'CUC': 'L','AUC': 'I','GUC': 'V','CUA': 'L','AUA': 'I','GUA': 'V',
                  'CUG': 'L','GUG': 'V','CCU': 'P', 'ACU': 'T','GCU': 'A','CCC': 'P',
                  'ACC': 'T','GCC': 'A','CCA': 'P','ACA': 'T','GCA': 'A','CCG': 'P',
                  'ACG': 'T','GCG': 'A','UAU': 'Y','CAU': 'H','AAU': 'N','GAU': 'D',
                  'UAC': 'Y','CAC': 'H','AAC': 'N','GAC': 'D','UAA': '*','CAA': 'Q',
                  'AAA': 'K','GAA': 'E','UAG': '*','CAG': 'Q','AAG': 'K','GAG': 'E',
                  'UGU': 'C','CGU': 'R','AGU': 'S','GGU': 'G','UGC': 'C','CGC': 'R',
                  'AGC': 'S','GGC': 'G','UGA': '*','CGA': 'R','AGA': 'R','GGA': 'G',
                  'UGG': 'W','CGG': 'R','AGG': 'R','GGG': 'G'
                                }
# Dictionary setting each codon equal to the relevant letter corresponding to the protein they encode to

    protein_translation = "" # Creating an empty string to append the translation
    for i in range(0, len(seq), 3): # For nucleotide in the sequence
        codon = seq[i:i+3] # Codon = index (i = +3 indices)
        if codon in codon_protein_dictionary: # If the codon is in the dictionary
            protein_translation += codon_protein_dictionary[codon] # Append to the protein_translation string the encoded protein
    return protein_translation # Return the previously empty string


print(RNA_protein_translation(f))