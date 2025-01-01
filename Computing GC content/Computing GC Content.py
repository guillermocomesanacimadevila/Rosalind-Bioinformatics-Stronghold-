import os

def read_file(path_of_file):
    f = open(os.path.expanduser(path_of_file), 'r')
    return [line.strip() for line in f.readlines()]
    
def GC_counter(seq): # Function for index sum of "Gs" and "Cs" as a % of len(seq) -> index nucleotide sum
    total_gc_counter_percentage = (seq.count("G") + seq.count("C")) / len(seq) * 100
    return total_gc_counter_percentage # Return %


# Variables for data storage, storing files in a list
FASTA_file_read = read_file("~/Desktop/rosalind_gc.txt") # Return as a list in a variable

# To store keys and the relevant data
FASTA_dictionary = {}

# String which is gonna be appended the relevant label
FASTA_labels = ""

# Conversion of FASTA file stored as a list into a dictionary
for line in FASTA_file_read:
    if ">" in line: # For every entry in the the list (does it have a ">")
        FASTA_labels = line
        FASTA_dictionary[FASTA_labels] = "" # If = TRUE -> Create a key for that and store it in dictionary
    else:
        FASTA_dictionary[FASTA_labels] += line # If = FALSE -> Accumulate value of the key in dictionary

# Filter through the FASTA_dictionary (both keys and values) - apply GC counter function to the values within the dictionary
Result_Dictionary = {key: GC_counter(value) for key, value in FASTA_dictionary.items()} # Dictionary comprehension

Max_GC_value_output = max(Result_Dictionary.values()) # Look within Result_Dictionary (values) and output the maximum value (int)
Max_GC_key = [key for key, value in Result_Dictionary.items() if value == Max_GC_value_output] # List comprehension - for a key of all keys and values within
Max_GC_key_output = " ".join(map(str, Max_GC_key)) # Joining an empty string to a mapped(change motif_index - int into str)
# Result_Dictionary, if value is equal to Max_GC_value, print "key".

# print(FASTA_dictionary) # Prints the name of the sequence as the key and the actual sequence as the value
# print(Result_Dictionary) # Prints "key" + GC_counter(value) as a %
print(Max_GC_key_output.strip(">")) # Prints key for the "max" GC (%), without the brackets and strip the ">" off
print(Max_GC_value_output) # Print value with "max" for GC (%) # NEED TO STRIP ">"
