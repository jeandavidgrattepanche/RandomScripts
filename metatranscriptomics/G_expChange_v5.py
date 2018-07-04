import os, sys, math

def geneExpChan(tsvfile, cutoff):
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
			newheader.append(header[allna[j]].replace('\n',''))
		allmi = [i for i,x in enumerate(header) if x[0:2] == "Mm" and x.split('_')[1] == "mi" and x[6] == "p" and x[6:10] != "p0z0"]
		print allmi
		for j in  range(0,len(allmi)):
			print allmi[j], header[allmi[j]]
			newheader.append(header[allmi[j]])
		print newheader
	dict = {} ; dict2 = {}; trans = []; z = 0
	out1 = open(tsvfile.split('.')[0]+'_Gexp.tsv','w+')
	out1.write('\t'+ ('\t').join(newheader) +'\n')	
	out2 = open(tsvfile.split('.')[0]+'.tsv','w+')
	out2.write('\t'+ ('\t').join(newheader) +'\n')	
	for row in open(tsvfile,'r'):
		list= []; list2 = []; z += 1
		if row[0] != "\t":
			trans.append(row.split('\t')[0])
			for j in  range(0,len(allna)):
				if float(row.split('\t')[contna[0]]) > int(cutoff) and float(row.split('\t')[allna[j]]) > int(cutoff):
					if float(row.split('\t')[allna[j]]) > 0 and float(row.split('\t')[allna[j]]) <= 10:
						valnax2 =  1
					elif float(row.split('\t')[allna[j]]) > 10 and float(row.split('\t')[allna[j]]) <= 100:
						valnax2 = 2
					elif float(row.split('\t')[allna[j]]) > 100 and float(row.split('\t')[allna[j]]) <= 1000:
						valnax2 = 3
					elif float(row.split('\t')[allna[j]]) > 1000 and float(row.split('\t')[allna[j]]) <= 10000:
						valnax2 = 4
					elif float(row.split('\t')[allna[j]]) > 10000 :
						valnax2 = 5
					else:
						print("BREAK")
				else:
					valnax2= 0
				list2.append(str(valnax2))
			for j in  range(0,len(allna)):
				if float(row.split('\t')[contna[0]]) > int(cutoff) and float(row.split('\t')[allna[j]]) > int(cutoff):
					valnax = round(math.log10(float(row.split('\t')[allna[j]]) / float(row.split('\t')[contna[0]])),1)
					if valnax > 0:
						valnax = 2
					elif valnax < 0:
						valnax = 0
					elif valnax == 0:
						valnax = 1
				else:
					if float(row.split('\t')[contna[0]]) <= int(cutoff):
						valnax = -2
					else:
						valnax = -1
				list.append(str(valnax))
			for j in  range(0,len(allmi)):
				if float(row.split('\t')[contmi[0]]) > int(cutoff) and float(row.split('\t')[allmi[j]]) > int(cutoff):
					if float(row.split('\t')[allmi[j]]) > 0 and float(row.split('\t')[allmi[j]]) <= 10:
						valmix2 =  1
					elif float(row.split('\t')[allmi[j]]) > 10 and float(row.split('\t')[allmi[j]]) <= 100:
						valmix2 = 2
					elif float(row.split('\t')[allmi[j]]) > 100 and float(row.split('\t')[allmi[j]]) <= 1000:
						valmix2 = 3
					elif float(row.split('\t')[allmi[j]]) > 1000 and float(row.split('\t')[allmi[j]]) <= 10000:
						valmix2 = 4
					elif float(row.split('\t')[allmi[j]]) > 10000 :
						valmix2 = 5
					else:
						print("BREAK")
				else:
					valmix2 = 0
				list2.append(str(valmix2))
			for j in  range(0,len(allmi)):
				if float(row.split('\t')[contmi[0]]) > int(cutoff) and float(row.split('\t')[allmi[j]]) > int(cutoff):
					valmix = round(math.log10(float(row.split('\t')[allmi[j]]) / float(row.split('\t')[contmi[0]])),1)
					if valmix > 0:
						valmix = 2
					elif valmix < 0:
						valmix = 0
					elif valmix == 0:
						valmix = 1
				else:
					if float(row.split('\t')[contmi[0]]) <= int(cutoff):
						valmix = -2
					else:
						valmix = -1
				list.append(str(valmix))
			print row.split('\t')[0]
			dict2[row.split('\t')[0]] = list2
			dict[row.split('\t')[0]] = list
	print z, " transcripts"
	list3 = []
	for transcript in trans:
		sum=0
		for element in dict[transcript]:
			if element != -1:
				sum+= float(element)
			else:
				sum+= -1
		if sum != -44: # and sum != 22 : 
			out1.write(transcript + '\t' + ('\t').join(dict[transcript]) + '\n')
			out2.write(transcript + '\t' + ('\t').join(dict2[transcript]) + '\n')
			list3.append(transcript)
	print len(list3), "transcript > ", cutoff
def main():
	tsvfile = sys.argv[1]
	cutoff = sys.argv[2]
	geneExpChan(tsvfile, cutoff)
main()
