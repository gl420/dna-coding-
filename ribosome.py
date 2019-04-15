# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 11:34:16 2019

@author: gl273
"""

from ribosome_utils import *

f = open("Codon_Table.txt" , "r")

d = load_code (f) 
print(d) 

f = open("myoglobin.seq" , "r")

seq = load_fasta(f) [1]

print(seq)


for i in range(0, len(seq), 3):
    print(i)
    print(seq[i:i+3]) 
    codon = d[seq[i:i+3]]
    print(codon)


