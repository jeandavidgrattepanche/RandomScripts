#!/usr/bin/python3

__author__ = "Jean-David Grattepanche"
__version__ = "1, February 7, 2017"
__email__ = "jeandavid.grattepanche@gmail.com"


import string
import re
import sys
import os
from sys import argv
from Bio import SeqIO


seqdict = {}

def main():
	script, seqfileAA, tablefile = argv
	for seqAA in SeqIO.parse(seqfileAA,'fasta'):
		seqdict[seqAA.description] = str(seqAA.seq)
	out = open(seqfileAA.split('.fasta')[0]+ "_B2G.fasta",'w')
	for row in open(tablefile,'r'):
		if row.split('\t')[0] != '':
			out.write('>'+ row.split('\t')[0] + '\n' + seqdict[row.split('\t')[0]] + '\n')
main()