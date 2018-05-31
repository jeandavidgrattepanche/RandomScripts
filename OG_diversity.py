import os, sys, math
from Bio import SeqIO

def geneExpChan(tsvfile, cutoff, seqfile):
	OGdict = {}
	for record in SeqIO.parse(seqfile,'fasta'):
		OGdict[record.id.split('_')[1]] = "OG5_"+record.id.split('_')[-1]
	with open(tsvfile,'r') as f:
		header = f.readline().split('\t'); newheader = []
		contmi = [i for i,x in enumerate(header) if x == "Mm_mi_p0z0"]
		print contmi[0], header[contmi[0]]
		contna = [i for i,x in enumerate(header) if x == "Mm_na_p0z0"]
		print contna[0], header[contna[0]]
		allna = [i for i,x in enumerate(header) if x[0:2] == "Mm" and x.split('_')[1] == "na" and x[6] == "p" and x[6:10] != "p0z0"]
		print allna
		for j in  range(0,len(allna)):
			print allna[j], header[allna[j]]
			newheader.append(header[allna[j]])
		allmi = [i for i,x in enumerate(header) if x[0:2] == "Mm" and x.split('_')[1] == "mi" and x[6] == "p" and x[6:10] != "p0z0"]
		print allmi
		for j in  range(0,len(allmi)):
			print allmi[j], header[allmi[j]]
			newheader.append(header[allmi[j]])
		print newheader
	dict = {}; trans = []; z = 0
	out1 = open('rpkm_Log_all_noPA_b.tsv','w+')
	out1.write('\t'+ ('\t').join(newheader) +'\n')	
	for row in open(tsvfile,'r'):
		list= []; z += 1
		if row.split('\t')[0].split('_')[0] == "Contig":
			trans.append(row.split('\t')[0])
			for j in  range(0,len(allna)):
				if float(row.split('\t')[contna[0]]) > 0 and float(row.split('\t')[allna[j]]) > 0:
					if float(row.split('\t')[allna[j]]): # > 0 and float(row.split('\t')[allna[j]]) <= 10:
						valnax =  1
# 					elif float(row.split('\t')[allna[j]]) > 10 and float(row.split('\t')[allna[j]]) <= 100:
# 						valnax = 2
# 					elif float(row.split('\t')[allna[j]]) > 100 and float(row.split('\t')[allna[j]]) <= 1000:
# 						valnax = 3
# 					elif float(row.split('\t')[allna[j]]) > 1000 and float(row.split('\t')[allna[j]]) <= 10000:
# 						valnax = 4
# 					elif float(row.split('\t')[allna[j]]) > 10000 :
# 						valnax = 5
					else:
						print("BREAK")
				else:
					valnax = 0
				list.append(str(valnax))
			for j in  range(0,len(allmi)):
				if float(row.split('\t')[contmi[0]]) > 0 and float(row.split('\t')[allmi[j]]) > 0:
					if float(row.split('\t')[allmi[j]]) > 0 : #and float(row.split('\t')[allmi[j]]) <= 10:
						valmix =  1
# 					elif float(row.split('\t')[allmi[j]]) > 10 and float(row.split('\t')[allmi[j]]) <= 100:
# 						valmix = 2
# 					elif float(row.split('\t')[allmi[j]]) > 100 and float(row.split('\t')[allmi[j]]) <= 1000:
# 						valmix = 3
# 					elif float(row.split('\t')[allmi[j]]) > 1000 and float(row.split('\t')[allmi[j]]) <= 10000:
# 						valmix = 4
# 					elif float(row.split('\t')[allmi[j]]) > 10000 :
# 						valmix = 5
					else:
						print("BREAK")
				else:
					valmix = 0
				list.append(str(valmix))
			print row.split('\t')[0]
			dict[row.split('\t')[0]] = list
	print z, " transcripts"
	list2 = []; listm=[]
	for transcript in trans:
		sum=0
		for element in dict[transcript]:
			sum+= float(element)
		if sum != 0:# and sum != 22 : 
			try:
				out1.write(OGdict[transcript.split('_')[1]] + '\t' + ('\t').join(dict[transcript])+ '\n')
				list2.append(transcript)
			except:
				listm.append(transcript)
	print len(list2), "transcript > ", cutoff
	print "Missing: ", len(listm)
	print listm
def main():
	tsvfile = sys.argv[1]
	cutoff = sys.argv[2]
	seqfile = sys.argv[3]
	geneExpChan(tsvfile, cutoff, seqfile)
main()