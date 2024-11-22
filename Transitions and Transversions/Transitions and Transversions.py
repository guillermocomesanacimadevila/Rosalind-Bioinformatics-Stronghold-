import os

def read_file(file_location):
    with open(os.path.expanduser(file_location)) as file:
        lines = file.readlines()
        labels = []
        sequences = []
        current_sequence = []

        for line in lines:
            line = line.strip()
            if line.startswith(">"):
                if current_sequence:
                    sequences.append("".join(current_sequence))
                    current_sequence = []
                labels.append(line)
            else:
                current_sequence.append(line)

        if current_sequence:
            sequences.append("".join(current_sequence))

        return sequences

fasta_sequences = read_file("~/Desktop/rosalind_tran.txt")
# "\n".join(sequences)
print(type(fasta_sequences))
print(fasta_sequences)

# =========== RETURN TRANSITION / TRANSVERSION RATIO =========== #
# Transition - When a purine is substituted by another purine (A or G) or the same with pyrimidine (T or C)
# Transversion - Purine substituted with pyrimidine or viceversa

def transition_transversion(seq1, seq2):
    purines = ["A", "G"]
    pyrimidines = ["C", "T"]
    transition_counter = 0
    transversion_counter = 0

    for nuc in range(len(seq1)):
        if seq1[nuc] != seq2[nuc]:
            if (seq1[nuc] in purines and seq2[nuc] in purines) or \
                    (seq1[nuc] in pyrimidines and seq2[nuc] in pyrimidines):
                transition_counter += 1
            else:
                transversion_counter += 1
    if transversion_counter == 0:
        return float("infinity")

    ratio = transition_counter / transversion_counter

    return ratio

print(transition_transversion(fasta_sequences[0], fasta_sequences[1]))