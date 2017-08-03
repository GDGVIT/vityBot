from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import string
from globals import *
StopWords = set(stopwords.words('english'))


def kw_match(query):

    # remove punctuations, stop words and stem it
    query = query.translate(None, string.punctuation)
    tokens = [SnowballStemmer('english').stem(token)
              for token in query.split() if token not in StopWords]

    for token in tokens:
        for module, module_list in keywords.items():
            if token in module_list:
                return eval(module)(query, tokens)

    return None
