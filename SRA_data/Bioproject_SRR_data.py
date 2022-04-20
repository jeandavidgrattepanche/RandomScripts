import re, sys, os, time
from sys import argv
from Bio import SeqIO
from Bio import Entrez
Entrez.email = 'xxxx@temple.edu'

def main():
	script, bioproject_list, BioP = argv
	if BioP[0].lower() == 'y':
		lr=0; check= 0
		for data in open(bioproject_list):
			dataname = data.split('\n')[0]
			print("Downloading and preparing ",dataname)
			handle = Entrez.esearch(db="sra", term=dataname, RetMax=1000)
			records = Entrez.read(handle)
			print(dataname, '\t',records["Count"])
# 			os.system("esearch -db sra -query "+dataname+' | efetch -format runinfo | cut -d "," -f 1 >> SRR_numbers.txt')
			os.system("esearch -db sra -query "+dataname+" | efetch -format runinfo > "+dataname+'2.tsv | cut -d "," -f 1 > SRR_numbers.txt')
			time.sleep(2)

		for SRRnumber in open("SRR_numbers.txt"):	
			lr=0; check= 0
		# 		print(SRRnumber[0:3])
			if SRRnumber[0:3] != "Run" and SRRnumber.split('\n')[0] != "":
				print("Downloading and preparing ",SRRnumber.split('\n')[0])
				while check == 0:
					os.system('fasterq-dump --split-files --gzip '+SRRnumber.split('\n')[0] + '--outdir $PWD/ExampleFiles/RawData/')
	elif BioP[0].lower() == 'n':
		for SRRnumber in open(bioproject_list):	
			lr=0; check= 0
		# 		print(SRRnumber[0:3])
			if SRRnumber[0:3] != "Run" and SRRnumber.split('\n')[0] != "":
				print("Downloading and preparing ",SRRnumber.split('\n')[0])
				while check == 0:
					os.system('fasterq-dump --split-files --gzip '+SRRnumber.split('\n')[0] + '--outdir $PWD/ExampleFiles/RawData/')
	else:
		print("************** \n Error in arguments \n example python3 Bioproject_SRR_ data.py list_of_Accession [y/n] \n y if you use Bioproject accession \n n if you use SRR numbers \n ********************")					
main()