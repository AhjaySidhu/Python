import doctest

"""
FSA module
==========

Import everything:

    >>> from fsa import *

Deterministic FSAs
------------------

Make a DFSA:

    >>> fsa1 = DFSA( { 0: { 'b': 1 },           # state 0  b => 1
    ...                1: { 'a':2 },            # state 1  a => 2
    ...                2: { 'a':3 },            # state 2  a => 3
    ...                3: { 'a':3, '!':4},      # state 3  a => 3,  ! => 4
    ...                4: {  } },               # state 4  undef for everything.
    ...               [ 4 ])
    >>> print fsa1
    { DFSA
      Alphabet : set(['a', '!', 'b'])
      0: initial
        b => [1]
      1:
        a => [2]
      2:
        a => [3]
      3:
        a => [3]
        ! => [4]
      4: final
    }

Test recognize method for DFSAs:

    >>> fsa1.recognize('baa!', trace=True)
    Obs 0 at state 0
    Obs 1 at state 1
    Obs 2 at state 2
    Obs 3 at state 3
    Obs 4 at state 4
    ACCEPT
    True
    >>> fsa1.recognize('baa!')
    True
    >>> fsa1.recognize('baaaaa!')
    True
    >>> fsa1.recognize('baaaxaa!')
    False
    >>> fsa1.recognize('ba!')
    False
    >>> fsa1.recognize('')
    False

Test the complement method:

    >>> C = fsa1.complement()
    >>> print C
    { DFSA
      Alphabet : set(['a', '!', 'b'])
      0: initial final
        a => ['sink']
        ! => ['sink']
        b => [1]
      1: final
        a => [2]
        ! => ['sink']
        b => ['sink']
      2: final
        a => [3]
        ! => ['sink']
        b => ['sink']
      3: final
        a => [3]
        ! => [4]
        b => ['sink']
      4:
        a => ['sink']
        ! => ['sink']
        b => ['sink']
      sink: final
        a => ['sink']
        ! => ['sink']
        b => ['sink']
    }
    >>> C.recognize('baa!')
    False
    >>> C.recognize('baaaaa!')
    False
    >>> C.recognize('baaaxaa!')
    False
    >>> C.recognize('ba!')
    True
    >>> C.recognize('')
    True

Make sure the complement method hasn't modified the original FSA:

    >>> fsa1.recognize('baaaaa!')
    True
    >>> fsa1.recognize('baaaxaa!')
    False

Some invalid DFSAs

    >>> x = DFSA( { 0 : { 'x' : 1 } }, [ 0 ] )
    Traceback (most recent call last):
       ...
    ValueError: 1 not a valid state

    >>> x = DFSA( { 0 : { 'x' : 0 } }, [ 1 ] )
    Traceback (most recent call last):
       ...
    ValueError: 1 is not a valid final state

    >>> x = DFSA( { 0 : { 'x' : [0, 1] }, 1 : {}  }, [ 1 ] )
    Traceback (most recent call last):
       ...
    ValueError: non-deterministic transitions not allowed in DFSAs

    >>> x = DFSA( { 0 : { 'x' : [0, 1] }, 1 : { '': 2}, 2 : { } }, [ 1 ] )
    Traceback (most recent call last):
       ...
    ValueError: epsilon transitions not allowed in DFSAs

Non-deterministic FSAs
----------------------

    >>> fsa2 = NFSA( { 0: { 'b' : 1 },
    ...                1: { 'a' : 2 },
    ...                2: { 'a' : [2, 3] },
    ...                3: { ''  : 2,
    ...                     '!' : 4 },
    ...                4: { } },
    ...                [ 4 ] )
    >>> print fsa2
    { NFSA
      Alphabet : set(['a', '', 'b', '!'])
      0: initial
        b => [1]
      1:
        a => [2]
      2:
        a => [2, 3]
      3:
         => [2]
        ! => [4]
      4: final
    }

Test recognition:

    >>> fsa2.recognize('baa!', trace=True)
    Obs 0 at state 0
    Obs 1 at state 1
    Obs 2 at state 2
    Obs 3 at state 3
    Obs 4 at state 4
    ACCEPT
    True
    >>> fsa2.recognize('baa!', depth_first=False, trace=True)
    Obs 0 at state 0
    Obs 1 at state 1
    Obs 2 at state 2
    Obs 3 at state 2
    Obs 3 at state 3
    Obs 3 at state 2
    Obs 4 at state 4
    ACCEPT
    True
    >>> fsa2.recognize('baaaaa!')
    True
    >>> fsa2.recognize('baaaxaa!')
    False
    >>> fsa2.recognize('ba!')
    False
    >>> fsa2.recognize('')
    False

Some invalid NFSAs

    >>> x = NFSA( { 0 : { 'x' : 1 } }, [ 0 ] )
    Traceback (most recent call last):
       ...
    ValueError: 1 not a valid state

    >>> x = NFSA( { 0 : { 'x' : 0 } }, [ 1 ] )
    Traceback (most recent call last):
       ...
    ValueError: 1 is not a valid final state

    >>> x = NFSA( { 0 : { 'x' : [0, 1] }, 1 : {}  }, [ 1 ] )

    >>> x = NFSA( { 0 : { 'x' : [0, 1] }, 1 : { '': 2}, 2 : { } }, [ 1 ] )

End of tests
"""

if __name__ == '__main__':
    doctest.testfile('fsa_test.py')