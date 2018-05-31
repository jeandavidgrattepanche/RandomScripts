setwd('/Users/katzlab33/Documents/JD_Grattepanche/metatranscriptomics/RPKM_size_treatment/')
library(vegan)
library(RColorBrewer)
library(gplots)
data.all <- read.table('RPKM_MeMi_ref_5_20_merge_Gexp.tsv')


data.dist.g <- vegdist(t(data.all), method = "euclidean")
col.clus <- hclust(data.dist.g, "ward.D")
data.dist.og <- vegdist((data.all), method = "euclidean")
row.clus <- hclust(data.dist.og, "ward.D")
heatmap.2(as.matrix(data.all), col=c("white","lightblue","blue","mediumslateblue","darkorchid4","red","firebrick","darkred"), Colv=as.dendrogram(col.clus), Rowv= as.dendrogram(row.clus), margins=c(6,6), trace = "none")