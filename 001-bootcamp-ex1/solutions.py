import statistics
import numpy as np

def biggest(l):
    return max(l)

def average(l):
    return statistics.mean(l)

def longest(s):
    return max(s,key=len)

def first_space(l):
    return [word for word in l if ' ' in word][0]

def freq(s):
    d = dict.fromkeys(list(s))
    for key in d.keys(): d[key] = s.count(key)
    return d

def panagram(s):
    chars = list(s)
    chars = [char for char in chars if char != ' ']
    return True if len(list(dict.fromkeys(chars))) == 26 else False

def abbreviate(s):
    return ''.join([word[0] for word in s.split() if word[0].isupper()])

def split(amount, denominations):
    counts = [0]*len(denominations)    
    i = 0    
    while i < len(denominations):
        if amount >= denominations[i]:
            amount -= denominations[i]
            counts[i] += 1
            i -= 1
        i += 1
    d = dict(zip(denominations,counts))
    zeros = [key for key in d.keys() if d[key] == 0]
    for i in range(len(zeros)): del d[zeros[i]]
    return d
