import os
from math import factorial


def read_file(location):
    with open(os.path.expanduser(location), "r") as file:
        lines = file.readlines()
        sequences = lines[1], lines[2]
        return "".join(sequences).replace("\n", "")

def transcription(seq):
    return seq.replace("T", "U")

rosalind_file = read_file(transcription("~/Desktop/rosalind_pmch.txt"))
print(rosalind_file)
print(f"nucleotide count: {rosalind_file.count("A"), rosalind_file.count("U"), rosalind_file.count("C"), rosalind_file.count("G")}")
print(factorial(rosalind_file.count("A")) * factorial(rosalind_file.count("G")))