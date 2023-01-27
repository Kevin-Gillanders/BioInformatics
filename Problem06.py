from Helpers import readFileToVariable         

def findMotifPos(dna, motif): 
    if len(motif) > len(dna):
        raise Exception("Motif cannot be longer than DNA it is compared to")
    positions = []
    for i in range(0, len(dna) - len(motif)):
        window = dna[i : i + len(motif)]
        if motif == window:
            positions.append(i + 1)
    return positions

data = readFileToVariable("6.txt").split()

dnaSeq = data[0]
motif = data[1]

for x in findMotifPos(dnaSeq, motif):
    print(x, end=' ')

