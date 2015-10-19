import doctest

"""
ngrams module
==========

Import everything:

    >>> from ngrams import *

MLE models
------------------

Unigrams:

    >>> model1 = NGramMLE(1)
    >>> model1.train(brownPart('a'))
    >>> model1.estimate()
    
    >>> model1.p('Pirate Manager Paul Stone is suspended .'.split())
    P(Pirate) = 1.901556e-05
    P(Manager) = 3.803113e-05
    P(Paul) = 5.704669e-05
    P(Stone) = 3.803113e-05
    P(is) = 6.959697e-03
    P(suspended) = 1.901556e-05
    P(.) = 3.831636e-02
    P(</s>) = 4.395448e-02
    P(Pirate,Manager,Paul,Stone,is,suspended,.,</s>) = 3.497076e-28
    3.4970755276226645e-28
    
    >>> model1.perplexity('Pirate Manager Paul Stone is suspended .'.split())
    8362.34065658542

    >>> model1.p('Pirate Manager Paul Stone was suspended .'.split())
    P(Pirate) = 1.901556e-05
    P(Manager) = 3.803113e-05
    P(Paul) = 5.704669e-05
    P(Stone) = 3.803113e-05
    P(was) = 6.817080e-03
    P(suspended) = 1.901556e-05
    P(.) = 3.831636e-02
    P(</s>) = 4.395448e-02
    P(Pirate,Manager,Paul,Stone,was,suspended,.,</s>) = 3.425414e-28
    3.425414143859905e-28

    >>> model1.perplexity('Pirate Manager Paul Stone was suspended .'.split())
    8387.111491076488

Bigrams:

    >>> model2 = NGramMLE(2)
    >>> model2.train(brownPart('a'))
    >>> model2.estimate()

    >>> model2.p('Pirate Manager Paul Stone is suspended .'.split())
    P(Pirate|<s>) = 2.163098e-04
    P(Manager|Pirate) = 5.000000e-01
    P(Paul|Manager) = 2.500000e-01
    P(Stone|Paul) = 1.666667e-01
    P(is|Stone) = 2.500000e-01
    P(suspended|is) = 1.366120e-03
    P(.|suspended) = 5.000000e-01
    P(</s>|.) = 1.000000e+00
    P(<s>,Pirate,Manager,Paul,Stone,is,suspended,.,</s>) = 7.695446e-10
    7.695446108335331e-10

    >>> model2.perplexity('Pirate Manager Paul Stone is suspended .'.split())
    20.04317875932377

    >>> model2.perplexity('Pirate Manager Paul Stone was suspended .'.split())
    inf

Add One models
------------------

Unigrams:

    >>> model1 = NGramLaplace(1)
    >>> model1.train(brownPart('a'))
    >>> model1.estimate()

    >>> model1.p('Pirate Manager Paul Stone is suspended .'.split())
    P(Pirate) = 2.508949e-05
    P(Manager) = 4.181581e-05
    P(Paul) = 5.854213e-05
    P(Stone) = 4.181581e-05
    P(is) = 6.130198e-03
    P(suspended) = 2.508949e-05
    P(.) = 3.371191e-02
    P(</s>) = 3.867126e-02
    P(Pirate,Manager,Paul,Stone,is,suspended,.,</s>) = 5.149668e-28
    5.1496677366029e-28

    >>> model1.perplexity('Pirate Manager Paul Stone is suspended .'.split())
    7912.564366455823
    
    >>> model1.p('Pirate Manager Paul Stone was suspended .'.split())
    P(Pirate) = 2.508949e-05
    P(Manager) = 4.181581e-05
    P(Paul) = 5.854213e-05
    P(Stone) = 4.181581e-05
    P(was) = 6.004750e-03
    P(suspended) = 2.508949e-05
    P(.) = 3.371191e-02
    P(</s>) = 3.867126e-02
    P(Pirate,Manager,Paul,Stone,was,suspended,.,</s>) = 5.044286e-28
    5.044285722893428e-28
    
    >>> model1.perplexity('Pirate Manager Paul Stone was suspended .'.split())
    7935.970521770169

Bigrams:

    >>> model2 = NGramLaplace(2)
    >>> model2.train(brownPart('a'))
    >>> model2.estimate()

    >>> model2.p('Pirate Manager Paul Stone is suspended .'.split())
    P(Pirate|<s>) = 2.590634e-07
    P(Manager|Pirate) = 3.993031e-04
    P(Paul|Manager) = 2.395818e-04
    P(Stone|Paul) = 1.711299e-04
    P(is|Stone) = 2.395818e-04
    P(suspended|is) = 1.634255e-06
    P(.|suspended) = 3.993031e-04
    P(</s>|.) = 5.989546e-04
    P(<s>,Pirate,Manager,Paul,Stone,is,suspended,.,</s>) = 3.971539e-34
    3.971538879578363e-34

    >>> model2.perplexity('Pirate Manager Paul Stone is suspended .'.split())
    59098.61615887918

    >>> model2.p('Pirate Manager Paul Stone was suspended .'.split())
    P(Pirate|<s>) = 2.590634e-07
    P(Manager|Pirate) = 3.993031e-04
    P(Paul|Manager) = 2.395818e-04
    P(Stone|Paul) = 1.711299e-04
    P(was|Stone) = 1.197909e-04
    P(suspended|was) = 8.341986e-07
    P(.|suspended) = 3.993031e-04
    P(</s>|.) = 5.989546e-04
    P(<s>,Pirate,Manager,Paul,Stone,was,suspended,.,</s>) = 1.013627e-34
    1.0136274368840323e-34

    >>> model2.perplexity('Pirate Manager Paul Stone was suspended .'.split())
    71829.5410889147

    """


if __name__ == '__main__':
    doctest.testfile('ngrams_test.py')