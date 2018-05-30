#!/usr/bin/python3

__author__ = "Jean-David Grattepanche"
__version__ = "1, May 29, 2018"
__email__ = "jeandavid.grattepanche@gmail.com"


import string
import re
import sys
import os
from sys import argv
from Bio import SeqIO
from Bio.Blast import NCBIXML



def main():
	script,  seqfile, xmlfile, readco, evalueco  = argv
	Seqdict= {}; a= 0; b=0;j=0; k=0
	for seq in SeqIO.parse(seqfile,'fasta'):
		Seqdict[seq.description] = str(seq.seq)
#	print(len(Seqdict))
	for blast_record in NCBIXML.parse(open(xmlfile)):
		if blast_record.descriptions:
			for i in range(1):
				b += 1
				evalue = float(blast_record.alignments[i].hsps[0].expect)
				ID = blast_record.query
				cov = int(blast_record.query.split('Cov')[1].split('_')[0])
				if cov >= int(readco):
					a+=1
				if evalue <= float(evalueco):
					j+=1
					
				if cov >= int(readco) and evalue <= float(evalueco):
					k+=1
					print(ID)
	print("number of transcripts =" ,len(Seqdict), 'in AA file or ', str(b),' in xml')
	print("Coverage < ", str(readco), " = ", str(a), ' \n evalue > ', str(evalueco), ' = ', str(j),' \n Both cutoffs = ', str(k))
					
main()