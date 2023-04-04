from Helpers import readFASTAFileToVariable, dnaCompliment

def identifyRestrictionSites(seq, seqComp, lowerBound, upperBound, zeroIndexed):
    for x in range(0, len(seq) ):
        # print(f"{x} : {seq}")
        for window in range(lowerBound, upperBound + 1):
            section = seq[x : x + window]
            sectionComp = seqComp[x : x + window][::-1]
            if x + window > len(seq):
                break
            if section == sectionComp:
                if zeroIdx: 
                    print(x, window)
                else:
                    print(f"{x + 1} {window}") 
                

data = readFASTAFileToVariable("7.txt")
lowerBound = 4
upperBound = 12
zeroIdx = False

for nucleotide in data:
    seq = nucleotide[1]
    seqComp = dnaCompliment(seq)
    print (f"Nucleotide sequence   : {seq}")
    print (f"Nucleotide compliment : {seqComp}")
    identifyRestrictionSites(seq, seqComp, lowerBound, upperBound, zeroIdx)
print()