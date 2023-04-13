words = []
noOfWords = int(input("Please enter the number of words: "))
for i in range(noOfWords):
    w = input("Enter your word: ")
    words.append(w)

result = input("Please Enter the Result word: ")


def backTrackingAlgorithm(row, col, bal, totalNoOfRows, totalNoOfCols, words, result, alphabetToDIg, digToALphabet):
    if(col >= totalNoOfCols):
        return bal == 0

    if(row == totalNoOfRows):
        return (bal % 10 == 0 and backTrackingAlgorithm(0, col+1, bal//10, totalNoOfRows, totalNoOfCols, words, result, alphabetToDIg, digToALphabet))

    word = words[row]
    if(col >= len(word)):
        return backTrackingAlgorithm(row+1, col, bal, totalNoOfRows, totalNoOfCols, words, result, alphabetToDIg, digToALphabet)

    alphabet = word[len(word)-col-1]
    sign = 0
    if(row < totalNoOfRows-1):
        sign = 1
    else:
        sign = -1

    if alphabet in alphabetToDIg:
        return backTrackingAlgorithm(row+1, col, bal + (sign * alphabetToDIg[alphabet]), totalNoOfRows, totalNoOfCols, words, result, alphabetToDIg, digToALphabet)
    else:
        for i in range(len(digToALphabet)):
            if(digToALphabet[i] is None):
                digToALphabet[i] = alphabet
                alphabetToDIg[alphabet] = i
                if(backTrackingAlgorithm(row+1, col, bal+(sign * i), totalNoOfRows, totalNoOfCols, words, result, alphabetToDIg, digToALphabet)):
                    return True
                digToALphabet[i] = None
                if alphabet in alphabetToDIg:
                    del alphabetToDIg[alphabet]
    return False


def cryptArithmetic(words, result):
    words.append(result)
    totalNoOfRows = len(words)
    maxLength = 0
    for i in words:
        maxLength = max(maxLength, len(i))

    totalNoOfCols = maxLength
    alphabetToDIg = {}
    digToALphabet = [None for i in range(10)]
    if(backTrackingAlgorithm(0, 0, 0, totalNoOfRows, totalNoOfCols, words, result, alphabetToDIg, digToALphabet)):
        print("YES")
    else:
        print("NO")


cryptArithmetic(words, result)
