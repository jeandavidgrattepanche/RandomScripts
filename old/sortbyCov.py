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
	script, seqfile = argv
	for seq in SeqIO.parse(open(seqfile,'r'),'fasta'):
		seqdict[seq.description + '-'+seq.description.split('Cov')[1].split('_')[0]] = str(seq.seq)
	sortedseq = sorted(seqdict.items(), key=lambda x: float(x[0].split('-')[1]) ,reverse=True)
	out3 = open(seqfile.split('.fasta')[0]+ "_Covsorted.fasta",'w')
	out4 = open(seqfile.split('.fasta')[0]+ "_Covsorted.tsv",'w')
	out4.write('seqname\tlength\tCoverage\n')
	for element in sortedseq:
		out4.write( element[0].split('-')[0]+ '\t'+ element[0].split('-')[0].split('Len')[1].split('_')[0] +'\t' + element[0].split('-')[1] +'\n')
		if int(element[0].split('-')[1]) >= 10:
			out3.write('>'+element[0].split('-')[0] + '\n' + element[1] + '\n')
main()
