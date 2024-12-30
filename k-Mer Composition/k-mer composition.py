import os
from itertools import product

def read_file(location):
    with open(os.path.expanduser(location), 'r') as f:
        lines = f.readlines()
        tag = ""
        sequence = ""
        for line in lines:
            if ">" in line:
                tag = line
            else:
                sequence += line
        return sequence.replace("\n", "")

kmer = read_file("~/Desktop/rosalind_kmer.txt")
# print(kmer) # 4-mer composition (k = 4)
# Need to know all possible 4-mer compositions for all 4 nucleotides

dna_nucleotides = "ATCG"
perm_list = list(product(dna_nucleotides, repeat=4))
formatted_perm_list = ["".join(p) for p in perm_list]
# print("\n".join(formatted_perm_list), type(formatted_perm_list))

# ===== Now let´s do it! ===== #
lex_seq = {key: 0 for key in formatted_perm_list}
format_lex = {key: lex_seq[key] for key in sorted(lex_seq)}
k = 4
for nuc in range(0, len(kmer) - k + 1):
    current_kmer = kmer[nuc:nuc + k]
    if current_kmer in format_lex:
        format_lex[current_kmer] += 1

print(str(format_lex.values()).replace("dict_values", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace(",", ""))