mydata <- read.csv("https://stepik.org/media/attachments/lesson/11481/evals.csv", stringsAsFactors = T)
mydata$quality <- rep(NA, nrow(mydata))
for (i in 1:nrow(mydata)){
  if (mydata$score[i] > 4){
    mydata$quality[i] <- 'good'
  }else mydata$quality[i] <- 'bad'
}
mydata$quality2 <- ifelse(mydata$score > 4, 'good', 'bad')
ifelse(mydata$quality == mydata$quality2, 'equals', 'not equals')
