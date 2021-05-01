import io
import os
import json
import string
from nltk.stem import WordNetLemmatizer
import math

split_string = ""
vocab_list = []
Dict1 = {}
Dict2 = {}
Dict3 = {}
Dict4 = {}
freqcounter = 1

def formindex(filenum, term):
    if filenum in Dict2:
        if term in Dict2[filenum]:
            Dict2[filenum][term]  += 1
        else:
            if term in Dict1:
                Dict1[term] += 1
            else:
                Dict1[term] = 1
            Dict2[filenum][term]  = 1
    else:
        Dict2[filenum] = {}
        Dict2[filenum][term] = 1
        # Dict1[term] += 1 #changes made here
        
def clean(split_string):
    for x in range(len(split_string)):
        if ord(split_string[x]) < 97 or ord(split_string[x]) > 122:
            split_string =  split_string.replace(split_string[x],' ')
    return split_string

def fileread(txtDir):
    lemmatizer = WordNetLemmatizer()
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
        filenum = txt.split('.')[0] 
        filename = txtDir + txt
        textFile = open(filename, "r+", encoding="utf-8")
        for my_line in textFile:
            if len(my_line) > 5:
                split_string = my_line.split(" ")
                for i in range(len(split_string)):
                    if len(split_string[i]) >= 1:
                        split_string[i] = split_string[i].lower()
                        split_string[i] = split_string[i].replace('\n','')
                        split_string[i] = clean(split_string[i])
                        split_string[i] = split_string[i].replace(' ','')
                        split_string[i] = lemmatizer.lemmatize(split_string[i], pos="v")
                        check = False
                        for x in stopword:
                            if split_string[i] == x:
                                check = True
                                break
                            else:
                                continue

                        if check == False:
                            formindex(filenum, split_string[i])

def FormIDF():
    for key in Dict1:
        Dict3[key] = math.log10(50/Dict1[key])
    
def FormTFIDF():
    for key in Dict3:
        for key1 in Dict2:
            for term in Dict2[key1].keys():
                if key == term:
                    Dict2[key1][term] *= Dict3[term]

def EvaluateWeight():
    sum = 0
    temp = {}
    addlist = []
    Dict4 = Dict2.copy()
    for key in Dict4:
        for term in Dict4[key]:
            Dict4[key][term] = Dict4[key][term] ** 2
    
    # print(Dict4)
    
    for key in Dict4:
        for term in Dict4[key]:
            sum = sum + Dict4[key][term]
        # print("Document number and sum before square root: " + str(key) + "--> " + str(sum))
        sum = sum ** 0.5
        # print("Document number and sum after square root: " + str(key) + "--> " + str(sum))
        temp[key] = sum
        dict_copy = temp.copy()
        addlist.append(dict_copy)
        sum = 0
    
    # print(addlist)
    # print(addlist[49].values())

    for key in Dict2:
        print(str(addlist[key]))
        for term in Dict2[key]:
            temp = Dict2[key][term]
            # print(temp)
            # print(addlist[key])
            # for x in range(addlist):
            #     if key == addlist[x]:
            #         temp = temp / 



def main():
    Dir = "./ShortStories\\"
    fileread(Dir)
    FormIDF()
    vocab = list(Dict3.keys())
    FormTFIDF()
    # print(Dict2)
    EvaluateWeight()
    with open ("Dictionary.json" , "w") as f:                                                               
        f.write(json.dumps(Dict2, sort_keys=False, indent=4))
    with open("Vocabulary.json", "w") as f:
        f.write(json.dumps(vocab, sort_keys=False, indent=4))
    with open("IDF_Dict.json", "w") as f:
        f.write(json.dumps(Dict3, sort_keys=False, indent=4))
    
main()
