#!/usr/bin/env Rscript

library(jsonlite)
library(httr)


##GitHub API keys
id<-Sys.getenv("GH_ID")
secret<-Sys.getenv("GH_SECRET")



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
history<-5
      
provinces <- fromJSON("./Proyectos/GitHub-DataProcessor-Spain/cities.json")

cities<-provinces$city
utf<-provinces$utf
#population<-as.numeric(provinces$population)


url<-"https://raw.githubusercontent.com/JJ/top-github-users-data/master/data/user-data-"
url_commits<-"https://api.github.com/repos/JJ/top-github-users-data/commits?path=data/user-data-"
url_old<-"https://raw.githubusercontent.com/JJ/top-github-users-data/"  


#languages_result<-list()
totalContributions_result<-list()
totalContributionsCities<-data.frame()
#totalContributionsPopulation_result<-c()
#totalContributionsCities<-data.frame()

for (i in 1:length(cities)) {
  #print(sprintf("Getting data about languages in %s",cities[i]))
  #file<-paste(url, utf[i],".json", sep="")
  print(cities[i])
  #province_data <- fromJSON(file)

  ##Getting old files
        print("Getting data from old files....····")
        file_commits<-paste(url_commits, utf[i],".json&client_id=",id,"&client_secret=",secret, sep="")
        
        print(file_commits)
        
        commitsJSON <- fromJSON(file_commits)
        
        commits<-as.data.frame(commitsJSON)#To data frame
        dates<-commits$commit$author$date#Getting dates
        new_dates<-substr(dates,1 ,10 )#Removing unused data
        commits$commit$author$date<-new_dates#To commits data frame
        
        commits<-data.frame(commits$commit$author$date,commits$sha)#Getting important data
        
        aux_date <- ""
        f <- function(x, output) {
          if(x['commits.commit.author.date']== aux_date){
            output<-FALSE
          }
          else{
            aux_date <<- x['commits.commit.author.date']
            output<-TRUE
          }
        }
        
        duplicated<-apply(commits,1,f)#Detecting duplicated dates
        
        commits<-commits[duplicated,]#Removing duplicated dates
        
        commits<-commits[1:history,]#Only last 5 files
        commits<-commits$commits.sha#Getting sha
        
        print("----Donwloading old versions of file")
        
        new_cityTotalContributions<-NULL
        totalContributions_result<-NULL
        
        totalContributions_result<-append(totalContributions_result,cities[i])
        for(j in seq(commits)){
          sha<-commits[j]
          file_old<-paste(url_old,sha, "/data/user-data-",utf[i],".json", sep="")
          old_data <- fromJSON(file_old)
          totalcontributions<-sum(as.numeric(old_data$contributions))  
          totalContributions_result<-append(totalContributions_result,totalcontributions)
        }
        
        new_cityTotalContributions<-data.frame()
        new_cityTotalContributions<-rbind(new_cityTotalContributions,totalContributions_result)
        
        colnames<-c("city")
        colnames<-append(colnames,seq(1,history,1))
        colnames(new_cityTotalContributions)<-colnames
        
        totalContributionsCities<- rbind( totalContributionsCities, new_cityTotalContributions)
    ##End getting old files
}

##########################
#Total contributions format
##########################
totalContributionsCities$`1`<-as.character(totalContributionsCities$`1`)#Factor to char
totalContributionsCities$`1`<-as.numeric(totalContributionsCities$`1`)#Char to numeric

final<-totalContributionsCities[ order(totalContributionsCities$`1`,decreasing=TRUE), ]#Order 
exportJson <- toJSON(final)#To JSON
print("Writing data total contributions JSON file")
write(exportJson, "./Proyectos/GitHub-DataProcessor-Spain/ProcessedData/totalContributions.json")#Writing
##########################

  
  ##Language
 # language_data<-table(province_data$language) #Getting languages frequency
#  language_data<-as.data.frame(language_data) #To data frame
#  language_data<-language_data[ order(language_data$Freq,decreasing=TRUE), ] #Sorting by frequency
#  colnames(language_data) <- c("language", "developers")
#  new_province<-list(cities[i],language_data)
#  languages_result[[i]]<-new_province
  
  
  
  ##Total contributions population
 # totalcontributionsPopulation<-totalcontributions/population[i]
#  print(totalcontributionsPopulation)
#  totalContributionsPopulation_result<-append(totalContributionsPopulation_result,totalcontributionsPopulation)
#en bucle iba}



colnames<-c("city")
colnames<-append(colnames,seq(1,history,1))

colnames(totalContributionsCities)<-colnames



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



