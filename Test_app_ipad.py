# script derived from TrophicModePredictionTool from J Burns et al 2018 NEE

import re; sys; os

for file in oslistdir(‘DataFolder/’):
	species=file.split(‘_’)[0]+’_’+file.split(‘_’)[1]
	os.command(‘species=‘+species)
	filename=file
	os.command(‘filename=‘+filename)
	HMMs=HMMs/phag_nonphag-allVall-any3diverse.hmmCAT.hmm
	os.command(‘HMMs= /phag_nonphag-allVall-any3diverse.hmmCAT.hmm’)	

# run hmmsearch
	os.command(‘hmmsearch --tblout $species.x.phag_nonphag-allVall-any3diverse.hmmsearchOUT-tbl.txt --cpu 2 $HMMs $filename’)

#then pick the most significant
	os.command(‘sigfile=${species}_sigHits.txt \
	sigModel=${sigfile//_sigHits.txt/_sigModels.txt} \
	echo $sigfile \
	echo $sigModel \
	grep -v “^#” $species.x.phag_nonphag-allVall-any3diverse.hmmsearchOUT-tbl.txt | awk ‘$5<=1e-5 && $8<=1e-4 > $sigfile \
	awk ‘{print $3}’ $sigfile | sort -u > $sigModel )
	os.command(‘cp $sigModel TestGenomes/$sigModel)
