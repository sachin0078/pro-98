with open("fileA.txt","r")as A:
    dataA=A.read()

with open("fileB.txt","r")as B:
    dataB=B.read()

with open("fileA.txt","w")as A:
    A.write(dataB)

with open("fileB.txt","w")as B:
    B.write(dataA)
