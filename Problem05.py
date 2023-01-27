def getDnaInfo(dnaString):
    cCnt = 0
    gCnt = 0
    for base in dnaString.upper():
        if base == 'C':
            cCnt += 1
        elif base == 'G':
            gCnt += 1
    lenDna = len(dnaString)
    gC = (cCnt + gCnt) 
    return (gC / lenDna ) * 100

GCContent = 0
dnaStringLbl = "" 
dnaString = ""

maxGCContent = 0
maxDnaStringLbl = ""
with open("5.txt", "r") as r :
    for line in r: 
        if line.startswith(">"):
            if dnaStringLbl != "":
                GCContent = getDnaInfo(dnaString)                
                print(f"{dnaStringLbl} has a GC% of : {GCContent}%")
                if(GCContent > maxGCContent):
                    maxGCContent = GCContent
                    maxDnaStringLbl = dnaStringLbl
                GCContent = 0
                dnaStringLbl = ""
                dnaString = ""
            dnaStringLbl = line[1:].replace("\n", "")
        else:
            dnaString += line.replace("\n", "")
    GCContent = getDnaInfo(dnaString)                
    print(f"{dnaStringLbl} has a GC% of : {GCContent}%")

if(GCContent > maxGCContent):
    maxGCContent = GCContent
    maxDnaStringLbl = dnaStringLbl   

print(f"Of the given DNA strings, {maxDnaStringLbl} has the highest GC% with : {maxGCContent}%")
        
#     if (newfile.is_open()){   //checking whether the file is open
#         string 
#         while(getline(newfile, read))
#         { //read data from file object and put it into string.
#             if(read[0] == '>')
#             {
#                 if(dnaStringLbl.empty())
#                 {
#                     dnaStringLbl = read.substr(1, read.length());
#                 }
#                 c, g, dnaLen = 0;
#                 dnaString = "";
#                 cout << dnaStringLbl << endl;
#             }
#             else
#             {
#                 dnaString = dnaString;
#             }
#         }
#         newfile.close(); //close the file object.
#     }
#   return 0;
# } 