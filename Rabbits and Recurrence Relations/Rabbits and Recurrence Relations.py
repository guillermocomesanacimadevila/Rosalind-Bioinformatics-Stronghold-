import os

def open_file(file_location):
    with open(os.path.expanduser(file_location), 'r') as file:
        return file.read().replace("\n", "")

File = open_file("~/Desktop/rosalind_fib.txt")


#Fibonacci Rabbits
def Fibonacci_calculation_b(months, offspringnumber):
    parent = 1
    child = 1
    for i in range(months - 1):
        child, parent = parent, parent + (child * offspringnumber)
    return child

print(Fibonacci_calculation_b(35, 2))