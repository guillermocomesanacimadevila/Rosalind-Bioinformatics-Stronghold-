import os

def read_file(location):
    with open(os.path.expanduser(location), "r") as file:
        f = file.readlines()
        sequence = ""
        tags = ""
        motif = " "
        for line in f[:-2]:
            if line.startswith(">"):
                tags += line
            else:
                sequence += line.strip()
        for line in f[-2:]:
            motif += line.strip()
        return sequence, motif

splc_motif = read_file("~/Desktop/rosalind_sseq.txt")
sequence_dict = {"sequence": splc_motif[0], "motif": splc_motif[1]}
print(splc_motif)
print(type(splc_motif)) # tuple
# Smaller sequence = motif
# Larger sequence = actual DNA

indices_list = []
current_position = 0
for nuc in sequence_dict["motif"]:
    if nuc in sequence_dict["sequence"] [current_position:]:
        index = sequence_dict["sequence"].index(nuc, current_position)
        indices_list.append(index + 1)
        current_position = index + 1

print(str(indices_list).replace("[", "").replace("]", "").replace(",", ""))