import Main
from Token import *
def removeDuplicate(list):
    l2 = []
    for i in list:
        if not l2.__contains__(i):
            l2.append(i)
    return l2

def generateTokens(file):
    tokenList = []
    for line in file:
        list = line.split(" ")
        token = Token(list[0],list[1],list[2],list[3:])
        tokenList.append(token)
    return tokenList



'''
curList = generateTokens(test2.ldOutput)
for token in curList:
    print(token.name,token.score,token.count,token.candidates)
    print("**********************")
'''