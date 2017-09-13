from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import string
from vityBot.modules.NLU.domains import *
StopWords = set(stopwords.words('english'))


def kw_match(query):
    '''
    Example-
    -------
    >>> kw_match('best clubs in vit')

    Parameters:
    ----------

       input:
       question: string

       output:
       module_name: string, None
    '''
    query = query.translate(None, string.punctuation)
    tokens = [SnowballStemmer('english').stem(token)
              for token in query.split() if token not in StopWords]

    for token in tokens:
        for module, module_list in keywords.items():
            if token in module_list:
                return module

    return None
