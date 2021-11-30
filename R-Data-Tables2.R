library(data.table)
data(Loblolly)
pine <- as.data.table(Loblolly)
pine[, mean(height), by=age]
pine[, mean(height), by=Seed]
pine[,.(height_med=median(height)),by=Seed][order(Seed)]
pine[,.(height=mean(height)), by=age][order(age)]
pine2=as.data.table(pine)
pine1 <-pine2[age=="15"]
setnames(pine1, "height", "Height in cm")
setnames(pine1, "age", "Age")
setnames(pine1, "Seed", "Seed No.")
setnames(pine, "Seed", "Seed No.")
setnames(pine, "age", "Age")
setnames(pine, "height", "Height in cm")
pine['Height in cm'>44.0]
forty4 <- pine['Height in cm'>44.0]
forty4[, mean(`Height in cm`), by=Age]