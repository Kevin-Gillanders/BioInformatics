def readFileToVariable (fileName):
    with open(fileName, "r") as r :
        data = r.read()
        print(f"Reading {fileName}")
        print("===========")
        print(f"Read in {data}")
        return data   

def readFASTAFileToVariable(fileName):
    fastaData = readFileToVariable(fileName).split("\n")
    fastaDataPaired = []
    sequenceIdentifier = ""
    sequenceData = ""
    firstElem = True
    for line in fastaData:
        if line[0] == ">":
            if firstElem:
                firstElem = False
                sequenceIdentifier = line[1:]
                continue
            fastaDataPaired.append([sequenceIdentifier, sequenceData])
            sequenceIdentifier = line[1:]
            print(sequenceIdentifier)
            sequenceData = ""
        else:
            sequenceData += line
    
    fastaDataPaired.append([sequenceIdentifier, sequenceData])

    return fastaDataPaired

def readFileToIterator(fileName):
    with open(fileName, "r") as r :
        for line in r:
            yield line 

def readFASTAFileToIterator(fileName):
    fastaData = readFileToIterator(fileName).split("\n")
    fastaDataPaired = []
    sequenceIdentifier = ""
    sequenceData = ""
    firstElem = True
    for line in fastaData:
        if line[0] == ">":
            if firstElem:
                firstElem = False
                sequenceIdentifier = line[1:]
                continue
            # fastaDataPaired.append([sequenceIdentifier, sequenceData])
            yield [sequenceIdentifier, sequenceData]
            sequenceIdentifier = line[1:]
            print(sequenceIdentifier)
            sequenceData = ""
        else:
            sequenceData += line
    
    # fastaDataPaired.append([sequenceIdentifier, sequenceData])
    yield [sequenceIdentifier, sequenceData]

    
