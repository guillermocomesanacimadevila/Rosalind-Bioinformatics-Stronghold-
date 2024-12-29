import os
from itertools import permutations
from itertools import product

def read_file(location):
    with open(os.path.expanduser(location), "r") as file:
        lines = file.readlines()
        alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        lexic = []
        indices = ""

        for line in lines:
            line = line.strip().upper()
            if line and line[0] in alphabet:
                lexic.append(line)
            else:
                indices += line
        lexic = "".join(map(str, lexic))
        lexic_split = lexic.split(" ")
        return lexic_split, int(indices)


file = read_file("~/Desktop/rosalind_lexf.txt")
print(file)

lexic_split, length = file
perm_list = list(product(lexic_split, repeat=length))

formatted_perm_list = ["".join(p) for p in perm_list]
print("\n".join(formatted_perm_list))
