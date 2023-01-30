from Helpers import readFASTAFileToVariable

data = readFASTAFileToVariable("7.txt")

for seq in data:
    print(seq)