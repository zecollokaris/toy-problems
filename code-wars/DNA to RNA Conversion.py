######Question#####

# Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

# Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').

# Create a funciton which translates a given DNA string into RNA.

# For example:

# DNAtoRNA("GCAT") returns ("GCAU")


#################################################################################

###### BDD ######


# -We will need to first select the letter to be replace
# in this case letter is the last letter

# -We could use (dna[-1]) : to select the last letter in the string

# -We will need to replace the last letter in the string T with the U

# -replace function can be used

#################################################################################

#####Code####

def DNAtoRNA(dna):
    return dna.replace("T","U")

#################################################################################