import io
import os
import json
import string
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import math

split_string = ""
Dict1 = {}
Dict2 = {}
Dict3 = {}
freqcounter = 1


def formindex(filenum, counter, term):
    
    global freqcounter
    if term in Dict1:
        Dict1[term] += 1
    else: 
        Dict1[term] = 1
    
    if filenum in Dict2:
        if term in Dict2[filenum]:
            Dict2[filenum][term]  += 1
        else:
            Dict2[filenum][term]  = 1
    else:
        Dict2[filenum] = {}
        Dict2[filenum][term] = 1
        
def clean(split_string):
    for x in range(len(split_string)):
        if ord(split_string[x]) < 97 or ord(split_string[x]) > 122:
            split_string =  split_string.replace(split_string[x],' ')
    return split_string

def fileread(txtDir):
    lemmatizer = WordNetLemmatizer()
    porter = PorterStemmer()
    stopword = []
    stopfile = "Stopword-List.txt"
    stopFile1 = open(stopfile, "r+", encoding="utf-8")
    for line in stopFile1:
        if(len(line) >= 2):
            word = line
            word = clean(word)
            word = word.replace(' ', '')
            stopword.append(word)
    
    for txt in os.listdir(txtDir):
        # if txt == '1.txt':
            filenum = txt.split('.')[0] 
            filename = txtDir + txt
            textFile = open(filename, "r+", encoding="utf-8")
            counter = 1
            for my_line in textFile:
                if len(my_line) > 5:
                    split_string = my_line.split(" ")
                    for i in range(len(split_string)):
                        if len(split_string[i]) >= 1:
                            split_string[i] = split_string[i].lower()
                            split_string[i] = split_string[i].replace('\n','')
                            split_string[i] = clean(split_string[i])
                            split_string[i] = split_string[i].replace(' ','')
                            split_string[i] = lemmatizer.lemmatize(
                                split_string[i], pos="v")
                            split_string[i] = porter.stem(split_string[i])
                            # print(split_string[i])
                            check = False
                            for x in stopword:
                                if split_string[i] == x:
                                    check = True
                                    break
                                else:
                                    continue

                            if check == False:
                                formindex(filenum, counter, split_string[i])
                                counter = counter + 1
                            else:
                                counter = counter + 1

def FormIDF():
    for key in Dict1:
        Dict3[key] = math.log(50/Dict1[key])
    
def FormTFIDF():
    print("You have to evalute TF*IDF now")

def main():
    global freqcounter
    Dir = "./ShortStories\\"
    fileread(Dir)
    # with open ("Dictionary.json" , "w") as f:                                                               
    #     f.write(json.dumps(Dict, sort_keys=False, indent=4))   #Writing the index to JSON File.
    # print(freqcounter)
    # print(Dict2)
    FormIDF()
    # print(Dict3)
    FormTFIDF()
main()
