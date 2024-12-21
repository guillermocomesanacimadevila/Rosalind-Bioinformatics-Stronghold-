# ======== Initial functions ======== #

def transcription(sequence):
    return sequence.replace('T', 'U')

def translation(sequence):
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
    protein = ""
    for nuc in range(0, len(sequence), 3):
        codon = sequence[nuc:nuc+3]
        if codon in codon_protein_dictionary:
            protein += codon_protein_dictionary[codon]
    return protein

# ======== Code ======== #

import os

def read_file(location):
    with open(os.path.expanduser(location), "r") as f:
        file = f.readlines()
        tags = ""
        sequence = ""
        for line in file:
            if line.startswith(">"):
                tags += line.strip()
            else:
                sequence += line.replace("\n", "")
        return sequence

orf_file = translation(transcription(read_file("~/Desktop/MACHINE LEARNING FITNESS TRACKER/Scripts/ORF/rosalind_orf.txt")))
orf_file_rna = transcription("~/Desktop/MACHINE LEARNING FITNESS TRACKER/Scripts/ORF/rosalind_orf.txt")
print(orf_file)

stop_codons = ["UAG", "UAA", "UGA"]
genes = ""
for nuc in orf_file:
    codon = orf_file[nuc:nuc+3]
    if orf_file_rna.startswith("AUG"):
        if orf_file_rna.endswith(stop_codons):
            genes += orf_file_rna
print(genes)