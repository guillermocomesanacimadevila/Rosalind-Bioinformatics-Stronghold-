import os
with open(os.path.expanduser("~/Desktop/rosalind_hamm.txt"), "r") as f1:
    lines = f1.readlines()
    seq1 = lines[0].strip()
    seq2 = lines[1].strip()


def counting_point_mutations(sequence1, sequence2):
    if len(sequence1) != len(sequence2):
        raise ValueError("Sequence length mismatch")

    mutation_counter = 0
    for i in range(len(sequence1)):
        if sequence1[i] != sequence2[i]:
            mutation_counter += 1

    return mutation_counter

print(counting_point_mutations(seq1, seq2))