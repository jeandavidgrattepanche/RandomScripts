#!/usr/bin/python3

__author__ = 'Jean-David Grattepanche'
__version__ = '4, August 21, 2018'
__email__ = 'jeandavid.grattepanche@gmail.com'



import sys
import os
import re
import time
import string
import os.path
from Bio import SeqIO
from sys import argv
listOG=[]
toosim = 0.99
seqcoverage = 0.7

def merge_files(folder):
	mergefile = open('forclustering.fasta','w+')
	print("MERGE following files")
	for taxafile in os.listdir(folder):
		if taxafile[0] != ".":
			taxaname = ('_').join(taxafile.split('_')[0:3])
			print(taxaname)
			mergefile = open('forclustering.fasta','a')
			for line2 in open(folder+'/'+taxafile, 'r'):
				if line2[0] == '>':
					mergefile.write('>'+taxaname + '_' + line2.replace('>','').replace('\n','') + '\n')
				else:
					mergefile.write(line2.replace('\n','') + '\n')
			
			mergefile.close()

	sort_cluster(folder)


def sort_cluster(folder):
	if not os.path.exists('temp/'):
		os.makedirs('temp/')
	if not os.path.exists('clusteringresults_vsearch/'):
		os.makedirs('clusteringresults_vsearch/')
	fastalist = []; fastadict= {}
	print("SORT the sequences by coverage and create a dictionnary")
	out = open('temp/forclustering_sorted.fasta','w+')
	for record in SeqIO.parse(open('forclustering.fasta','r'),'fasta'):
#		IDL  = record.description, int(len(record.seq))
		IDL  = record.description, int(record.description.split('_Cov')[1].replace('\n',''))
		fastalist.append(IDL)
		fastadict[record.description] = record.seq
	for seqlength in sorted(fastalist, reverse=True, key=lambda x: x[1]):
		out = open('temp/forclustering_sorted.fasta','a')
		out.write('>'+seqlength[0] + '\n'+ str(fastadict[seqlength[0]])+'\n')
		out.close()	
	print("CLUSTER for too similar sequences that overalp at least 70%")
	print('vsearch --cluster_fast temp/forclustering_sorted.fasta --strand both --usersort --query_cov '+str(seqcoverage)+' --id '+str(toosim) +' --uc clusteringresults_vsearch/results_forclustering.uc' )
	os.system('vsearch --cluster_fast temp/forclustering_sorted.fasta --strand both --usersort --query_cov '+str(seqcoverage)+' --id '+str(toosim) +' --uc clusteringresults_vsearch/results_forclustering.uc' )
	print("PARSE too similar: keep seed sequences (highest coverage) for each cluster")
	input2 = open('clusteringresults_vsearch/results_forclustering.uc','r')
	out2 = open('fastatokeep.fas','w+')
	out3 = open('fastatoremoved.fas','w+')
	out4 = open('fastatoremoved.uc','w+')

	for row2 in input2:
		if row2.split('\t')[0] == 'S':
			out2.write('>'+row2.split('\t')[8] + '\n' + str(fastadict[row2.split('\t')[8]])+ '\n')
		if row2.split('\t')[0] == 'H':
			master = row2.split('\t')[9].replace('\n','')
			clustered =  row2.split('\t')[8].replace('\n','')
			Covmaster = int(master.split('_Cov')[1].replace('\n',''))
			Covclustered = int(clustered.split('_Cov')[1].replace('\n',''))
			master8dig = ('_').join(master.split('_')[0:3])[:-2]
			clustered8dig = ('_').join(clustered.split('_')[0:3])[:-2]
			print(master, master8dig, Covmaster)
			if master8dig == clustered8dig:
				out2.write('>'+row2.split('\t')[8] + '\n' + str(fastadict[row2.split('\t')[8]])+ '\n')
			elif float(Covmaster/Covclustered) < 10:
				out2.write('>'+row2.split('\t')[8] + '\n' + str(fastadict[row2.split('\t')[8]])+ '\n')
			elif Covclustered >= 50:				
				out2.write('>'+row2.split('\t')[8] + '\n' + str(fastadict[row2.split('\t')[8]])+ '\n')
			else:
				out3.write('>'+row2.split('\t')[8] + '\n' + str(fastadict[row2.split('\t')[8]])+ '\n')
				out4.write(row2+ '\n')
					
def main():
	print('\n\n*******************************************************************')
	print('This script:  \n\t Create cluster and remove sequence too similar \n')
	print('\n\npython3 XSpeciesContamination.py folder\n\n')
	print('\nFor example\npython3 XSpeciesContamination.py trimmed200p5 \n\n')
	print('*******************************************************************\n\n')
	script, folder = argv
	merge_files(folder)
# 	sort_cluster(folder)

main()