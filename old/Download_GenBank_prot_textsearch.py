from Bio import Entrez
from Bio import SeqIO
Entrez.email = "jgrattepanche@smith.edu"

list2 = [] ; list3= []
for row in open('list_prot_GB.fasta','r'):
	for element in row.split(','):
#		print(element.replace("'",'').replace('[','').replace(']','').replace(" ",''))
		if element.replace("'",'').replace('[','').replace(']','') not in list2:
			list2.append(element.replace("'",'').replace('[','').replace(']','').replace(" ",''))
print(len(list2), 'already retrieved')
print("Asking GenBank")		
answer = Entrez.esearch(db='protein', term='eukaryota NOT metazoa NOT fungi NOT viridiplantae', retmax='50000000')
records = Entrez.read(answer)
answer.close()
print("Parsing results and Retrieving sequences")
out = open('seq_prot_GB.fasta','a')
outlog = open('list_prot_GB.fasta','a')
for ID in records['IdList']:
	if ID not in list2:
		list3.append(ID)
for i in range(0, len(list3) , 200):
	list = list3[i:i+200]
	result = Entrez.efetch(db='protein',id=list,rettype='gb',retmode='text')
	out = open('seq_prot_GB.fasta','a')
	for seq in SeqIO.parse(result,'gb'):
		out.write('>'+seq.id + '_' + seq.annotations['source']+'\n'+ str(seq.seq)+'\n')
	out.close()
	outlog = open('list_prot_GB.fasta','a')
	outlog.write(str(list) + '\n')
	outlog.close()
	print( int(int(i)+int(len(list2))), ' data have been retrieved on ', len(records['IdList']), "i.e. ", float((int(int(i)+int(len(list2)))/int(len(records['IdList'])))*100))
