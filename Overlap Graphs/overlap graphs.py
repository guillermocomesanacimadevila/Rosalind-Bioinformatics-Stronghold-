import os

def read_file(location):
    with open(os.path.expanduser(location), "r") as file:
        lines = file.readlines()
        sequences = {}
        current_header = ""
        for line in lines:
            line = line.strip()
            if line.startswith(">"):
                current_header = line[1:]
                sequences[current_header] = ""
            elif current_header:
                sequences[current_header] += line
        return sequences

ovr_grphs = read_file("~/Desktop/rosalind_grph-2.txt")
print(ovr_grphs)

# for a certain k - (k = 3) -> suffix of seq1 -> has to overlap with prefix of s2 -> generate overlap
# -> dict
# k = 3

def overlap_graphs(sequences, k=3):
    overlaps = []
    for id1, seq1 in sequences.items():
        suffix = seq1[-k:]
        for id2, seq2 in sequences.items():
            if id1 != id2:
                prefix = seq2[:k]
                if suffix == prefix:
                    overlaps.append((id1, id2))

    return overlaps

overlaps = list(overlap_graphs(ovr_grphs))
print("\n".join([f"{i[0]} {i[1]}" for i in overlaps]))