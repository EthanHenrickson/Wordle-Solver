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
        try:
            tempWord = wordList.pop(int(len(wordList)/2))
        except:
            print("Couldn't solve the word :(")
            break

        if count == 0:
            tempWord = 'soare' #salet

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
                for word in wordList:
                    if word[count1] != tempWord[count1]:
                        removeList.append(word)
        
            elif item == 1:
                for word in wordList:
                    if currentLetter not in word:
                        removeList.append(word)
                    if word[count1] == tempWord[count1]:
                        removeList.append(word) 
                 
            elif item == 0 and tempWord.count(currentLetter) == 1:
                for word in wordList:
                    if currentLetter in word:
                        removeList.append(word)

            for deleteWord in removeList:
                        wordList.remove(deleteWord)

            count1 += 1
        count += 1
    time.sleep(8)
    close()

init2()
solver()
