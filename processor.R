#!/usr/bin/env Rscript

#install.packages("jsonlite", repos="http://cran.r-project.org")
#install.packages("httr", repos="http://cran.r-project.org")

library(jsonlite)
library(httr)


##GitHub API keys
id<-Sys.getenv("GH_ID")
secret<-Sys.getenv("GH_SECRET")
setwd("/home/iblancasa/Escritorio/Proyectos/GitHub-DataProcessor-Spain")


############################################################################################
print("-------------SPAIN-----------------------")
print("Reading data from Spain")

#Reading JSON
spanish_data <- fromJSON("https://raw.githubusercontent.com/JJ/top-github-users-data/master/data/user-data-Espa%C3%B1a.json")


print("Getting data about languages...")
language_data<-table(spanish_data$language) #Getting languages frequency
language_data<-as.data.frame(language_data) #To data frame
language_data<-language_data[ order(language_data$Freq,decreasing=TRUE), ] #Sorting by frequency
colnames(language_data) <- c("language", "developers")


exportJson <- toJSON(language_data)#To JSON
print("Writing data about languages in JSON file")
write(exportJson, "./ProcessedData/spanishLanguages.json")#Writing
print("JSON file wrote")





############################################################################################
############################################################################################
############################################################################################
############################################################################################



print("-------------PROVINCES-----------------------")

provinces <- fromJSON("cities.json")

cities<-provinces$city
utf<-provinces$utf
population<-as.numeric(provinces$population)


url<-"https://raw.githubusercontent.com/JJ/top-github-users-data/master/data/user-data-"


languages_result<-list()




calcule <- function (name_city){
    print(paste("Getting data from ",name_city, sep=""))
    
    file<-paste(url, name_city,".json", sep="")
    file<-URLencode(file)
    print(file)
    province_data <- fromJSON(file)
    
    
    ##Getting languages in each province
    print("   Getting languages in province")
    language_data<-table(province_data$language) #Getting languages frequency
    language_data<-as.data.frame(language_data) #To data frame
    language_data<-language_data[ order(language_data$Freq,decreasing=TRUE), ] #Sorting by frequency
    colnames(language_data) <- c("language", "developers")
    new_province<-list(name_city,language_data)
    languages_result<<-list(languages_result,new_province)
    ##End getting languages in each province
}


sapply(cities,calcule)


print("Data from provinces calculated!")



##########################
#Languages in province format
##########################
exportJson <- toJSON(languages_result)#To JSON
print("Writing data about languages in JSON file")
write(exportJson, "./ProcessedData/languagesProvince.json")#Writing


print("JSON file wrote")

rm(list=ls())



