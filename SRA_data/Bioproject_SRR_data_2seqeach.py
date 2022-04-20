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
			os.system("esearch -db sra -query "+dataname+' | efetch -format runinfo | cut -d "," -f 1 >> SRR_numbers.txt')
	# 		os.system("esearch -db sra -query "+dataname+" | efetch -format runinfo > "+dataname+'2.tsv | cut -d "," -f 1 > SRR_numbers.txt')
			time.sleep(2)

		for SRRnumber in open("SRR_numbers.txt"):	
			lr=0; check= 0
		# 		print(SRRnumber[0:3])
			if SRRnumber[0:3] != "Run" and SRRnumber.split('\n')[0] != "":
				print("Downloading and preparing ",SRRnumber.split('\n')[0])
				while check == 0:
					os.system('fasterq-dump --split-files --gzip '+SRRnumber.split('\n')[0] + '--outdir $PWD/ExampleFiles/RawData/')
					if os.path.isfile(SRRnumber.split('\n')[0]+'_1.fastq'):
						check = 1
					elif os.path.isfile(SRRnumber.split('\n')[0]+'.fastq'):
						print(SRRnumber.split('\n')[0])
						check = 2
					else:
						print("TRY AGAIN for ", SRRnumber.split('\n')[0])
						os.system("rm -R fasterq.tmp.*")
						check = 0
				if check == 1:		
					out = open("first2seq_part2.fasta",'a')
					x = 0
					for seq in SeqIO.parse(SRRnumber.split('\n')[0]+'_1.fastq','fastq'):
						if x < 5:
							print(seq.description, str(seq.seq))
							x+=1
							out.write('>'+ seq.description + '\n'+ str(seq.seq)+'\n')
						else:
							break
					out.close()
					print("Compressing files ",SRRnumber.split('\n')[0]," \n")
					os.system('gzip '+SRRnumber.split('\n')[0]+'*.fastq')
					print("Moving files ",SRRnumber.split('\n')[0]," to Google Drive.\n") 
					os.system('mv '+SRRnumber.split('\n')[0]+'*.fastq.gz /Volumes/GoogleDrive/My\ Drive/Amplicon_V4/done/')
					os.system('rm /Users/tuk61790/ncbi/public/sra/'+SRRnumber.split('\n')[0]+'.*')
				if check == 2:
					print("Compressing files ",SRRnumber.split('\n')[0]," \n")
					os.system('gzip '+SRRnumber.split('\n')[0]+'*.fastq')
					print("Moving files ",SRRnumber.split('\n')[0]," to Google Drive.\n") 
					os.system('mv '+SRRnumber.split('\n')[0]+'*.fastq.gz /Volumes/GoogleDrive/My\ Drive/Amplicon_V4/tocheck/')
					os.system('rm /Users/tuk61790/ncbi/public/sra/'+SRRnumber.split('\n')[0]+'.*')

	elif BioP[0].lower() == 'n':
		for SRRnumber in open(bioproject_list):	
			lr=0; check= 0
		# 		print(SRRnumber[0:3])
			if SRRnumber[0:3] != "Run" and SRRnumber.split('\n')[0] != "":
				print("Downloading and preparing ",SRRnumber.split('\n')[0])
				while check == 0:
					os.system('fasterq-dump --split-files --gzip '+SRRnumber.split('\n')[0] + '--outdir $PWD/ExampleFiles/RawData/')
					if os.path.isfile(SRRnumber.split('\n')[0]+'_1.fastq'):
						check = 1
					elif os.path.isfile(SRRnumber.split('\n')[0]+'.fastq'):
						print(SRRnumber.split('\n')[0])
						check = 2
					else:
						print("TRY AGAIN for ", SRRnumber.split('\n')[0])
						os.system("rm -R fasterq.tmp.*")
						check = 0
				if check == 1:		
					out = open("first2seq_part2.fasta",'a')
					x = 0
					for seq in SeqIO.parse(SRRnumber.split('\n')[0]+'_1.fastq','fastq'):
						if x < 5:
							print(seq.description, str(seq.seq))
							x+=1
							out.write('>'+ seq.description + '\n'+ str(seq.seq)+'\n')
						else:
							break
					out.close()
					print("Compressing files ",SRRnumber.split('\n')[0]," \n")
					os.system('gzip '+SRRnumber.split('\n')[0]+'*.fastq')
					print("Moving files ",SRRnumber.split('\n')[0]," to Google Drive.\n") 
					os.system('mv '+SRRnumber.split('\n')[0]+'*.fastq.gz /Volumes/GoogleDrive/My\ Drive/Amplicon_V4/done/')
					os.system('rm /Users/tuk61790/ncbi/public/sra/'+SRRnumber.split('\n')[0]+'.*')
				if check == 2:
					print("Compressing files ",SRRnumber.split('\n')[0]," \n")
					os.system('gzip '+SRRnumber.split('\n')[0]+'*.fastq')
					print("Moving files ",SRRnumber.split('\n')[0]," to Google Drive.\n") 
					os.system('mv '+SRRnumber.split('\n')[0]+'*.fastq.gz /Volumes/GoogleDrive/My\ Drive/Amplicon_V4/tocheck/')
					os.system('rm /Users/tuk61790/ncbi/public/sra/'+SRRnumber.split('\n')[0]+'.*')
	else:
		print("************** \n Error in arguments \n example python3 Bioproject_SRR_ data.py list_of_Accession [y/n] \n y if you use Bioproject accession \n n if you use SRR numbers \n ********************")					
main()