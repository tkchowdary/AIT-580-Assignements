######################################################################################################################
#Tukey’s five number summary

library(readr)
Atlantic <- read_csv("Desktop/Atlantic.csv")
summary(Atlantic) # summary of Tukey's five number summary

######################################################################################################################
#Construct a pairwise correlation matrix for each pair of columns.

library(readr)
data_set <- read_csv("Desktop/Atlantic.csv")
data_set <- na.omit(data_set)
a<-data_set[,c(3,4,5,6,10,11)] #Subset is created
b<-as.matrix(a) #data frame is converted to matrix
d<-cor(b) #correlation matrix is created to b
e<-as.matrix(d) #d is converted to matrix and stored in e
class(e)
corrplot::corrplot(e,method = "circle") # correlation is plotted to e

######################################################################################################################
#Construct a pairwise distribution plot for each interesting pair of columns.

library(readr)
data_set <- read_csv("Desktop/Atlantic.csv")
install.packages("tidyverse")
library(lattice)
pairs(data_set[,c(3, 4, 5, 6, 10, 11)])

######################################################################################################################
#Line plot

library(ggplot2)
library(readr)
data_set <- read_csv("Desktop/Atlantic.csv")
sub_set<-data_set[,3:4]
sub_set<-unique(sub_set)
ggplot(sub_set,aes(x=sub_set$year ,y=sub_set$cyclone_of_the_year ))+
	geom_line()+
	stat_smooth(method='gam')+
	labs(x="Year", y="Cycle of the year", title="Year vs Cyclone of the Year")


######################################################################################################################
#A scatter plot.

library(ggplot2)
library(readr)
data_set <- read_csv("Desktop/Atlantic.csv")
ggplot(data_set,aes(x=data_set$year ,y=data_set$cyclone_of_the_year ))+
	geom_point()+
	stat_smooth(method = "lm")+
	labs(x="Year", y="Cycle of the year", title="Year vs Cyclone of the year")

######################################################################################################################
#A heatmap.

library(readr)
library(dplyr)
library(ggplot2)
data_set <- read_csv("Desktop/Atlantic.csv")
sub_set<-data_set[,c(3, 4, 6, 10)]
sub_set<-distinct(sub_set)
sub_set <- as.matrix(sub_set)
heatmap(sub_set)

######################################################################################################################
#A bar plot or pie chart.

library(ggplot2)
library(readr)
library(dplyr)
data_set <- read_csv("Desktop/Atlantic.csv")
sub_set<-data_set[,c(3,4)]
sub_set<-distinct(sub_set)
ggplot(sub_set,aes(sub_set$year ,sub_set$cyclone_of_the_year ))+
	geom_bar(stat="identity")+
	labs(x="Year", y="Cyclone of the year", title="Year vs Cyclone of the year")


######################################################################################################################
#A histogram.

library(readr)
library(dplyr)
library(ggplot2)
data_set <- read_csv("Desktop/Atlantic.csv")
sub_set<-data_set[,c(3,4)]
sub_set<-distinct(sub_set)
ggplot(sub_set,aes(sub_set$year ))+
	geom_histogram(color="blue",bins = 20)+
	labs(x="Year", y="Frequency", title="Year vs Frequency ")