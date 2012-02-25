pdf("hist.pdf")
polarity <- read.table("~/weibo/regression/1average_label/1-2y.txt", quote="\"")
hist(polarity$V1, breaks=20, freq=FALSE, col="red", xlab="Polarity", main="Histogram of polarity ([-3, +3]) distribution")
lines(density(polarity$V1), col="blue")
rug(jitter(polarity$V1))
dev.off()

library("gplots")
pdf("heatmap.pdf")
combine_label1 <- read.delim("~/weibo/regression/1average_label/combine_label1.txt", header=F)
combine_label2 <- read.delim("~/weibo/regression/1average_label/combine_label2.txt", header=F)
combine_label <- rbind(combine_label1, combine_label2)
heatmap.2(as.matrix(combine_label))
dev.off()


#http://learnr.wordpress.com.sixxs.org/2009/06/28/ggplot2-version-of-figures-in-lattice-multivariate-data-visualization-with-r-part-1/
library("ggplot2")
n = 2000
v1 = cbind(combine_label$V1, rep(1, n))
v2 = cbind(combine_label$V2, rep(2, n))
v3 = cbind(combine_label$V3, rep(3, n))
v4 = cbind(combine_label$V4, rep(4, n))
v5 = cbind(combine_label$V5, rep(5, n))
annotation = data.frame(rbind(v1, v2, v3, v4, v5))
colnames(annotation) = c("polarity", "annotator")
pg <- ggplot(annotation, aes(polarity)) + geom_histogram() + facet_wrap(~annotator)
ggsave(file="hist_diff.pdf")
