# Levenshtein distance
import editdistance

import IO
# refernce https://pypi.python.org/pypi/editdistance
from Match import *
from Token import *

misspell = IO.readFile(IO.loadFile("misspell.txt"))
dictionary = IO.readFile(IO.loadFile("dictionary.txt"))



def compare(output, correctFile):
    pass

# def analyseLDistance(file, dictionary):
#     for term in file:
#         ld(term, dictionary)


def ged(file, dictionary):
    count = 1
    tokenList = []
    for m in file:
        minMark = 9999999
        collection = []
        for l in dictionary:
            curScore = editdistance.eval(m, l)
            if curScore == minMark:
                collection.append(l)
            if curScore < minMark:
                collection.clear()
                minMark = curScore
                collection.append(l)
        print("now doing:"+str(count))
        count+=1
        print("Token:" + m + "  Score:" + str(minMark) + "  Count:" + str(
            len(collection)) + "  Possible_Correction:" + str(collection))
        tokenList.append(Token(m, minMark, len(collection), collection))
    return tokenList


def analyseNGram(n,file, dictionary):
    count = 1
    tokenList = []
    for m in file:
        minMark = 9999999
        collection = []
        for l in dictionary:
            curScore = nGram(n, m, l)
            if curScore == minMark:
                collection.append(l)
            if curScore < minMark:
                collection.clear()
                minMark = curScore
                collection.append(l)
        print("now doing:"+str(count))
        count+=1
        print("Token:" + m + "  Score:" + str(minMark) + "  Count:" + str(
            len(collection)) + "  Possible_Correction:" + str(collection)
              )
        tokenList.append(Token(m, minMark, len(collection), collection))
    return tokenList


def analyseSWDistance(file, dictionary):
    count = 1
    tokenList = []
    for m in file:
        maxMark = 0
        collection = []
        for l in dictionary:
            curScore = led(m, l)
            if curScore == maxMark:
                collection.append(l)
            if curScore > maxMark:
                collection = []
                maxMark = curScore
                collection.append(l)
        print("now doing:"+str(count))
        count+=1
        print("Token:" + m + "  Score:" + str(int(maxMark)) + "  Count:" + str(
            len(collection)) + "  Possible_Correction:" + str(collection)
              )
        a = open('testOutput_led_.txt', 'a')
        curLine = m + " " + str(int(maxMark)) + " " + str(len(collection))+"\n"
        a.write(curLine)
        a.close()


if __name__ == '__main__':
    tokenList = []
    choice = input("please input your choice:\nged\nngram\nled\n")
    if choice == "ged":
        tokenList = ged(misspell,dictionary);
    elif choice == "ngram":
        tokenList = analyseNGram(3,misspell,dictionary)
    elif choice == "led":
        analyseSWDistance(misspell,dictionary)

    IO.write(tokenList, "testOutput_"+choice+"_.txt")
