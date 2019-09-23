# script derived from TrophicModePredictionTool from J Burns et al 2018 NEE

import re, sys, os

for file in oslistdir('DataFolder/'):
	species=file.split('_')[0]+'_'+file.split('_')[1]
	filename=file
	HMMs='HMMs/phag_nonphag-allVall-any3diverse.hmmCAT.hmm'

# run hmmsearch
	os.system('hmmsearch --tblout '+species+'.x.phag_nonphag-allVall-any3diverse.hmmsearchOUT-tbl.txt --cpu 2 '+HMMs+' DataFolder/'+ filename)

#then pick the most significant
	os.system('grep -v "^#" '+species+".x.phag_nonphag-allVall-any3diverse.hmmsearchOUT-tbl.txt | awk '$5<=1e-5 && $8<=1e-4' > "+species+'_sigHits.txt')
	os.system("awk '{print $3}' "+species+'_sigHits | sort -u > '+species+'_sigModels.txt')
	os.system('cp '+species+'_sigModels.txt TestGenomes/'+species+'_sigModels.txt')
