#CRISPR site finder for DNA fasta files
#Searches for PAM site and reverse compliment

import re

##### INPUTS #####
PAMsite = "NGG"
REVcomp = "CCN"
infile = "Homo_sapiens.GRCh38.dna.chromosome.1.fa"
outfile = "chr1.CRISPRsites.txt"

##### NOTES #####
#When searching for new PAM sites
#Be sure to change regex search code and trimer variable accordingly
#And for loop to end of sequence

##### CODE #####
#generate reverse compliment from PAMsite
#add capability for regex to automatically search when changing PAMsite
print("Location" + "\t" + "Fasta_file" + "\t" + "Gen_Pattern" + "\t" + "Specific_Site")

with open(infile) as f:
    sequence = [line.rstrip() for line in f]
    sequence = "".join(sequence[1:])

output = open(outfile, 'w')
output.write("Location" + "\t" + "Fasta_file" + "\t" + "Gen_Pattern" + "\t" + "Specific_Site" + "\n")

for i in range(0, len(sequence)-3):
    trimer = sequence[i] + sequence[i+1] + sequence[i+2]
    location = str(i)

    if re.search(r'\wGG', trimer):
        print(location + "\t" + infile + "\t" + PAMsite + "\t" + trimer)
        output.write(location + "\t" + infile + "\t" + PAMsite + "\t" + trimer + "\n")
    
    if re.search(r'CC\w', trimer):
        print(location + "\t" + infile + "\t" + REVcomp + "\t" + trimer)
        output.write(location + "\t" + infile + "\t" + REVcomp + "\t" + trimer + "\n")

output.close()