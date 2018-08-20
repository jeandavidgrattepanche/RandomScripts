#!/usr/bin/python
#renames LAK sequences, removing extension, and will some day local blast, etc.  Part of Laura's dream
import os
import re
import time
import operator
import datetime

PATH = os.getcwd()

# PATH = '/Users/katzlab3003/Documents/seqrenaming/'
macfolder = [".DS","Thumbs.db", ".DS_Store"]
alist={}

now = time.time()
today = datetime.datetime.now().isoformat()

print "start at" , today

directory = '/Volumes/GoogleDrive/My Drive'
os.chdir(directory+'/LAK_sequences/LAK_Sequences')
for file in os.listdir("."):
	if file != 'Transferred' and os.path.isdir(file):
		for fileseq in os.listdir(file):
			if fileseq[0:3] == 'LAK':
				print file, fileseq
				folder = file +'/'+ fileseq
# 				print('cp ' , folder , '/*  ' , PATH)
				os.system('cp ' + folder + ' ' + PATH)
				os.system('mv ' + folder + ' ../Transferred')
			else:
				print "No new sequence"

for seq in os.listdir(PATH):
	if re.search('.ab1',seq):
		newseq = seq.split('_')[0]
		if re.match('LAK',seq):		
			print "NEW"
			os.system('mv ' +  PATH + '/' + seq + ' ' +  PATH + '/' + newseq)
#	else:
#		print "error", seq


newdirectory = PATH + "tomoveinLAKseqs2_AD"
macfolder = ['.DS ','.DS_Store', 'Thumbs.db ', ]
for seq in os.listdir(PATH):
#	print seq[0:3]
	if seq[0:3] == "LAK": # and seq not in macfolder:
		number = seq.split("K")[-1]
		number2 = number[:2]
		print number
	
		if re.match('LAK',seq) and number[0] != '.':
#			print "OK"
#			try:
			folder = 'LAK' + str(int(number2)) + '001-' + str(int(number2) + 1) + '000'
			folderAD = newdirectory + folder
			print folder
			os.system('mkdir ' + '/Volumes/GoogleDrive/My\ Drive/Katzlab\ Shared\ Folder/KatzLab_Seq/' + folder)
			os.system('mv ' + PATH + seq + '   ' + '/Volumes/GoogleDrive/My\ Drive/Katzlab\ Shared\ Folder/KatzLab_Seq/' + folder)
#			os.system('mkdir ' + folderAD)
#			os.system('mv ' + PATH + seq + '   ' + folderAD+'/')
			print "transferring to ", folder
#			except:
#				print number + ' is not a number'
				
print "end at", datetime.datetime.now().isoformat()