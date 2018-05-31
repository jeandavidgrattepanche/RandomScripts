import os,sys


if len(sys.argv) != 3:
	print ('\n\nDouble check that you have added all the necessary command-line inputs! (see usage below for an example)\n\n')
	print ('Usage:\n\n\t $ python3 extract_mapped_rpkm.txt Mm directory\n\n')
	sys.exit()
else:
	code = sys.argv[1]
	directory = sys.argv[2]

def loop_rpkm():
	out = open(directory.split('/')[0]+'_mapped.txt','w+')
	for filename in os.listdir(directory):
		if filename.startswith(code) and filename.endswith('_rpkm.txt'):
			name = ('_').join(filename.split('_')[0:3])
			rpkmfile=open(directory+'/'+filename,'r')
			for line in rpkmfile:
				if line.startswith('#Reads'):
					reads = line.split('\t')[1].split('\n')[0]
				if line.startswith('#Mapped'):
					mapped = line.split('\t')[1].split('\n')[0]
			perc=(int(mapped)/int(reads)) * 100
			out.write(filename.split('_')[2] + '\t' + filename.split('_')[1] + '\t'+ str(reads) + '\t' + str(mapped) + '\t' + str(perc) +'\n')
def main():

	loop_rpkm()

main()
