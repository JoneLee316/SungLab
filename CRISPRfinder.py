#CRISPR site finder for DNA fasta files
#Searches for PAM site and reverse compliment

import re

##### INPUTS #####
PAMsite = "NGG"
REVcomp = "CCN"
infile = "Homo_sapiens.GRCh38.dna.chromosome.1.fa"

#have the outfile and chr# auto fill 
#do this in code
outfile = "chr1.CRISPRsites.txt"
chromosome = "1"

##### NOTES #####
#When searching for new PAM sites
#Be sure to change regex search code and trimer variable accordingly
#And for loop to end of sequence

##### CODE #####
#generate reverse compliment from PAMsite
#add capability for regex to automatically search when changing PAMsite
print("Chr#" + "\t" + "Position" + "\t" + "Gen_Pattern" + "\t" + "Specific_Site" + "\t" + "Fasta_file" + "\n")

with open(infile) as f:
    sequence = [line.rstrip() for line in f]
    sequence = "".join(sequence[1:])

output = open(outfile, 'w')
output.write("Chr#" + "\t" + "Position" + "\t" + "Gen_Pattern" + "\t" + "Specific_Site" + "\t" + "Fasta_file" + "\n")

for i in range(0, 10500): #len(sequence)-3
    trimer = sequence[i] + sequence[i+1] + sequence[i+2]
    position = str(i)

    if re.search(r'\wGG', trimer):
        print(chromosome + "\t" + position + "\t" + PAMsite + "\t" + trimer + "\t" + infile)
        output.write(chromosome + "\t" + position + "\t" + PAMsite + "\t" + trimer + "\t" + infile + "\n")
    
    if re.search(r'CC\w', trimer):
        print(chromosome + "\t" + position + "\t" + REVcomp + "\t" + trimer + "\t" + infile)
        output.write(chromosome + "\t" + position + "\t" + REVcomp + "\t" + trimer + "\t" + infile + "\n")

output.close()
