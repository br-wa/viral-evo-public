#!/usr/bin/env Rscript

library(ggmuller)
library(ggplot2)

args = commandArgs(trailingOnly=TRUE)
if(length(args)==0){stop("specify name please",call.=FALSE)}

mycols <- c("firebrick1","darkgoldenrod3")
dis_df = read.csv("disFrame.csv")
pop_df = read.csv("popFrame.csv")
mul_df = get_Muller_df(dis_df,pop_df,cutoff=0.001)
Muller_pop_plot(mul_df, add_legend=TRUE, xlab="days", ylab="population", palette=mycols) + ggtitle(paste(args[1]," (population)"))
ggsave("mullerplots/myplot.jpg")
Muller_plot(mul_df, add_legend=TRUE, xlab="days", ylab="frequency", palette=mycols) + ggtitle(paste(args[1]," (frequency)"))
ggsave("mullerplots/myfreqplot.jpg")
