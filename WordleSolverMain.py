import csv
from WebsiteConnect import sendKeysToParse, init, close
import time

wordList = []
def init2():
    init()
    with open("fiveletter.csv") as fileObject:
        reader_obj = csv.reader(fileObject)
        for row in reader_obj:
            temp = []
            for item in row:
                temp.append(item)
            temp.pop()*4
            temp = temp[0]
            wordList.append(temp)

def solver():   
    count = 0
    while (1):
        tempWord = wordList.pop(int(len(wordList)/2))

        if count == 0:
            tempWord = 'salet'

        tempResult = sendKeysToParse(tempWord)
                
        if tempResult == [2,2,2,2,2]:
            print(f"{count+1}, {tempWord}")
            break

        print(tempWord)
        print(tempResult, "\n")

        count1 = 0
        for item in tempResult:
            currentLetter = tempWord[count1]
            removeList = []
                
            if item == 2:
                for item2 in wordList:
                    if item2[count1] != tempWord[count1]:
                        removeList.append(item2)
        
            elif item == 1:
                for item2 in wordList:
                    if currentLetter not in (item2):
                        removeList.append(item2)
                    if item2[count1] == tempWord[count1]:
                        removeList.append(item2) 
                 
            elif item == 0 and tempWord.count(currentLetter) == 1:
                for item2 in wordList:
                    if currentLetter in (item2):
                        removeList.append(item2)

            for delete in removeList:
                        wordList.remove(delete)

            count1 += 1
        count += 1
    time.sleep(5)
    close()


init2()
solver()


#14.5% failure with pop()
#10%failure with pop(0)
#3.1% failure with pop(0) and reverse









"""
def inWord(word,wordtocompare):
    returnValue = []
    word = list(word)
    wordtocompare = list(wordtocompare)
    count = 0
    for letter in wordtocompare:
        if letter == word[count]:
            returnValue.append(2)
        elif letter in word:
            returnValue.append(1)
        else:
            returnValue.append(0)
        count += 1

    return returnValue
"""
