
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
            newCity<-City(name="Ávila", id="4193a11aeba858759f78",secret="dcae8c9a69bf672f854efa5fbf53fa4ec3e2b97c")
            newCity@data<-data
            eval.parent(substitute(theObject<-newCity))
            }
)

city<-City(name="Ávila", id="4193a11aeba858759f78",secret="dcae8c9a69bf672f854efa5fbf53fa4ec3e2b97c")
city<-getData(city)
