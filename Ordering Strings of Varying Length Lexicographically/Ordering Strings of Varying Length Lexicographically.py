import os
from itertools import product

def read_file(location):
    with open(os.path.expanduser(location), "r") as file:
        lines = file.readline().split()
        return sorted(lines)

def read_perm(location):
    with open(os.path.expanduser(location), "r") as file:
        lines = file.readlines()
        perm = lines[1]
        return perm

lexv = read_file("~/Desktop/rosalind_lexv.txt")
perms = int(read_perm("~/Desktop/rosalind_lexv.txt"))
# perm_list = list(product(lexv, repeat=range(0, perms))
# print(lexv, perms)
all_perms = []
for length in range(1, perms + 1):
    perm_list = list(product(lexv, repeat=length))
    for perm in perm_list:
        all_perms.append((''.join(perm)))

all_perms_sorted = sorted(all_perms)
for perm in all_perms_sorted:
    print(perm)