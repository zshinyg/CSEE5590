import nltk


file = open("Python_Lesson7/input.txt", 'r')
file_content =file.read()

##TOKENIZE
tokens = nltk.word_tokenize(file_content)

##POS
pos_tokens = nltk.pos_tag(tokens)

##STEMMING
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer
snowStemmer = SnowballStemmer("english")
stem_content = snowStemmer.stem(file_content)

##LEMMATIZE
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lem_content = lemmatizer.lemmatize(file_content)


##TRIGRAM TAGGER
from nltk import ngrams
sents = nltk.sent_tokenize(file_content)
trigram_content = list(ngrams(sents,3))

###NRE
from nltk import wordpunct_tokenize, pos_tag, ne_chunk
nre_content = ne_chunk(pos_tag(wordpunct_tokenize(file_content)))
