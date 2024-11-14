import os

def read_file(file_directory):
    with open(os.path.expanduser(file_directory), "r") as f:
        file = f.readlines()
        sequence = ""
        recording = False  # Flag to start/stop recording lines

        for line in file:
            if line.startswith(">"):
                if recording:  # If already recording, stop when encountering the next ">"
                    break
                recording = True  # Start recording when the first ">" is found
            elif recording:
                sequence += line  # Record lines only when the flag is True

        return sequence.replace("\n", "")

def accumulate_introns(file_directory):
    with open(os.path.expanduser(file_directory), "r") as f:
        content = f.readlines()
        introns = {}
        current_header = "" # Store the most recent header
        intron_accumulator = ""

        for line in content: # For each line in the file
            line = line.strip() # Get rid of all spaces
            if line.startswith(">"):
                current_header = line[1:] # Setting current_header to be the line without the greater than symbol
                introns[current_header] = "" # Setting "current header" as the key
            elif current_header: # If the line does not start with the greater than symbol
                introns[current_header] += line

        intron_accumulator = " ".join(map(str,{value for value in introns.values() if not value.startswith("AUG")}))

        return intron_accumulator

#  {value for key, value in introns.items() if key != "AUG"}

def transcription(seq):
    return seq.replace("T", "U")

def translation(seq):
    amino_acids = {'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'UCU': 'S',
                   'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
                   'CUC': 'L', 'AUC': 'I', 'GUC': 'V', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
                   'CUG': 'L', 'GUG': 'V', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A', 'CCC': 'P',
                   'ACC': 'T', 'GCC': 'A', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A', 'CCG': 'P',
                   'ACG': 'T', 'GCG': 'A', 'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
                   'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D', 'UAA': '*', 'CAA': 'Q',
                   'AAA': 'K', 'GAA': 'E', 'UAG': '*', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
                   'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G', 'UGC': 'C', 'CGC': 'R',
                   'AGC': 'S', 'GGC': 'G', 'UGA': '*', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
                   'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'}
    protein = ""
    for nuc in range(0, len(seq), 3):
        codon = seq[nuc:nuc+3]
        if codon in amino_acids:
            protein += amino_acids[codon]

    return protein

FASTA_open_RNA = transcription(read_file("~/Desktop/rosalind_splc.txt"))
FASTA_open_introns = (accumulate_introns("~/Desktop/rosalind_splc.txt"))

##################

FASTA_open_introns_RNA = transcription(FASTA_open_introns)
FASTA_open_RNA_2 = transcription(FASTA_open_RNA)
FASTA_open_introns = [transcription(intron) for intron in FASTA_open_introns]

def remove_introns(trans_seq, introns):
    new_seq = trans_seq

    for intron in introns:
        new_seq = new_seq.replace(intron, "")

    return new_seq

print(remove_introns(FASTA_open_RNA_2, FASTA_open_introns))