#!/usr/bin/python3

__author__ = "Jean-David Grattepanche"
__version__ = "3, June 25, 2019"
__email__ = "jeandavid.grattepanche@gmail.com"



import sys
import os
import re
import urllib.request
import time
import string
import os.path
from Bio import SeqIO
from Bio import Entrez
Entrez.email = 'XXX@smith.edu'
from sys import argv



def Rename(inputfile):
	i = 100
	print("start Adding Name")
	IDlist = []
	chars_to_remove = ["(", ")" , ":" , ";" , "[", "]", "," , "/"]
	for record in open(inputfile,'r'): 
		gbID  = record.split('\n')[0].split('.')[0]
		if gbID not in IDlist:
			IDlist.append(gbID)
	for k in range(0, len(IDlist), i):
		list = IDlist[k:k+i]
		print(k, " - ", k+i, "on", len(IDlist), "efetch batch of:", len(list), "sequences" )
		list2 = str(list).replace('[','').replace(']','').replace("'","").replace(" ","")
		print("efetch:", list2)
		try:
			time.sleep(10)
			handle = Entrez.efetch(db="nucleotide", id=list2, rettype="gb" )
			records = SeqIO.parse(handle,"gb")
		except:
			time.sleep(120)
			try:
				print("try 2")
				handle = Entrez.efetch(db="nucleotide", id=list2, rettype="gb" )
				records = SeqIO.parse(handle,"gb")
			except urllib.request.HTTPError as err:
				if err.code == 502:
					time.sleep(60)
					print("retry efetch")
					raise
		for record2 in records:
			print(record2.annotations)
			print(record2)
			ID2 = record2.annotations["accessions"][0] #.replace("_","")
			try:
				newname = record2.annotations["taxonomy"][0][0:3]+ "\t" +record2.annotations["taxonomy"][1][0:3] + "\t" +record2.annotations["taxonomy"][2][0:3] + "\t" +record2.annotations["taxonomy"][3][0:2] + "\t" +record2.annotations["taxonomy"][4][0:2] + "\t" +record2.annotations["taxonomy"][5][0:2] +  "\t" +  record2.annotations["organism"]  # need to be modified related to the taxonomy list =>record2.annotations["taxonomy"][14][0:3]
			except:
				try: 
					newname = record2.annotations["taxonomy"][0][0:3]+ "\t" +record2.annotations["taxonomy"][1][0:3] + "\t" +record2.annotations["taxonomy"][2][0:3] + "\t" +record2.annotations["taxonomy"][3][0:2] + "\t" +record2.annotations["taxonomy"][4][0:2] + "\t\t" +  record2.annotations["organism"]  # need to be modified related to the taxonomy list =>record2.annotations["taxonomy"][14][0:3]
				except:
					try: 
						newname = record2.annotations["taxonomy"][0][0:3]+ "\t" +record2.annotations["taxonomy"][1][0:3] + "\t" +record2.annotations["taxonomy"][2][0:3] + "\t" +record2.annotations["taxonomy"][3][0:2] + "\t\t\t" +  record2.annotations["organism"]  # need to be modified related to the taxonomy list =>record2.annotations["taxonomy"][14][0:3]
					except:
						try: 
							newname = record2.annotations["taxonomy"][0][0:3]+ "\t" +record2.annotations["taxonomy"][1][0:3] + "\t" +record2.annotations["taxonomy"][2][0:3] + "\t\t\t\t" +  record2.annotations["organism"]  # need to be modified related to the taxonomy list =>record2.annotations["taxonomy"][14][0:3]
						except:
							newname = "\t\t\t\t\t\t\t" + record2.annotations["organism"].replace(' ',' ')
			rename2 = newname.translate(''.join(chars_to_remove)).replace('\t','_').replace(' ','_') 
			outrename = open("Gb_seq.fas",'a')
			outrename.write('>' + rename2 + '_'+ ID2 +  '\n'+ str(record2.seq)+'\n')
			outrename.close()
			
def main():
	script, GBfile = argv
	Rename(GBfile)
main()
