# ======== Call libraries ======== #

import os

# ======== Initial functions ======== #

def rev_comp(sequence):
    rev_comp_dict = {"A": "T", "T": "A", "G": "C", "C": "G"}
    return "".join(rev_comp_dict[nuc] for nuc in sequence[::-1])

def transcription(sequence):
    return sequence.replace('T', 'U')

def translation(sequence):
    codon_protein_dictionary = {
        "AUG": "M", "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "CUU": "L",
        "AUU": "I", "GUU": "V", "CUC": "L", "AUC": "I", "GUC": "V",
        "CUA": "L", "AUA": "I", "GUA": "V", "CUG": "L", "GUG": "V",
        "CCU": "P", "ACU": "T", "GCU": "A", "CCC": "P", "ACC": "T",
        "GCC": "A", "CCA": "P", "ACA": "T", "GCA": "A", "CCG": "P",
        "ACG": "T", "GCG": "A", "UAU": "Y", "CAU": "H", "AAU": "N",
        "GAU": "D", "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
        "UAA": "*", "CAA": "Q", "AAA": "K", "GAA": "E", "UAG": "*",
        "CAG": "Q", "AAG": "K", "GAG": "E", "UGU": "C", "CGU": "R",
        "AGU": "S", "GGU": "G", "UGC": "C", "CGC": "R", "AGC": "S",
        "GGC": "G", "UGA": "*", "CGA": "R", "AGA": "R", "GGA": "G",
        "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
    }
    protein = ""
    for nuc in range(0, len(sequence) - 2, 3):
        codon = sequence[nuc:nuc+3]
        if codon in codon_protein_dictionary:
            if codon_protein_dictionary[codon] == "*":
                break
            protein += codon_protein_dictionary[codon]
    return protein

# ======== Code ======== #

import os

def read_file(location):
    with open(os.path.expanduser(location), "r") as f:
        file = f.readlines()
        sequence = ""
        for line in file:
            if not line.startswith(">"):
                sequence += line.strip()
        return sequence

dna_sequence = read_file("~/Desktop/rosalind_orf.txt")
orf_file_rna = transcription(dna_sequence)
orf_file_rna_rev = transcription(rev_comp(dna_sequence))

genes = []
stop_codons = ["UAG", "UAA", "UGA"]

for nuc in range(0, len(orf_file_rna) - 2, 3):
    codon = orf_file_rna[nuc:nuc+3]
    if codon == "AUG":
        gene = ""
        for i in range(nuc, len(orf_file_rna) - 2, 3):
            next_codon = orf_file_rna[i:i+3]
            if next_codon in stop_codons:
                break
            gene += next_codon
        if gene:
            genes.append(translation(gene))

genes_by_lines = "\n".join(genes)
# print(genes_by_lines)

genes_rev = []
for nucleotide in range(0, len(orf_file_rna_rev) - 2, 3):
    codon_1 = orf_file_rna_rev[nucleotide:nucleotide+3]
    if codon_1 == "AUG":
        gene_1 = ""
        for i in range(nucleotide, len(orf_file_rna_rev) - 2, 3):
            next_codon = orf_file_rna_rev[i:i+3]
            if next_codon in stop_codons:
                break
            gene_1 += next_codon
        if gene_1:
            genes_rev.append(translation(gene_1))

genes_by_lines_rev = "\n".join(genes_rev)
print(genes_by_lines_rev)
