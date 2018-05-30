import os,sys

#----------------------------- Colors For Print Statements ------------------------------#
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   ORANGE = '\033[38;5;214m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#------------------------------ Checks the Input Arguments ------------------------------#


if len(sys.argv) != 4:
	print color.BOLD + '\n\nDouble check that you have added all the necessary command-line inputs! (see usage below for an example)\n\n'
	print color.BOLD + '\n\nDouble check that this script is in the bbmap folder!\n\n'
	print  color.RED + 'Example Usage:\n\n\t' + color.CYAN + 'katzlab$ python Autorpkm.py ref Mm directory\n\n' + color.END	
	print color.BOLD + 'The current script controls for names, for example, Mm is the shared starting of each file/folder, and ref is the reference you want to map your reads against\n\n'
	sys.exit()
else:
	ref =  sys.argv[1]
	code = sys.argv[2]
	directory = sys.argv[3]

def loop_rpkm():
	for filename in os.listdir(directory):
		if filename.startswith(code) and filename.endswith('.fastq.gz') and 'FWD' in filename:
			name = ('_').join(filename.split('_')[0:3])
			print('./seal.sh in='+directory+filename+' in2='+directory+ filename.replace('FWD','REV')+' ref='+ref+' rpkm=../'+name+'_rpkm.txt Xmx30g')
			os.system('./seal.sh in='+directory+filename+' in2='+directory+filename.replace('FWD','REV')+' ref='+ref+' rpkm=../'+name+'_rpkm.txt Xmx30g')	
# 			os.system('mv ../'+filename+' ../done/')
# 			os.system('mv ../'+filename.replace('FWD','REV')+' ../done/')
#			os.system('scp ../'+newname+'_WTA_rnaspades_'+date+'/transcripts.fasta katzlab33@131.229.93.42:/Volumes/katzlab/Alistaire_Ruggiero/Reassembled_LKH/'+newname+'_WTA_rnaspades_'+date+'_transcripts.fasta')
def main():

	loop_rpkm()

main()
