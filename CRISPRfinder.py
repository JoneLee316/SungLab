##### CRISPR site finder - python3 CRISPRfinder.py <inputfile> <PAMsite> #####
import re
import sys

infile = sys.argv[1]
PAMsite = sys.argv[2] # change to read in file of list of PAM sites

PAMrev = PAMsite[::-1]

PAMsiteRE = ''
REVcompRE = ''
REVcomp = ""

# make sure all input files are names *.fa (* being chromosome no.)
chromosome = infile.split(".")[0]

outfile = chromosome + ".CRISPRsites.txt"

# make dictionary of each shorthand letter to make it easier to read - possibly
for i in PAMsite:
    if i == "N":
        PAMsiteRE = PAMsiteRE + r'\w'
    if i == "A":
        PAMsiteRE = PAMsiteRE + 'A'
    if i == "T":
        PAMsiteRE = PAMsiteRE + 'T'
    if i == "C":
        PAMsiteRE = PAMsiteRE + 'C'
    if i == "G":
        PAMsiteRE = PAMsiteRE + 'G'
    if i == "Y":
        PAMsiteRE = PAMsiteRE + '(T|C)'
    if i == "R":
        PAMsiteRE = PAMsiteRE + '(A|G)'
    if i == "W":
        PAMsiteRE = PAMsiteRE + '(A|T)'
    if i == "V":
        PAMsiteRE = PAMsiteRE + '(A|C)'
    if i == "S":
        PAMsiteRE = PAMsiteRE + '(G|C)'
    if i == "K":
        PAMsiteRE = PAMsiteRE + '(G|T)'
    if i == "H":
        PAMsiteRE = PAMsiteRE + '(A|T|C)'
    if i == "B":
        PAMsiteRE = PAMsiteRE + '(G|C|T)'
    if i == "D":
        PAMsiteRE = PAMsiteRE + '(G|A|T)'

for i in PAMrev: 
    if i == "N":
        REVcomp = REVcomp + i # reverse compliment stays the same
        REVcompRE = REVcompRE + r'\w'
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
    if i == "Y":
        REVcomp = REVcomp + "R" # R and Y swap for reverse compliment
        REVcompRE = REVcompRE + '(A|G)'
    if i == "R":
        REVcomp = REVcomp + "Y"
        REVcompRE = REVcompRE + '(T|C)'
    if i == "W":
        REVcomp = REVcomp + "W" # reverse compliment stays the same
        REVcompRE = REVcompRE + '(A|T)' # T|A
    if i == "V":
        REVcomp = REVcomp + "K" # V and K swap for reverse compliment
        REVcompRE = REVcompRE + '(T|G)' # T|G
    if i == "S":
        REVcomp = REVcomp + "S" # reverse compliment stays the same
        REVcompRE = REVcompRE + '(G|C)' # G|C
    if i == "K":
        REVcomp = REVcomp + "V" 
        REVcompRE = REVcompRE + '(C|A)' # C|A
    if i == "H":
        REVcomp = REVcomp + "D" # H and D swap for reverse compliment
        REVcompRE = REVcompRE + '(G|A|T)' # T|A|G
    if i == "B":
        REVcomp = REVcomp + "b" # no reverse compliment exists in the current line up
        REVcompRE = REVcompRE + '(G|C|T)' # C|G|A
    if i == "D":
        REVcomp = REVcomp + "G"
        REVcompRE = REVcompRE + '(A|T|C)' # C|T|A

# print("Chr#" + "\t" + "Position" + "\t" + "Gen_Pattern" + "\t" + "Specific_Site" + "\t" + "Fasta_file" + "\n")

with open(infile) as f:
    sequence = [line.rstrip() for line in f]
    sequence = "".join(sequence[1:])

output = open(outfile, 'w')
output.write("Chr#" + "\t" + "Position" + "\t" + "Gen_Pattern" + "\t" + "Specific_Site" + "\t" + "Fasta_file" + "\n")

for i in range(0, len(sequence)-3):
    searchSEQ = ""
    for x in range(0, len(PAMsite)):
        searchSEQ = searchSEQ + sequence[i+x]

    position = str(i)

    #add for loop to loop through array of PAMsite/REVcomp
    #have search be automatic based on PAMsite and REVcomp
    if re.search(PAMsiteRE, searchSEQ):
        # print(chromosome + "\t" + position + "\t" + PAMsite + "\t" + searchSEQ + "\t" + infile)
        output.write(chromosome + "\t" + position + "\t" + PAMsite + "\t" + searchSEQ + "\t" + infile + "\n")
    
    if re.search(REVcompRE, searchSEQ):
        # print(chromosome + "\t" + position + "\t" + REVcomp + "\t" + searchSEQ + "\t" + infile)
        output.write(chromosome + "\t" + position + "\t" + REVcomp + "\t" + searchSEQ + "\t" + infile + "\n")

output.close()
