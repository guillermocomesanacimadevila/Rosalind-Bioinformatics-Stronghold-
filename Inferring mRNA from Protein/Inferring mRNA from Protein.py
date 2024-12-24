import os

def read_file(location):
    with open(os.path.expanduser(location), "r") as file:
        sequence = file.read()
        return sequence.replace("\n", "")

protein = read_file("~/Desktop/rosalind_mrna.txt")
codon_protein_dictionary = {"AUG": "M", "UUU": "F", "UUC": "F", 'UUA': 'L', 'UUG': 'L', 'UCU': 'S',
                            'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
                            'CUC': 'L', 'AUC': 'I', 'GUC': 'V', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
                            'CUG': 'L', 'GUG': 'V', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A', 'CCC': 'P',
                            'ACC': 'T', 'GCC': 'A', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A', 'CCG': 'P',
                            'ACG': 'T', 'GCG': 'A', 'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
                            'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D', 'UAA': '*', 'CAA': 'Q',
                            'AAA': 'K', 'GAA': 'E', 'UAG': '*', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
                            'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G', 'UGC': 'C', 'CGC': 'R',
                            'AGC': 'S', 'GGC': 'G', 'UGA': '*', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
                            'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
                            }

# Re-map this shit

protein_rna = {value: key for key, value in codon_protein_dictionary.items()}
print(protein_rna)

def reverse_translation(sequence):
    rna_seq = ""
    for aa in sequence:
        if aa in protein_rna:
            rna_seq += protein_rna[aa]
    return rna_seq

rna_sequence = reverse_translation(protein)
print(rna_sequence)

def counting_codons(sequence):
    codon_counter = 0
    for nuc in range(0, len(sequence), 3):
        codon = sequence[nuc:nuc+3]
        if codon in [key for key, value in codon_protein_dictionary.items()]:
            codon_counter += 1
    return codon_counter

print(counting_codons(rna_sequence))

# For each protein look at the number of codons it maps,
# mutiply them all together and then by 3

new_dict = {value:key for key, value in codon_protein_dictionary.items()}

# For every aa in protein
# Look at where it is in rev_dict
# Count how many codons does it encode
# Mass multiply all encoding codons for all AA x 3 (stop codons)

# Couting protein specific encoding codon
amino_acid_count = {key:0 for key in new_dict}
print(type([value for key, value in new_dict.items()]))
for aa in protein:
    if aa in amino_acid_count:
        amino_acid_count[aa] += 1
print(amino_acid_count)
# stop_codon_count = 3
# Count how many codons encode per AA present in aa_count_dict
# Multiply that each individual aa and by 3 in a function


# /(x / len(n)) * n(codons) * stop_codon_count (3)

#####
codons_per_amino_acid = {}
for codon, amino_acid in codon_protein_dictionary.items():
    if amino_acid not in codons_per_amino_acid:
        codons_per_amino_acid[amino_acid] = 0
    codons_per_amino_acid[amino_acid] += 1

def count_possible_rna_sequences(protein_sequence):
    total_sequences = 1
    for aa in protein_sequence:
        if aa in codons_per_amino_acid:
            total_sequences *= codons_per_amino_acid[aa]
            total_sequences %= 1_000_000  # Modulo to prevent overflow
    total_sequences *= codons_per_amino_acid['*']  # Account for stop codons
    total_sequences %= 1_000_000
    return total_sequences

result = count_possible_rna_sequences(protein)
print(result)