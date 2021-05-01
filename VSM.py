import io
import os
import json
from nltk.stem import WordNetLemmatizer
import string
from tkinter import *
os.system('python Dict_Create.py')
split_string = ""
Dict = {}
Dict1 = {}
Dict2 = {}
IDF = {}
newDict = {}
freqcounter = 1
with open('Dictionary.json') as json_file:
    Dict = json.load(json_file)
with open('IDF_Dict.json') as json_file:
    IDF = json.load(json_file)
def clean(split_string):
    for x in range(len(split_string)):
        if ord(split_string[x]) < 97 or ord(split_string[x]) > 122:
            split_string =  split_string.replace(split_string[x],' ')
    return split_string

def formindex(term):
  if term in Dict1:
    Dict1[term] += 1
  else:
    Dict1[term] = 1

def calculate(query,alpha):
  ans = []
  stopword = []
  stopfile = "Stopword-List.txt"
  stopFile1 = open(stopfile, "r+", encoding="utf-8")
  for line in stopFile1:
    if(len(line) >= 2):
        word = line
        word = clean(word)
        word = word.replace(' ', '')
        stopword.append(word)
  lemmatizer = WordNetLemmatizer()
  query = query.split(" ")
  for x in range(len(query)):
    query[x] = query[x].lower()
    temp = query[x]
    temp = clean(temp)
    temp = lemmatizer.lemmatize(temp, pos="v")
    check = False
    for y in stopword:
        if temp == y:
            check = True
            break
        else:
            continue

    if check == False:
        formindex(temp)

  query[x] = temp
  sum = 0
  for term in Dict1:
    Dict2[term] = IDF[term] * Dict1[term]
    Dict2[term] = Dict2[term] ** 2
    sum = sum + Dict2[term]
  sum = sum ** 0.5
  for term in Dict1:
    Dict1[term] /= sum
  for key in Dict:
    newDict[key] = 0
    for term in Dict1:
      if term in Dict[key]:
        newDict[key] += Dict1[term] * Dict[key][term]

  length = 0
  for key in newDict:
    if newDict[key] > alpha:
      ans.append(int(key))
      ans.sort()
      length += 1
      newans = 'Document are: '
  for x in range(len(ans)):
    newans = newans + str(ans[x]) + " , "
  newans = newans + "\nThe length is " + str(length)
  print(newans)
  return newans

def main():
    alpha = 0.005
    root = Tk()
    root.title('Query Search Box')
    bottomframe = Frame(root)
    bottomframe.pack(side=BOTTOM)

    Labeltext = StringVar()
    Label(bottomframe, textvariable=Labeltext).pack(side=LEFT)
    # This function is triggered on button press to process query and display answer

    def click():
        s = entry.get()
        s = s.lower()
        answer = calculate(s,alpha)
        if len(answer) == 0:
            Labeltext.set("no result found")
        else:
            Labeltext.set(str(answer))

    topframe = Frame(root)
    Label(topframe, text='Text to find:').pack(side=LEFT)
    entry = Entry(topframe)
    entry.pack()
    button = Button(topframe, text="search", command=click)
    button.pack()
    topframe.pack(side=TOP)
    root.mainloop()

  

main()
