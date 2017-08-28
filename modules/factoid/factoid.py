from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import string
from modules import *
StopWords = set(stopwords.words('english'))


def factoid(query):
    '''
    Example-
    -------
    >>> factoid('best clubs in vit')

    Parameters:
    ----------

       input:
       question: string

       output:
       confidence, answer or None
    '''
    query = query.translate(None, string.punctuation)
    tokens = [SnowballStemmer('english').stem(token)
              for token in query.split() if token not in StopWords]

    for token in tokens:
        for module, module_list in keywords.items():
            if token in module_list:
                return eval(module)(query, tokens)

    return None
