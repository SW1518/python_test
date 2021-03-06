import sys, pprint
import os
import fileinput
import re

pprint.pprint(sys.path)
def hello():
    print("hello,world")

def test():
    hello()

def add_linenum():
    for line in fileinput.input(inplace=True):
        line = line.rstrip()
        num = fileinput.lineno()
        print('{:50} # {:2d}'.format(line,num))
def poker():
    values = list(range(1,10)) + "Jack Queen King".split()
    suits = 'diamonds clubs hearts spades'.split()
    deck = ['{} {}'.format(v,s) for v in values for s in suits]

def find_sender():
    pat = re.compile('From: (.*) <.*?>$')
    for line in fileinput.input():
        m = pat.match(line)
        if m : print(m.group(1))

if __name__ == '__main__':
    deck = {}
    poker()
    pprint.pprint(deck)
    test()
    while (deck): input(deck.pop())