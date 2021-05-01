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
freqcounter = 1

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

def main():
    lemmatizer = WordNetLemmatizer()
    with open('Dictionary.json') as json_file:
      Dict = json.load(json_file)
    with open('IDF_Dict.json') as json_file:
      IDF = json.load(json_file)
    # print(Dict)
    # query = input("Please enter the query: ")
    query = "BOY BOY GIRL"
    query = query.split(" ")
    for x in range(len(query)):
      query[x] = query[x].lower()
      temp = query[x]
      temp = clean(temp)
      temp = lemmatizer.lemmatize(temp, pos="v")
      formindex(temp)
      query[x] = temp
    print(Dict1)
    sum = 0
    for term in IDF:
      for newterm in Dict1:     
        if term == newterm:
          Dict2[term] = IDF[term] * Dict1[term]
          Dict2[term] = Dict2[term] ** 2
          sum = sum + Dict2[term]
    sum = sum ** 0.5
    print(sum)
    for term in Dict1:
      Dict1[term] /= sum
    print(Dict1)
main()
