import os

def read_file(location):
    with open(os.path.expanduser(location), "r") as file:
        fasta_dict = {}
        current_tag = None
        current_sequence = []
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if current_tag: # ensured processing of tag and seq 1 by 1
                    fasta_dict[current_tag] = ''.join(current_sequence)
                current_tag = line[1:]
                current_sequence = []
            else:
                current_sequence.append(line)
        if current_tag:
            fasta_dict[current_tag] = ''.join(current_sequence)
    return fasta_dict

rosalind_lqsc = read_file("~/Desktop/rosalind_lcsq.txt")
print(rosalind_lqsc)
print(type(rosalind_lqsc))
print({len(value) for key, value in rosalind_lqsc.items()}) # not the same length

# save each key to a different dict
iterated_dict = iter(rosalind_lqsc.items())
first_key, first_value = next(iterated_dict)
second_key, second_value = next(iterated_dict)
sequence_1 = {first_key: first_value}
sequence_2  = {second_key: second_value}
print(type(sequence_1), sequence_1)
print(type(sequence_2), sequence_2)

s1 = first_value
s2 = second_value
print(type(s1), type(s2))
print(f"seq1: {s1}")
print(f"seq2: {s2}")

def common_subsequence(seq1, seq2):
    min_length = min(len(seq1), len(seq2))
    matching_nucleotides = []
    dna_nucleotides = ["A", "C", "G", "T"]
    for nuc in range(min_length):
        if seq1[nuc] == seq2[nuc] and seq1[nuc] in dna_nucleotides:
            matching_nucleotides.append(seq1[nuc])
    return "".join(matching_nucleotides)

print(common_subsequence(s1, s2))