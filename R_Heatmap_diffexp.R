setwd('/Users/katzlab33/Documents/JD_Grattepanche/metatranscriptomics/RPKM_size_treatment/')
library(vegan)
library(RColorBrewer)
library(gplots)
data.all <- read.table('RPKM_MeMi_ref_10_50_mergeb.tsv')
gexp.all <- read.table('RPKM_MeMi_ref_10_50_merge_Gexpb.tsv')

data.dist.g <- vegdist(t(data.all), method = "euclidean")
col.clus <- hclust(data.dist.g, "ward.D")
data.dist.og <- vegdist((data.all), method = "euclidean")
row.clus <- hclust(data.dist.og, "ward.D")

#data.dist.g <- vegdist(t(gexp.all), method = "euclidean")
#col.clus <- hclust(data.dist.g, "ward.D")
#data.dist.og <- vegdist((gexp.all), method = "euclidean")
#row.clus <- hclust(data.dist.og, "ward.D")

heatmap.2(as.matrix(gexp.all), col=c("lightgrey", "white","darkblue","yellow","red"), Colv=as.dendrogram(col.clus), Rowv= as.dendrogram(row.clus), margins=c(6,6), trace = "none")
quartz()

heatmap.2(as.matrix(data.all), col=c("lightgrey", "white","darkblue","yellow","red"), Colv=as.dendrogram(col.clus), Rowv= as.dendrogram(row.clus), margins=c(6,6), trace = "none")
