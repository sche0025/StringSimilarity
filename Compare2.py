from IO import *
import Match


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

    attempt2 = 0
    for i in range(0, len(tokenList)):
        if tokenList[i].score == Match.led(tokenList[i].name, correctList[i]):
            TF += 1
        attempt += tokenList[i].count

    print("TF:", TF, " Attempts:", attempt)
    print("the precision is:", round((TF * 100 / attempt), 3))
    for i in range(0, len(tokenList)):
        if len(tokenList[i].name) <= 3:
            if tokenList[i].score == Match.led(tokenList[i].name, correctList[i]):
                TF2 += 1
                # print(tokenList[i].name, correctList[i])
            attempt2 += tokenList[i].count
    print("\nFor tokens whose correct form is shorter than misspelled")
    print("TF:", TF2, " Attempts:", attempt2)
    print("the precision is:", round((TF2 * 100 / attempt2), 3))

def printRecall(tokenList, correctList):
    TF = 0
    TF2 = 0
    size2 = 0
    for i in range(0, len(tokenList)):
        # print(tokenList[i].candidates)
        # print(correctList[i])
        # print(contain(tokenList[i].candidates,correctList[i]))
        # print("")
        if tokenList[i].score == Match.led(tokenList[i].name, correctList[i]):
            # input("!")
            TF += 1

    print("TF:", TF, " Total Tokens:", len(tokenList))
    print("the recall is:", round((TF * 100 / len(tokenList)), 3))

    for i in range(0, len(tokenList)):
        if len(tokenList[i].name) <= 3:
            if tokenList[i].score == Match.led(tokenList[i].name, correctList[i]):
                TF2 += 1
            size2 += 1
    print("\nFor tokens whose correct form is shorter than misspelled")
    print("TF:", TF2, " Attempts:", size2)
    print("the recall is:", round((TF2 * 100 / size2), 3))
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


if __name__ == '__main__':
    fileToLoad = ""
    choice = input("please input the number to inspect statistics"
                   "\n1: local edit distances "
                   )

    if choice == str(1):
        fileToLoad = "testOutput_led_.txt"
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

# compareDataset()
