# Rosalind Bioinformatics Stronghold Problem 1 - Counting DNA Nucleotides
import os # Importing "Operative System" library
f = open(os.path.expanduser("~/Desktop/rosalind_dna-2.txt")) # Open data set and set it as a temporary variable in Python "f"
f = f.read().replace("\n", "") # Read "f" and combine everything into a single line

DNA_Nucleotides = ["A", "C", "G", "T"] # List of all 4 DNA nucleotides

def sequence_counter(seq): # Calling the function to count DNA nucleotides, taking one argument (sequence)
    nucleotide_dictionary = {"A": 0, "C": 0, "G": 0, "T": 0} # Dictionary creating a counter for each nucleotide, starting at 0
    for nuc in seq: # For Loop (For each nucleotide in the corresponding sequence)
        if nuc in DNA_Nucleotides: # If the nucleotide is one of the nucleotides pertaining the variable called "DNA_nucleotides"
            nucleotide_dictionary[nuc] += 1 # Sum 1 to each nucleotide encountered in the sequence
        else: # Else
            raise ValueError("Invalid nucleotide sequence") # Nucleotide != A, T, C or G = Value Errora dn display the corresponding message
    return nucleotide_dictionary # Return the updated dictionary

# However, this method will output the updated version of the dictionary, not the individual nucleotide count itself

def nucleotide_counter(seq): # Accurate function to count DNA Nucleotides
    A_counter = seq.count("A") # Count all "A"s within the corresponding sequence
    C_counter = seq.count("C") # Count all "C"s within the corresponding sequence
    G_counter = seq.count("G") # Count all "G"s within the corresponding sequence
    T_counter = seq.count("T") # Count all "T"s within the corresponding sequence

    return A_counter, C_counter, G_counter, T_counter # Return each counter separately

print(nucleotide_counter(f))
print(sequence_counter(f))

