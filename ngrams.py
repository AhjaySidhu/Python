#!/usr/bin/env python

"""
Simple n-gram models 

@author: Rob Malouf
@organization: Dept. of Linguistics, San Diego State University
@contact: rmalouf@mail.sdsu.edu
@version: 2
@date: 18-March-2015
@since: 18-March-2010
"""

from nltk import ngrams
from nltk.corpus import brown
from collections import defaultdict
from operator import itemgetter
import math

def brownPart(part):
    """Return one section of the Brown corpus as a list of sentences."""
    return brown.sents([f for f in brown.fileids() if f.startswith('c'+part)])

class NGram(object):

    """Generic ngram models"""

    def __init__(self, n):

            self.n = n
            self.counts = defaultdict(float)
            self.counts1 = defaultdict(float)
            self.words = 0.0

    def train(self, text):
        """Count n-gram occurrences in a list of sentences."""
        for sentence in text:

            # add beginning and ending pseudo-words
            sentence = ['<s>'] * (self.n-1) + sentence + ['</s>']

            # total size of corpus
            self.words += len(sentence)

            # count n grams
            for g in ngrams(sentence, self.n):
                self.counts[g] += 1.0

            # count n-1 grams (so long as n > 1)
            if self.n > 1:
                for g in ngrams(sentence, self.n-1):
                    self.counts1[g] += 1.0

    def estimate(self):
       """Construct a probability distribution from a dictionary of n-gram counts."""
       raise(NotImplementedError)
        
    def p(self, sentence, trace=True):
        """Find the likelihood of a sentence using an ngram model."""

        # add beginning and ending pseudo-words
        sentence = ['<s>'] * (self.n-1) + sentence + ['</s>']

        q = 1.0
        for g in ngrams(sentence, self.n):

            if self.n == 1:
                # if n == 1, P(w) = C(w) / N
                q1 = self.probs[g]
                if trace:
                    print 'P(%s) = %e'%(g[-1], q1)
            else:
                # otherwise, P(wi|w1,...,wi-1) = P(w1,...,wi) / P(w1,...,wi-1)
                if self.probs1[g[:-1]] == 0.0:
                    # we'll define 0.0/0.0==0.0, to avoid division by zero errors
                    q1 = 0.0
                else:
                    q1 = self.probs[g] / self.probs1[g[:-1]]
                if trace:
                    print 'P(%s|%s) = %e'%(g[-1],','.join(g[:-1]),q1)
            q *= q1

        if trace:
            print 'P(%s) = %e'%(','.join(sentence),q)
        return q
        
    def perplexity(self, sentence):        
        """Compute perplexity of a sentence given a model. (you need to fill this in)"""
        LP = 0.0
        for g in self.n:
            LP = LP + math.log(q,2)
        LP = LP * -(1/self.n)
        PP = 2**LP
        return float(PP)
       

class NGramMLE(NGram):

    """Maximum-likelihood probabilities"""

    def estimate(self):
        """Construct a maximum likelihood probability distribution from a dictionary of n-gram counts."""
        self.probs = defaultdict(float)
        for g in self.counts:
            self.probs[g] = self.counts[g] / self.words
        if self.n > 1:
            self.probs1 = defaultdict(float)
            for g in self.counts1:
                self.probs1[g] = self.counts1[g] / self.words

class NGramLaplace(NGram):

    """Laplace probabilities"""

    def estimate(self):
        """Construct a  probability distribution
           from a dictionary of n-gram counts using add one smoothing."""

        self.probs = defaultdict(float)
        self.probs1 = defaultdict(float)
        for g in self.counts:
            self.probs[g] = self.counts[g] + 1 / self.words + self.n
            if self.n > 1:
                self.probs1 = defaultdict(float)
                for g in self.counts1:
                    self.probs1[g] = self.counts1[g] + 1 / self.words + self.n

if __name__ == '__main__':

    for n in [1, 2]:
    
        print 'MLE', n, 'grams'
        print

        model = NGramMLE(n)
        model.train(brownPart('a'))
        model.estimate()

        q = model.p('Pirate Manager Paul Stone is suspended .'.split())
        print
        q = model.p('Pirate Manager Paul Stone was suspended .'.split())
        print

        model = NGramLaplace(n)
        model.train(brownPart('a'))
        model.estimate()

        q = model.p('Pirate Manager Paul Stone is suspended .'.split())
        print
        q = model.p('Pirate Manager Paul Stone was suspended .'.split())
        print


