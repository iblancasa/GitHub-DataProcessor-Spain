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
colnames(language_data) <- c("language", "developers")


exportJson <- toJSON(language_data)#To JSON
print("Writing data about languages in JSON file")
write(exportJson, "./ProcessedData/spanishLanguages.json")#Writing
print("JSON file wrote")
rm(list=ls())



############################################################################################
############################################################################################
############################################################################################
############################################################################################



print("-------------PROVINCES-----------------------")

provinces <- fromJSON("./Proyectos/GitHub-DataProcessor-Spain/cities.json")

cities<-provinces$city
utf<-provinces$utf
population<-as.numeric(provinces$population)


url<-"https://raw.githubusercontent.com/JJ/top-github-users-data/master/data/user-data-"


languages_result<-list()
totalContributions_result<-c()
totalContributionsPopulation_result<-c()

for (i in 1:length(cities)) {
  print(sprintf("Getting data about languages in %s",cities[i]))
  file<-paste(url, utf[i],".json", sep="")
  print(cities[i])
  print(file)
  province_data <- fromJSON(file)

  language_data<-table(province_data$language) #Getting languages frequency
  language_data<-as.data.frame(language_data) #To data frame
  language_data<-language_data[ order(language_data$Freq,decreasing=TRUE), ] #Sorting by frequency
  
  
  ##Language
  new_province<-list(cities[i],language_data)
  languages_result[[i]]<-new_province
  
  
  ##Total contributions
  totalcontributions<-sum(as.numeric(province_data$contributions))  
  totalContributions_result<-append(totalContributions_result,totalcontributions)
  
  
  ##Total contributions population
  totalcontributionsPopulation<-totalcontributions/population[i]
  print(totalcontributionsPopulation)
  totalContributionsPopulation_result<-append(totalContributionsPopulation_result,totalcontributionsPopulation)
}





#####Languages in province
exportJson <- toJSON(languages_result)#To JSON
print("Writing data about languages in JSON file")
write(exportJson, "./Proyectos/GitHub-DataProcessor-Spain/ProcessedData/languagesProvince.json")#Writing



#####Total contributions
contributions_total <- data.frame(cities,totalContributions_result)
contributions_total<-contributions_total[ order(contributions_total$totalContributions_result,decreasing=TRUE), ]
colnames(contributions_total) <- c("language", "developers")

exportJson <- toJSON(contributions_total)#To JSON
print("Writing data total contributions JSON file")
write(exportJson, "./Proyectos/GitHub-DataProcessor-Spain/ProcessedData/totalContributions.json")#Writing




#####Total contributions population
contributionsPopulation_total <- data.frame(cities,totalContributionsPopulation_result)
contributionsPopulation_total<-contributionsPopulation_total[ order(contributionsPopulation_total$totalContributionsPopulation_result,decreasing=TRUE), ]
colnames(contributionsPopulation_total) <- c("language", "rate")
exportJson <- toJSON(contributionsPopulation_total)#To JSON
print("Writing data total contributions / population JSON file")
write(exportJson, "./Proyectos/GitHub-DataProcessor-Spain/ProcessedData/totalContributionsPopulation.json")#Writing



print("JSON file wrote")

rm(list=ls())



