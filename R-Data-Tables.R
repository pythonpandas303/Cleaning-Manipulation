data(iris)
str(iris)
summary(iris)
head(iris)
install.packages('data.table')
library(data.table)
dt <- as.data.table(iris)
dt[,mean(Sepal.Length),by=substring(Species,1,1)]
dt[,.N,by=10*round(Sepal.Length*Sepal.Width/10)]
dt[,.(Sepal_length=median(Sepal.Length),
   Sepal_width=median(Sepal.Width),
   Petal_length=median(Petal.Length),
   Petal_width=median(Petal.Width)),
by=Species][order(-Species)]
dt[,.(Sepal.Length=mean(Sepal.Length),
      Sepal.Width=mean(Sepal.Width),
      Petal.Length=mean(Petal.Length),
      Petal.Width=mean(Petal.Width)),
      by=Species][order(Species)]
dt[,lapply(.SD,mean),by=Species]
dt[,lapply(.SD,max),by=Species]
iris=as.data.table(iris)
dt1 <- iris[Species=="virginica"]
head(dt1)
dt2 <- iris[Species %in% c("virginica","versicolor")]
head(dt2)
tail(dt2)
setnames(iris, gsub("^Sepal[.]","",names(iris)))
iris <- iris[,grep("^Petal",names(iris)):=NULL]
head(iris)
iris[Width*Length > 20]