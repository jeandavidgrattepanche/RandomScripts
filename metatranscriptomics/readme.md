# Scripts related to metatranscriptomics analyses:

Part of these scripts need the output of phyloTOL.

To refine my reference, I have ran:
$ python3 ParseXml_Memi.py AAseqfile xmlfile 10 1e-50 => reduce reference dataset in AA
$ python3 AA_Nucl_R2G.py AAseqfile NTDseqfile => create the NTD file for the reduce reference (NTD is used for seal in bbmap)

To calculate the gene expression (use seal implemented in bbmap):
$ python Autorpkm.py NTDreference code_libraries directory_libraries => calculate gene expression for transcript in reference for each libraries
$ python3 Librpkm_merging.py NTDreference code_libraries directory_rpkm_for_eachlibrary => merge the result of each library in one unique table
$ python3 extract_mapped_rpkm.py code_libraries directory_rpkm_for_eachlibrary => create a mapped file (statistic of the amount of read mapped to the reference)


