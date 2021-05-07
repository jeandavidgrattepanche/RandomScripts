setwd('/home/tuk61790/HPCr/')
library('ape')
library('phytools')
library('phyloseqCompanion')
library("ggplot2")
library("plyr")
library(factoextra)
source('/home/tuk61790/HPCr/multiplot.R', chdir = TRUE)

data.all <- read.table('OTUtable_ingroup_noTtree_part1.txt')
mytable = otu_table(cbind(data.all[c(0)],data.all[c(16:111)]), taxa_are_rows=TRUE,errorIfNULL=TRUE)
env.all <- read.table('NBP1910_envdataCTD_2021.txt')
envdata = sample_data(env.all)
testb <- as.matrix(data.all[c(0:15)])
TAX <- tax_table(testb)
physeq <- phyloseq(mytable, envdata, TAX)
#pico <- subset_samples(physeq, size == "pico")
#nano <- subset_samples(physeq, size == "nano")
#micro <- subset_samples(physeq, size == "micro")

#PCoA <- ordinate(physeq, "PCoA", distance = "canberra")
dUNIFRAC = UniFrac(physeq, weighted=TRUE, normalized=FALSE, fast=TRUE)
PCoA <- ordinate(physeq, "PCoA", distance = dUNIFRAC)
ordplotP <- plot_ordination(physeq, PCoA, color="Lat", shape="size",label="sample", title="Allsize")
ordplotPplus <- ordplotP + geom_point(size=3) + stat_ellipse(geom = "polygon", type="norm", alpha=0.4, aes(fill=size))
quartz()
plot(ordplotPplus)

sizes <- c("micro","nano","pico")
indices <- c("bray","jaccard","chao") #"raup","chisq"
list <- list()
i = 0
for(ind in indices){
	for(sizedata in sizes){
		i = i + 1
		named <- paste(ind,sizedata,sep = "-")
		print(named)
		PCoAm <- ordinate(subset_samples(physeq, size == sizedata), "PCoA", distance = ind)
		ordplotPm <- plot_ordination(subset_samples(physeq, size == sizedata), PCoAm, color="Lat", shape="depth",label="sample",title=named)
		ordplotPmplus <- ordplotPm + geom_point(size=3)
		assign(paste("p",i,sep=""), ordplotPmplus)
		list[[length(list)+1]] <- paste("p",i,sep="")
#		plot(get(paste("p",i,sep="")))
	}
}
pdf('PCoAs.pdf')
multiplot(p1,p2,p3,p4,p5,p6,p7,p8,p9,cols=3)
dev.off()

list <- list()
j = 0
for(sizedata in sizes){
	j = j + 1
	print(sizedata)
	ordMDS <- metaMDS(t(otu_table(subset_samples(physeq, size == sizedata))))
	ordMDS.fit <- envfit(ordMDS ~ Lat + Long + bprod + pprod_Sun + pprod_PAR + ice + airT + depth_m + PAR1 + PAR2 + salinity1 + timeJ + latitude + longitude + oxygen1 + oxygenSaturation + fluorescence + beamTrans + waterT1 + conductivity1 + depSM + size_num, data=sample.data.table(sizedata), perm=999, na.rm = TRUE)
	part123 <- c(plot(ordMDS, dis="site") , plot(ordMDS.fit) , text(ordMDS, display="sites"))
	assign(paste("q",j,sep=""), part123)
}
pdf('NMDS.pdf')
multiplot(q1,q2,q3,q4,q5,q6,q7,q8,q9,cols=3)
dev.off()