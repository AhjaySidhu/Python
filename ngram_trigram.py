import doctest

"""
ngrams module
==========

Import everything:

    >>> from ngrams import *

MLE models
------------------

Trigram:

    >>> model1 = NGramMLE(3)
    >>> model1.train(brownPart('a'))
    >>> model1.estimate()
    
    >>> model1.p('Pirate Manager Paul Stone is suspended .'.split())

    
    >>> model1.perplexity('Pirate Manager Paul Stone is suspended .'.split())


    >>> model1.p('Pirate Manager Paul Stone was suspended .'.split())


    >>> model1.perplexity('Pirate Manager Paul Stone was suspended .'.split())

    """
    
    
if __name__ == '__main__':
    doctest.testfile('ngram_trigram.py')