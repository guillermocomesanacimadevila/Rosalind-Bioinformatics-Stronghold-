import os
import difflib

def read_file(location):
    with open(os.path.expanduser(location)) as file:
        lines = file.readlines()
        tags = []
        sequence1 = ""
        sequence2 = ""
        for line in lines:
            if line.startswith(">"):
                tags.append(line.strip())
            elif line in lines[:17]:
                sequence1 += line.strip()
            else:
                sequence2 += line.strip()
                dict = {tags[0]: sequence1, tags[1]: sequence2}
        return sequence1, sequence2

# print(len(os.path.expanduser("~/Desktop/rosalind_lcsq.txt")))
sequence = read_file('~/Desktop/rosalind_lcsq.txt')
matcher = difflib.SequenceMatcher(None, sequence[0], sequence[1])
lcs = ''.join(sequence[0][op[0]:op[0] + op[2]] for op in matcher.get_matching_blocks() if op[2] > 0)
print(sequence)
print(lcs)
