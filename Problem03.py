def DNACompliment(strand, isDNA = True):
    # A - T/U
    # C - G    
    strandComp = ""
    for base in strand:
        if base == 'A':
            if isDNA:
                strandComp += 'T'
            else:
                strandComp += 'U'
        elif base == 'C':
            strandComp += 'G'
        elif base == 'G':
            strandComp += 'C'
        elif (base == 'T' and isDNA) or (base == 'U' and not isDNA):
            strandComp += 'A'
        else:
            raise Exception(f"Unrecognised Base ${strand}") 
    return strandComp[::-1]


with open("3.txt", 'r') as r:
    base = r.read()

print(f"The base DNA strand {base}")
print(f"The complimentary base DNA strand {DNACompliment(base)}")