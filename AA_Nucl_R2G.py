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
from Bio.SeqUtils import GC

seqdict = {}; seqlen=[]; seqGC=[]

def main():
	script, seqfileAA, Seqfilenucl = argv
	for seq in SeqIO.parse(open(Seqfilenucl,'r'),'fasta'):
		seqdict[seq.description.split('_')[1]] = str(seq.seq)
	out = open(seqfileAA.split('.fasta')[0]+ "_nucl.fasta",'w')
	for seqAA in SeqIO.parse(open(seqfileAA,'r'),'fasta'):
		out.write('>'+ seqAA.description + '\n' + seqdict[seqAA.description.split('_')[5]] + '\n')
main()
