##### CRISPR site finder - python3 CRISPRfinder.py <inputfile> <PAMsite> #####
import re
import sys

infile = sys.argv[1]
PAMsite = sys.argv[2]

# make sure all input files are names *.fa (* being chromosome no.)
chromosome = infile.split(".")[0]

outfile = chromosome + ".CRISPRsites.txt"

PAMrev = PAMsite[::-1]

PAMsiteRE = ''
REVcompRE = ''
REVcomp = ""

PAMdictRE = {"N":r'\w', "A": 'A', "T":'T', "C":'C', "G":'G', "Y":'(T|C)', "R":'(A|G)', "W":'(A|T)', "V":'(A|C)', "S":'(G|C)', "K":'(G|T)', "H":'(A|T|C)', "B":'(G|C|T)', "D":'(G|A|T)'}
REVdictRE = {"N":r'\w', "A": 'T', "T":'A', "C":'G', "G":'C', "Y":'(A|G)', "R":'(T|C)', "W":'(T|A)', "V":'(T|G)', "S":'(C|G)', "K":'(C|A)', "H":'(T|A|G)', "B":'(C|G|A)', "D":'(C|T|A)'}
REVdictSYM = {"N":'N', "A": 'T', "T":'A', "C":'G', "G":'C', "Y":'R', "R":'Y', "W":'W', "V":'K', "S":'S', "K":'V', "H":'D', "B":'b', "D":'H'}

for i in PAMsite:
    PAMsiteRE = PAMsiteRE + PAMdictRE[i]

for i in PAMrev: 
    REVcomp = REVcomp + REVdictSYM[i]
    REVcompRE = REVcompRE + REVdictRE[i]

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

    if re.search(PAMsiteRE, searchSEQ):
        # print(chromosome + "\t" + position + "\t" + PAMsite + "\t" + searchSEQ + "\t" + infile)
        output.write(chromosome + "\t" + position + "\t" + PAMsite + "\t" + searchSEQ + "\t" + infile + "\n")
    
    if re.search(REVcompRE, searchSEQ):
        # print(chromosome + "\t" + position + "\t" + REVcomp + "\t" + searchSEQ + "\t" + infile)
        output.write(chromosome + "\t" + position + "\t" + REVcomp + "\t" + searchSEQ + "\t" + infile + "\n")

output.close()
