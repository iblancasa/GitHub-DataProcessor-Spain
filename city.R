#!/usr/bin/Rscript
install.packages("jsonlite", repos="http://cran.r-project.org")
install.packages("httr", repos="http://cran.r-project.org")

library(jsonlite)
library(httr)


City<-setClass(
  "City",
  
  slots=c(
    name="character",
    id="character",
    secret="character",
    data="data.frame"
  ),
  

  validity=function(object)
  {
    if(is.na(object@name)) {
      return("No city defined")
    }
    return(TRUE)
  },
  

)

setGeneric(name="getData",
           def=function(theObject)
           {
             standardGeneric("getData")
           }
)

setMethod(f="getData",
          signature="City",
          definition=function(theObject)
          {
            file<-paste("https://raw.githubusercontent.com/JJ/top-github-users-data/master/data/user-data-",
                        theObject@name,
                        ".json", 
                        sep="")
            data<-fromJSON(URLencode(file))
            newCity<-City(name=theObject@name, id=theObject@id,secret=theObject@secret)
            newCity@data<-data
            eval.parent(substitute(theObject<-newCity))
            }
)

city<-City(name="Ávila", id=Sys.getenv("GH_ID"),secret=Sys.getenv("GH_SECRET"))
city<-getData(city)

city@data
