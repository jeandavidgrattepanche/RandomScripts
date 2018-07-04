import os,sys


if len(sys.argv) != 4:
	print('\n\nDouble check that you have added all the necessary command-line inputs! (see usage below for an example)\n\n')
	print ('Example Usage:\n\n\t $ python Librpkm_merging.py ref  Mm directory\n\n')	
	sys.exit()
else:
	ref = sys.argv[1]
	code = sys.argv[2]
	directory = sys.argv[3]

def loop_rpkm():
	seqlist = []; contdict = {}; namelist = []; dictsample = {}
	for seq in open(ref):
		if seq[0] == '>':
			seqlist.append(seq.replace('>','').replace('\n',''))
	for filename in os.listdir(directory):
		if filename.startswith(code) and filename.endswith('rpkm.txt'):
			name = ('_').join(filename.split('_')[0:3])
			namelist.append(name)
			for row in open(directory+'/'+filename):
				if row.split('\t')[0].split('_')[0] == 'Contig':
					rpkm = row.split('\t')[5]
					contigname= row.split('\t')[0]
#					dictsample[name] = rpkm
					if contigname not in contdict:
						contdict[contigname] = {}
						contdict[contigname][name]= rpkm
					else:	
						contdict[contigname][name]= rpkm
	out = open(directory.split('/')[0]+'_merge.txt','w+')
	out.write('\t'+('\t').join(namelist) + '\n')
	for seqref in seqlist:
		towrite = []
		for name in namelist:
			try:
				towrite.append(contdict[seqref][name])
			except:
				towrite.append('0')
		out.write(seqref+'\t'+('\t').join(towrite) +'\n')
	
def main():

	loop_rpkm()

main()
