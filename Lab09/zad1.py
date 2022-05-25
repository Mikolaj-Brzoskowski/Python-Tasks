import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

text="""I am not throwing away my shot!
I am not throwing away my shot!
Hey yo, I'm just like my country,
I'm young, scrappy and hungry,
and I'm not throwing away my shot!
I'm 'a get a scholarship to King's College.
I probably shouldn't brag, but dag, I amaze and astonish.
The problem is I got a lot of brains but no polish.
I gotta holler just to be heard.
With every word, I drop knowledge!
I'm a diamond in the rough, a shiny piece of coal
tryin' to reach my goal. My power of speech: unimpeachable.
Only nineteen but my mind is older.
These New York City streets get colder, I shoulder
ev'ry burden, ev'ry disadvantage
I have learned to manage, I don't have a gun to brandish,
I walk these streets famished.
The plan is to fan this spark into a flame.
But damn, it's getting dark, so let me spell out the name,
I am the"""

rick_roll="""We're no strangers to love
You know the rules and so do I (do I)
A full commitment's what I'm thinking of
You wouldn't get this from any other guy
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
Your heart's been aching, but you're too shy to say it (say it)
Inside, we both know what's been going on (going on)
We know the game and we're gonna play it
And if you ask me how I'm feeling
Don't tell me you're too blind to see
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
Your heart's been aching, but you're too shy to say it (to say it)
Inside, we both know what's been going on (going on)
We know the game and we're gonna play it
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you"""

tokenized_text=sent_tokenize(text)
tokenized_word=word_tokenize(text)

new_stopwords = ["I", "!", ",", "m", "'m", "n't", ".", "'", "'s"]

stop_words=nltk.corpus.stopwords.words('english')
stop_words.extend(new_stopwords)
filtered_sent=[]
for w in tokenized_word:
    if w not in stop_words:
        filtered_sent.append(w)
print("Filterd Sentence:",filtered_sent)

wl = WordNetLemmatizer()

lemmed_words=[]
for w in filtered_sent:
    lemmed_words.append(wl.lemmatize(w, "v"))

print(lemmed_words)

fdist = FreqDist(lemmed_words)
print(fdist.most_common(5))

fdist.plot(30,cumulative=False)
plt.show()