from IO import *


def contain(candidates, correct):
    boo = False
    for candidate in candidates:
        if candidate.strip() == correct.strip():
            boo = True
            break
    return boo


def printPrecision(tokenList, correctList):
    attempt = 0
    TF = 0
    TF2 = 0
    sizeForShortAttempt = 0
    for i in range(0, len(tokenList)):
        if contain(tokenList[i].candidates, correctList[i]):
            # input("!")
            TF += 1
        attempt += tokenList[i].count

        if len(tokenList[i].name) <= 3:
            sizeForShortAttempt += tokenList[i].count
            if contain(tokenList[i].candidates, correctList[i]):
                TF2 += 1

    print("TF:", TF, " Attempts:", attempt)
    print("the precision is:", round((TF * 100 / attempt), 2))
    print()
    print("TF2:", TF2, " Short Tokens:", sizeForShortAttempt)
    print("the recall is:", round((TF2 * 100 / sizeForShortAttempt), 2))


def printRecall(tokenList, correctList):
    TF = 0
    TF2 = 0
    sizeForShort = 0
    for i in range(0, len(tokenList)):
        if contain(tokenList[i].candidates, correctList[i]):
            # input("!")
            TF += 1
        if len(tokenList[i].name) <= 3:
            sizeForShort += 1
            if contain(tokenList[i].candidates, correctList[i]):
                TF2 += 1

    print("TF:", TF, " Total Tokens:", len(tokenList))
    print("the recall is:", round((TF * 100 / len(tokenList)), 2))
    print()
    print("TF2:", TF2, " Short Tokens:", sizeForShort)
    print("the recall is:", round((TF2 * 100 / sizeForShort), 2))


def compareDataset():
    correctList = readFile(loadFile("correct.txt"))
    misspellList = readFile(loadFile("misspell.txt"))
    match = 0
    mismatch = 0

    for i in range(0, len(correctList)):
        if correctList[i] == misspellList[i]:
            match += 1
            print(str(i) + ": " + correctList[i])
        else:
            mismatch += 1

    print(match)


def printScoreDistribution(tokenList):
    s0 = 0
    s1 = 0
    s2 = 0
    others = 0
    for i in range(0, len(tokenList)):
        if tokenList[i].score == 0:
            s0 += 1
        elif tokenList[i].score == 1:
            s1 += 1
        elif tokenList[i].score == 2:
            s2 += 1
        else:
            others += 1
    print("0 changes:", s0, " ", s0 / len(tokenList))
    print("1 changes:", s1, " ", s1 / len(tokenList))
    print("2 changes:", s2, " ", s2 / len(tokenList))
    print("others:", others, " ", others / len(tokenList))


if __name__ == '__main__':
    fileToLoad = ""
    choice = input("please input the number to inspect statistics"
                   "\n1: globe edit distance "
                   "\n2: N-gram with n=2  ")

    if choice == str(1):
        fileToLoad = "testOutput_ged_.txt"
    elif choice == str(2):
        fileToLoad = "testOutput_2gram_.txt"
    print()
    correctList = readFile(loadFile("correct.txt"))
    tokenList = loadStatistics(fileToLoad)

    if (len(tokenList)) == (len(correctList)):
        print("the count of term match")
    else:
        print("Error")
        exit(0)

    printRecall(tokenList, correctList)
    print("------------------------")
    printPrecision(tokenList, correctList)

    if choice == str(1):
        printScoreDistribution(tokenList)
# compareDataset()
