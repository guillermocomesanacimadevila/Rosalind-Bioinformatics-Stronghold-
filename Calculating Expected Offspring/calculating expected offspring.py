import os

def read_file(location):
    with open(os.path.expanduser(location), "r") as file:
        lines = file.readline()
        return list(map(int, lines.split()))

rosalind_iev = read_file("~/Desktop/rosalind_iev-2.txt")
print(type(rosalind_iev))
print([type(i) for i in rosalind_iev]) # strings at first -> int
print(rosalind_iev)

# AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa- aa, aa-aa (n = 6) -> number of pairs per genotype
print(len(rosalind_iev))

# multiply each number by respective prob of having a dominant allele
# a = 100% (1.0), etc...
single_pair = ((rosalind_iev[0] * 1) + (rosalind_iev[1] * 1) + (rosalind_iev[2] * 1) + (rosalind_iev[3] * 0.75) + (rosalind_iev[4] * 0.5) + (rosalind_iev[5] * 0))
print(single_pair * 2) # two pairs