import os

def read_file(file_directory):
    with open(os.path.expanduser(file_directory), 'r') as f:
        lines = f.readlines()
        labels = []
        sequence_list = []

        for line in lines:
            if line.startswith(">"):
                labels.append(line.strip())
            else:
                sequence_list.append(line)

        return "".join(sequence_list)

def read_file_2(file_directory):
    with open(os.path.expanduser(file_directory), 'r') as f:
        file = f.read()
        return file

fasta_file = read_file("~/Desktop/rosalind_grph.txt")
fasta_open_2 = read_file_2("~/Desktop/rosalind_grph.txt")

# ======== FIRST VARIABLE OPENS THE RAW SEQUENCE EXCLUDING THE LABEL ======== #
# Last k nucleotides of A sequence match the First k nucleotides of sequence B

