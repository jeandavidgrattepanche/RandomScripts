#!/usr/bin/python3

__author__ = "Jean-David Grattepanche"
__version__ = "1, August 31, 2018"
__email__ = "jeandavid.grattepanche@gmail.com"


import re,os, sys
from Bio import SeqIO
from Bio import Phylo
from sys import argv



#take a leaf, compare it to its sister
def checkClade(tree):
	out = open('rename.tree','w+')
	for line in open(tree,'r'):
		for element in line.split('OT'):
			if element.startswith('U'):
				new_element= element.split(':')[0].split('_')[0].replace('U','OTU')+':'+(':').join(element.split(':')[1:])
				out.write(new_element.replace("QUERY___",""))
			else:
				out.write(element.replace("QUERY___",""))
				
def main():
	script, treefile = argv	
	checkClade(treefile)	
main()