##### CRISPR site finder for DNA fasta files #####

#Searches for PAM site and reverse compliment

##### INPUTS #####

PAMsite = "NGG"
infile = "Homo_sapiens.GRCh38.dna.chromosome.22.fa"

##### CODE #####

#import all necessary packages
import re

#extract variables from inputs
PAMrev = PAMsite[::-1]

PAMsiteRE = ''
REVcompRE = ''
REVcomp = ""

#this might need to be updates as different files are used
chromosome = re.findall('\d+', infile)[1]

outfile = "chr" + chromosome + ".CRISPRsites.txt"

for i in PAMsite:
    if i == "N":
        PAMsiteRE = PAMsiteRE + '\w'
    if i == "A":
        PAMsiteRE = PAMsiteRE + 'A'
    if i == "T":
        PAMsiteRE = PAMsiteRE + 'T'
    if i == "C":
        PAMsiteRE = PAMsiteRE + 'C'
    if i == "G":
        PAMsiteRE = PAMsiteRE + 'G'

for i in PAMrev:
    if i == "N":
        REVcomp = REVcomp + i
        REVcompRE = REVcompRE + '\w'
    if i == "A":
        REVcomp = REVcomp + "T"
        REVcompRE = REVcompRE + 'T'
    if i == "T":
        REVcomp = REVcomp + "A"
        REVcompRE = REVcompRE + 'A'
    if i == "C":
        REVcomp = REVcomp + "G"
        REVcompRE = REVcompRE + 'G'
    if i == "G":
        REVcomp = REVcomp + "C"
        REVcompRE = REVcompRE + 'C'

#print header for output to terminal
print("Chr#" + "\t" + "Position" + "\t" + "Gen_Pattern" + "\t" + "Specific_Site" + "\t" + "Fasta_file" + "\n")

#read in sequence
with open(infile) as f:
    sequence = [line.rstrip() for line in f]
    sequence = "".join(sequence[1:])

#open output file to write too and add header
output = open(outfile, 'w')
output.write("Chr#" + "\t" + "Position" + "\t" + "Gen_Pattern" + "\t" + "Specific_Site" + "\t" + "Fasta_file" + "\n")

#for loop to loop through sequence and find all PAMsites and REVcomps
for i in range(0, len(sequence)-3): #range(0, len(sequence)-3) CHANGE BACK WHEN COMPLETE
    #generate seqence to search against based on position in sequence
    searchSEQ = ""
    for x in range(0, len(PAMsite)):
        searchSEQ = searchSEQ + sequence[i+x]
    
    #convert position variable to string for output
    position = str(i)

    #have search be automatic based on PAMsite and REVcomp
    if re.search(PAMsiteRE, searchSEQ):
        print(chromosome + "\t" + position + "\t" + PAMsite + "\t" + searchSEQ + "\t" + infile)
        output.write(chromosome + "\t" + position + "\t" + PAMsite + "\t" + searchSEQ + "\t" + infile + "\n")
    
    if re.search(REVcompRE, searchSEQ):
        print(chromosome + "\t" + position + "\t" + REVcomp + "\t" + searchSEQ + "\t" + infile)
        output.write(chromosome + "\t" + position + "\t" + REVcomp + "\t" + searchSEQ + "\t" + infile + "\n")

#close output file
output.close()
