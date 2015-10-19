## test program for grading hwk #2

# use version of fsa from current working directory
import sys
sys.path = [ '.' ] + sys.path

from fsa import NFSA

try:
    x = NFSA({ 0 : {'a' : [0, 1], '' : [1]},
               1 : {'b' : [1, 2], '' : [2]},
               2 : {'c' : [2, 3], '' : [3]},
               3 : {'d' : [3, 4], '' : [4]},
               4 : {'' : [0]} },
               [4])
except ValueError:
    print 'x has an epsilon loop'

try:
    y = NFSA({ 0 : {'a' : [0, 1], '' : [2]},
               1 : {'b' : [1, 2]},
               2 : {'c' : [2, 3], '' : [3]},
               3 : {'d' : [3, 4], '' : [4]},
               4 : {'' : [2]} },
               [4])
except ValueError:
    print 'y has an epsilon loop'
