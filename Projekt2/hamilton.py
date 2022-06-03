import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

script = """"""
names = []
script_dict = {
    
}

with open('Projekt2\Hamilton.txt') as f:
    script = f.read()

tokenized_text=sent_tokenize(script)
tokenized_word=word_tokenize(script)
stop_words=nltk.corpus.stopwords.words('english')
new_stopwords = ["I", "!", ",", "m", "'m", "n't", ".", "'", "'s", "``", "''", "Mr", "The", "-", "’", "?", "(", ")", "‘", ":", "&", "”", "“", "And", "You", "A", "FULL", "AND"]
stop_words.extend(new_stopwords)
filtered_word=[]
for w in tokenized_word:
    if w not in stop_words:
        filtered_word.append(w)

for word in filtered_word:
    if word.isupper():
        for splitted in word.split("/"):
            names.append(splitted)

fdist = FreqDist(filtered_word)
print(fdist.most_common(5))
