import numpy as np
from fast_match import kw_match
import operator
from globals import *


def top_match(question):
    # returns best answer among all modules
    result = []
    for module in modules:
        result.append(eval(module)(question))
    result = best_match
    result.sort(key=operator.itemgetter(0), reverse=True)
    # pick the topmost one and check its confidence
    # TODO need to ask another question to user incase of ties
    if result[0][0] >= 0.80:
        return result[0]
    return None


def factoid(question):
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

    items = kw_match(question)
    if items:
        return items
    return top_match(question)
