import os
import numpy as np

def open_file(file_location):
    with (open(os.path.expanduser(file_location), 'r') as f):
        lines = f.readlines()
        sequence = ""
        integers = []

        for line in lines:
            line = line.strip()
            if all(char in "ATCG" for char in line):
                sequence += line
            else:
                integers.extend(line.split())

        return integers, sequence
# elements = [integers[i:i + len(integers)] for i in range(0, len(integers), 5)]

def counting_nuc(seq):
    nuc_dict = {"A": 0, "C": 0, "G": 0, "T": 0}

    for nuc in seq:
        if nuc in nuc_dict:
            nuc_dict[nuc] += 1

    return nuc_dict

fasta_file = open_file("~/Desktop/rosalind_prob.txt")
# print(fasta_file[0])
# print(counting_nuc(fasta_file[1]))


# total_log_numpy = (np.sum(np.log10(values)))
# print(total_log_numpy)
# logged_list = (np.sum(np.log10([element for element in logged_integer])))

numeric_elements = list(map(float, fasta_file[0]))

def logarithmic_calculation(values):
    gc_value = [element / 2 for element in values]
    at_value = [(1 - i) / 2 for i in values]
    log_dict = [(gc_value[i], at_value[i], gc_value[i], at_value[i]) for i in range(len(values))]

    summed_log_tuples = [np.sum(np.log10(tup)) for tup in log_dict]

    return summed_log_tuples

# print(logarithmic_calculation(numeric_elements))

final_val = str(logarithmic_calculation(numeric_elements)).replace("np.float64", "").replace("[", "").replace("]", "").replace(",", "").replace(")", "").replace("(", "")
print(final_val)