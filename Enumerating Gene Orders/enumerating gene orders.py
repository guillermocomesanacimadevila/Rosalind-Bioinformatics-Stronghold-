import os
from itertools import permutations

def read_file(file_path):
    with open(os.path.expanduser(file_path), 'r') as f:
        value = f.readline().strip()
        return int(value)

final_integer = read_file("~/Desktop/rosalind_perm.txt")
print(f"Input Integer: {final_integer}")

new_list = list(range(1, final_integer + 1))
print(f"List of Numbers: {new_list}")

all_permutations = list(permutations(new_list))
print(f"Total Permutations: {len(all_permutations)}")

for perm in all_permutations:
    print(" ".join(map(str, perm)))