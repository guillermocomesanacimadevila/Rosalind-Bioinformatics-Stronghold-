import os

f = open(os.path.expanduser("~/Desktop/rosalind_prtm.txt"))
f = f.read().replace("\n", "")

def protein_mass_calculation(seq): # Call Function
    protein_mass = {
                "A": 71.03711, "C": 103.00919, "D": 115.02694, "E": 129.04259, "F": 147.06841,
                "G": 57.02146, "H": 137.05891, "I": 113.08406, "K": 128.09496, "L": 113.08406,
                "M": 131.04049, "N": 114.04293, "P": 97.05276, "Q": 128.05858, "R": 156.10111,
                "S": 87.03203, "T": 101.04768, "V": 99.06841, "W": 186.07931, "Y": 163.06333
            }
# Dictionary key = Amino Acid, value = Mass per molecule
    protein = 0 # Set variable "protein" as 0 (int)
    for i in range(len(seq)): # For each amino acid in the sequence
        if seq[i] in protein_mass: # If the amino acid is in "protein mass" dictionary
            protein += protein_mass[seq[i]] # Append the Sum the relative values corresponding each amino acid to the variable named "protein"
    return protein 

print(protein_mass_calculation(f))