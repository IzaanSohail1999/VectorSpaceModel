import io
import os
import json
from nltk.stem import WordNetLemmatizer
import string
from tkinter import *
os.system('python pos_index.py')
split_string = ""
Dict = {}
freqcounter = 1


# This is thr main function which gives directories of all stories present and the stopword list
# Here using tkinter a GUI is made where query is taken stored
# sent to concerned functions and answered displayed in answer box 
def main():
    lemmatizer = WordNetLemmatizer()
    with open('Dictionary.json') as json_file:
      Dict = json.load(json_file)
    
    # print(Dict)
    query = input("Please enter the query")
    query = query.split(" ")
    print(query)
    query = query.lower()
    query = lemmatizer.lemmatize(query, pos="v")


    
main()
