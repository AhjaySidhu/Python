#!/usr/bin/python

"""
Basic HMM bigram tagger
@author: Rob Malouf
@organization: Dept. of Linguistics, San Diego State University
@contact: rmalouf@mail.sdsu.edu
@version: 1
@date: 7-May-2015
"""

from itertools import izip
from collections import defaultdict, Counter

from nltk.corpus import brown

NINF=-float('inf')

### Main Program

class HMMTagger(object):

    def __init__(self,tagged):

        # tag unigram counts: tagCount[tag]
        tagCount = Counter()              

        # tag bigram counts: tagtagCount[(tag1, tag2)]
        tagtagCount = Counter()

        # word/tag pair counts: wordtagCount[(word, tag)]
        wordtagCount = Counter()

        # vocabulary
        self.words = set()
        self.s0  = '<s>'  ## start state

        ## count events in training data    

        for sent in tagged:

            # start with the start tag <s>
            prevtag = self.s0
            tagCount[self.s0] += 1
                    
            for word,tag in sent + [('</s>','</s>')]:

                tagCount[tag] += 1
                tagtagCount[(prevtag, tag)] += 1
                self.words.add(word)
                wordtagCount[(word, tag)] += 1

                prevtag = tag

        self.tags = set(tagCount.keys())
                           
        ## smooth counts and compute probs

        # transition probabilities (using add-one smoothing)

        N = len(tagCount)       # number of tags
        self.A = dict()
        for tag1 in tagCount:
            for tag2 in tagCount:
                self.A[(tag1, tag2)] = (tagtagCount[(tag1, tag2)] + (1.0 / 2.0)) /  float(tagCount[tag1] + (N / 2.0))

        # emission probabilities (using add-one smoothing)
        
        V = len(self.words)     # number of words
        self.B = defaultdict(lambda: 1.0 / V)        
        for (word, tag) in wordtagCount:
            self.B[(word, tag)] = (wordtagCount[(word, tag)] * tagCount[tag] + (1.0 / 2.0)) / float(tagCount[tag] + (V / 2.0))        

    def tag(self,sent):

        ## Initialize trellis and backtrace

        trellis = [ dict.fromkeys(self.tags, NINF) ]
        trellis[0][self.s0] = 1.0
        backtrace = [ dict.fromkeys(self.tags, None) ]

        ## Fill in the rest of the trellis

        for word in sent+['</s>']:

            # add an empty column
            trellis.append(dict())
            backtrace.append(dict())

            for tag2 in self.tags:

                # find most likely path to this state
                a = NINF
                for tag1 in self.tags:
                    p = trellis[-2][tag1] * self.A[(tag1, tag2)]
                    if p > a:
                        a = p
                        b = tag1

                # compute viterbi prob
                trellis[-1][tag2] = a * self.B[(word, tag2)]
                backtrace[-1][tag2] = b

        ## Extract best tag sequence from trellis

        t = -1
        best = max((p,t) for (t,p) in trellis[t].iteritems())[1]
        path = [ ]
        while best != None:
            path.append(best)
            best = backtrace[t][best]
            t -= 1
        path.reverse()
        
        return zip(sent,path[1:-1])

    def accuracy(self,testdata):
        """Compute the accuracy of a tagger against a 'gold standard'"""

        right = 0.0
        n = 0.0
        for sent in testdata:
            result = self.tag([w for w,t in sent])
            for (w1,t1),(w2,t2) in izip(sent,result):
                if t1 == t2:
                    right += 1.0
                n += 1.0
        return right / n                


def main():
   
    trainData = brown.tagged_sents(categories=['adventure','editorial'])
    testData = brown.tagged_sents(categories='news')[:25]
    
    # train tagger
    tagger = HMMTagger(trainData)
    
    # tag a sample sentence
    print tagger.tag(brown.sents(categories='news')[2])
    print
    
    # compute accuracy on the test data
    print 'Basic HMM accuracy = %.2f'%(tagger.accuracy(testData)*100)

if __name__ == '__main__':
    main()


