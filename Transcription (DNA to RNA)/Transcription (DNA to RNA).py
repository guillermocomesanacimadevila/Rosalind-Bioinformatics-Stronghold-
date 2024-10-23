import os
def read_file(file_path):
    with open(os.path.expanduser(file_path), "r") as f:
        sequence = f.read().replace("\n", "")
        return sequence


File_read = read_file("~/Desktop/rosalind_rna.txt") # Store corresponding file into a variable


def transcription(Seq): # Call transcription function
    return Seq.replace("T", "U") # For every "T" replace it with a "U"

print(transcription(File_read))