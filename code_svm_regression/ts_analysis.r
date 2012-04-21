library('ggplot2')
library('xts')
library('zoo')
library('TTR')

draw_curve <- function(fin){
    Sys.setlocale("LC_ALL", "C")
    x.df <- read.table(fin, sep='\t')
    x.df$date <- as.POSIXct(strptime(x.df[, 1], format="%a %b %d %H:%M:%S %z %Y"))
    colnames(x.df) <- c("string", "value", "time")
    x.df$date <- as.Date(x.df$time)
    y.df <- aggregate(x.df$value, list(x.df$date), sum)
    colnames(y.df) <- c("date", "value")

    z <- zoo(y.df$value, y.df$date)
    n = 2
    z.smooth = EMA(z, n)
    z.smooth[1:n] <- z[1:n]

    z.df <- data.frame(date = index(z), value = coredata(z))
    z.smooth.df <- data.frame(date = index(z.smooth), value = coredata(z.smooth))

    g <- qplot(date, value, data=z.df) + geom_smooth(span=0.25, degree=2) + opts(title = fin)
    print(g)

    outputdir <- "/Users/mxf/weibo/data_svm_regression/7visualizations/"
    print(fin)
    name <- tail(strsplit(fin, '/')[[1]], 1)
    print(name)
    name <- gsub("all", "pdf", name)
    out_file = paste(outputdir, name, sep="")
    ggsave(file = out_file)

    return(z.df)
}

basedir = "/Users/mxf/weibo/data_svm_regression/6testset_libsvm/"

list.df <- NULL

filelist = list.files(basedir, ".*.all")
i <- 1
for (name in filelist){
    fullname <- paste(basedir, name, sep="")
    z.df <- draw_curve(fullname)
    list.df[[i]] <- z.df 
    i <- i + 1
}
#z.df1 <- draw_curve("1251648860.all")
#z.df2 <- draw_curve("1467948134.all")
#z.df3 <- draw_curve("1723531411.all")
#z.df4 <- draw_curve("1790018523.all")
#z.df5 <- draw_curve("1931783082.all")
#z.df6 <- draw_curve("2075473762.all")
