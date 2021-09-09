import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk import pos_tag
from nltk.corpus import wordnet

def convertposttags(liste):
    new_list=[]
    liste_tuples=pos_tag(liste)
    for tupl in liste_tuples:
        if 'VB' in tupl[1]:
            new_list.append((tupl[0],wordnet.VERB))
        elif 'NN' in tupl[1]:
            new_list.append((tupl[0],wordnet.NOUN))
        elif 'JJ' in tupl[1]:
            new_list.append((tupl[0],wordnet.ADJ))
        elif 'RB' in tupl[1]:
            new_list.append((tupl[0],wordnet.ADV))
        else: 
            new_list.append((tupl[0],'n'))
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(tupl[0],pos=tupl[1]) for tupl in new_list]
    return " ".join(lemmatized)

def NLP_preprocess(text,language='english',lemmatizer=False,stemmer=False,tags=False):
    ### lower
    text = text.lower()
    ### Not Digit
    text = ''.join(word for word in text if not word.isdigit())
    ### Punctuation
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    text = text.replace('  ',' ')
    ### Stop_words handling
    stop_words = set(stopwords.words(language))
    liste = text.split(" ")
    text = ' '.join(word for word in liste if not word in stop_words)
    text = text.split(" ")
    ### Lemmatizer activate
    if lemmatizer==True:
        lemmatizer = WordNetLemmatizer()
        if tags==True:
            text = convertposttags(text)
            text = text.split(" ")
        else :
            lemmatized = [lemmatizer.lemmatize(word) for word in text]
            text = lemmatized
    ### Stemmer activate
    if stemmer==True:
        stemmer = PorterStemmer()
        stemmer = [stemmer.stem(word) for word in text]
        text = stemmer
    return " ".join(text)