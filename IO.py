from Token import *
def loadFile(filename):
    file = open(filename, 'r')
    return file


def readFile(file):
    content = []
    for line in file:
        if line.strip != "":
            content.append(line.strip())
    return content


def fownid(file, dic):
    dic = []
    difSet = []
    index = 0
    for i in file:
        index += 1
        count = 0
        if not dic.__contains__(i):
            count += 1
            difSet.append(i)

    return difSet

def write(tokenList, filename):
    newFile = open(filename, 'w')
    line = 1
    for t in tokenList:
        cadStr = ""
        for candidate in t.candidates:
            cadStr += str(candidate) + " "
        cadStr = cadStr.strip()
        newLine = t.name + " " + str(t.score) + " " + str(t.count) + " " + cadStr
        if line < len(tokenList):
            newFile.write(newLine + "\n")
        else:
            newFile.write(newLine)
        line +=1
    newFile.close()

def loadStatistics(filename):
    tokenList = []
    curFile = loadFile(filename)
    for line in curFile:
        infoList = line.strip().split(" ")
        newToken = Token(infoList[0],int(infoList[1]),int(infoList[2]),infoList[3:])
        tokenList.append(newToken)
    return tokenList