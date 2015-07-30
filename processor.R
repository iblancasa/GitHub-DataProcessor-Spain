#!/usr/bin/env Rscript

library(jsonlite)
library(httr)

############################################################################################
print("-------------SPAIN-----------------------")
print("Reading data from Spain")

#Reading JSON
spanish_data <- fromJSON("https://raw.githubusercontent.com/JJ/top-github-users-data/master/data/user-data-Espa%C3%B1a.json")


print("Getting data about languages...")
language_data<-table(spanish_data$language) #Getting languages frequency
language_data<-as.data.frame(language_data) #To data frame
language_data<-language_data[ order(language_data$Freq,decreasing=TRUE), ] #Sorting by frequency

languages<-as.character(language_data[,"Var1"])#Getting language names
frequences<-language_data[,"Freq"]#Getting language frequency

language_data<-mapply( c , languages , frequences , SIMPLIFY = FALSE, USE.NAMES = FALSE  )#Creating list


exportJson <- toJSON(language_data)#To JSON
print("Writing data about languages in JSON file")
write(exportJson, "./ProcessedData/spanishLanguages.json")#Writing
print("JSON file wrote")
############################################################################################