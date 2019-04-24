import numpy as np
'''
Local Edit Distance in Action
Smith-Waterman algorithm
references Smith-Waterman Python implementation
https://gist.github.com/nornagon/6326a643fc30339ece3021013ed9b48c
'''


def smith_waterman(a: str, b: str):
    """
    Compute the Smith-Waterman alignment score for two strings.
    See https://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm#Algorithm
    This implementation has a fixed gap cost (i.e. extending a gap is considered
    free). In the terminology of the Wikipedia description, W_k = {c, c, c, ...}.
    This implementation also has a fixed alignment score, awarded if the relevant
    characters are equal.
    Kinda slow, especially for large (50+ char) inputs.
    """
    # H holds the alignment score at each point, computed incrementally
    alignment_score = 1
    gap_cost = -1,
    replacement_score = -1
    H = np.zeros((len(a) + 1, len(b) + 1))
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            # The score for substituting the letter a[i-1] for b[j-1]. Generally low
            # for mismatch, high for match.
            match = H[i - 1, j - 1] + (alignment_score if a[i - 1] == b[j - 1] else replacement_score)
            # The scores for for introducing extra letters in one of the strings (or
            # by symmetry, deleting them from the other).
            delete = H[1:i, j].max() + gap_cost if i > 1 else 0
            insert = H[i, 1:j].max() + gap_cost if j > 1 else 0
            H[i, j] = max(match, delete, insert, 0)
    # The highest score is the best local alignment.
    # For our purposes, we don't actually care _what_ the alignment was, just how
    # aligned the two strings were.
    # print(H)
    return H.max()


# local Edit Distance

def led(f,t):
    lf = len(f)
    lt = len(t)
    A = np.zeros((lt + 1, lf + 1))
    A[0][0]=0
    for j in range(1,lt+1):
        for k in range(1,lf+1):
            if f[k-1] == t[j-1]:
                temp = 1
            else:
                temp = -1
            A[j][k] = max(
                0,
                A[j][k - 1] - 1,
                A[j - 1][k] - 1,
                A[j - 1][k - 1] + temp
            )
    return A.max()



def nGram(n, str1, str2):

    list1 = divideString(n, str1)
    list2 = divideString(n, str2)
    # print(list(set(list1).intersection(set(list2))))
    score = len(list1) + len(list2) - 2 * len(list(set(list1).intersection(set(list2))))
    return score


#  just
def divideString(n, curStr):
    length = len(curStr)
    strList = []
    strList.append("#"+curStr[0])
    if length < n:
        return ["#"+curStr[0],curStr,curStr[-1]+"#"]
    index = 0
    while index<= length -n:
        strList.append(curStr[index:index+n])
        index +=1
    strList.append(curStr[-1]+"#")
    return strList
