import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer


# lemmatizer = WordNetLemmatizer()
# print(lemmatizer.lemmatize("drove", pos="v"))

porter = PorterStemmer()
print(porter.stem('house'))
