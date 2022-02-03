#!/usr/bin/python3

__author__ = "Jean-David Grattepanche"
__version__ = "3, December 1, 2016"
__email__ = "jeandavid.grattepanche@gmail.com"


import sys
import os
import re
from Bio import SeqIO
from sys import argv

seqlistF = []
seqlistR = []
rename= {}
morpholist = []
uniqseqlist= []
def checkprimer(seqfile, primerfile):	
	j=0; k=0; l=0; n=0
	for Seq in SeqIO.parse(open(seqfile),'fasta'):
		j=j+1
		for line in open(primerfile.split('.')[0]+ "with1_2mismatchF.txt",'r'):
			primerseq = line.split('\t')[1].split('\n')[0]
			primer = line.split('\t')[0]
			if primerseq in str(Seq.seq).upper():
				sequence= Seq.seq.split(primerseq)[1]
				if Seq.id not in seqlistF:
					seqlistF.append(Seq.id)
					k=k+1
					out0=open("primercheck_results.txt",'a')
					out0.write(primer + '\t'+ primerseq + '\t'+ Seq.id + '\t' + str(sequence) +'\n')
					out0.close()
	for line1 in open("primercheck_results.txt",'r'):
		for line2 in open(primerfile.split('.')[0]+ "with1_2mismatchR.txt",'r'):
			primerseq2 = line2.split('\t')[1].split('\n')[0]
			primer2 = line2.split('\t')[0]
			if primerseq2 in str(line1.split('\n')[0].split('\t')[3]):
				sequence2=line1.split('\t')[3].split(primerseq2)[0]
				if line1.split('\t')[2] not in seqlistR:
					seqlistR.append(line1.split('\t')[2])
					l=l+1
					out1=open("primercheck_results_both.txt",'a')
					out1.write(primer2 + '\t'+ primerseq2 + '\t'+ line1.split('\t')[2] + '\t' + str(len(str(sequence2))) +'\n')
					out1.close()
		print("s=",j,"F=", k ,"B=", l)
		
	
def main():
	script, seqfile, primerfile = argv 
	#create primers list with 1 or 2 mismatches:
	for line in open(primerfile,'r'):
		primerFlist = []
		primerRlist = []
		primerseq = line.split('\t')[1].split('\n')[0]
		primer = line.split(':')[0]
		if primer.split('_')[1] == "F":
			primerfileupdateF = open(primerfile.split('.')[0]+ "with1_2mismatchF.txt",'a')
			primerfileupdateF.write(primer + '\t' + primerseq + '\n')
			primerfileupdateF.close()
			primerFlist.append(primerseq)
			for i in range(0,len(primerseq)):
				for char in ["A","T","C","G","R","Y","S","W","K","M","B","D","H","V","N",""]:
					if char != primerseq[i]:
						primerseqFb = primerseq[:i] + char + primerseq[(i+1):] 
#						print(primerseq, primerseqFb)
						if primerseqFb not in primerFlist:
#							print("primer added")
							primerFlist.append(primerseqFb)
							primerfileupdateF = open(primerfile.split('.')[0]+ "with1_2mismatchF.txt",'a')
							primerfileupdateF.write(primer+"_1" + '\t' + primerseqFb + '\n')
							primerfileupdateF.close()
							for m in range(0,len(primerseq)):
								for char2 in ["","A","T","C","G","R","Y","S","W","K","M","B","D","H","V","N"]:
									if char2 != primerseqFb[m]:
										primerseqFc = primerseqFb[:m] + char2 + primerseqFb[(m+1):] 
#										print(primer, int(i), primerseqFb)
										if primerseqFc not in primerFlist:
											primerFlist.append(primerseqFc)
											primerfileupdateF = open(primerfile.split('.')[0]+ "with1_2mismatchF.txt",'a')
											primerfileupdateF.write(primer+"_2" + '\t' + primerseqFc + '\n')
											primerfileupdateF.close()
		elif primer.split('_')[1] == "R":
			primerfileupdateR = open(primerfile.split('.')[0]+ "with1_2mismatchR.txt",'a')
			primerfileupdateR.write(primer + '\t' + primerseq + '\n')
			primerfileupdateR.close()
			primerRlist.append(primerseq)
			for i in range(0,len(primerseq)):
				for char in ["A","T","C","G","R","Y","S","W","K","M","B","D","H","V","N",""]:
					if char != primerseq[i]:
						primerseqRb = primerseq[:i] + char + primerseq[(i+1):] 
#						print(primerseq, primerseqRb)
						if primerseqRb not in primerRlist:
#							print("primer added")
							primerRlist.append(primerseqRb)
							primerfileupdateR = open(primerfile.split('.')[0]+ "with1_2mismatchR.txt",'a')
							primerfileupdateR.write(primer+"_1" + '\t' + primerseqRb + '\n')
							primerfileupdateR.close()
							for m in range(0,len(primerseq)):
								for char2 in ["","A","T","C","G","R","Y","S","W","K","M","B","D","H","V","N"]:
									if char2 != primerseqRb[m]:
										primerseqRc = primerseqRb[:m] + char2 + primerseqRb[(m+1):] 
#										print(primer, int(i), primerseqRb)
										if primerseqRc not in primerRlist:
											primerRlist.append(primerseqRc)
											primerfileupdateR = open(primerfile.split('.')[0]+ "with1_2mismatchR.txt",'a')
											primerfileupdateR.write(primer+"_2" + '\t' + primerseqRc + '\n')
											primerfileupdateR.close()
		else:
			print("ERROR!", primer)
	checkprimer(seqfile,primerfile)
main()