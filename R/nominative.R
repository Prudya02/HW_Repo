df <- read.csv("https://stepik.org/media/attachments/lesson/11502/grants.csv")
df
str(df)
df$status <- as.factor(df$status)
levels(df$status) <- c("Not funded", "Funded")
t1 <- table(df$status)
t2 <- table(status = df$status,field = df$field)
t2 <- table(years = df$years_in_uni, field = df$field, status = df$status)
prop.table(t2)
prop.table(t2, 1)
prop.table(t2, 2)
t1 <- HairEyeColor
t2 <- prop.table(t1,1)
dimnames(t2)
red_men <- t2['Red', 'Blue','Male']
red_men  
red_men <- prop.table(HairEyeColor['Red', 'Blue','Male'], 1)
red_men <- prop.table(HairEyeColor[,,'Male'], 2)['Red', 'Blue']
t1 <-  HairEyeColor
sum <- sum(t1[,'Green','Female'])
df
t2 <- table(Years = df$years_in_uni,Field = df$field, Status = df$status)
barplot(t1,legend.text = T,args.legend = list(x = "topright"))
barplot(t2,legend.text = T,args.legend = list(x = "topright"),beside = T)
mosaicplot(t2)
barplot(t1[])
library("ggplot2")
mydata <- as.data.frame(HairEyeColor)
mydata <- subset(mydata, Sex == "Female")
obj <- ggplot(data = mydata, aes(x = Hair, y = Freq, fill = Eye)) + 
  geom_bar(stat="identity", position = "dodge") + 
  scale_fill_manual(values=c("Brown", "Blue", "Darkgrey", "Darkgreen"))
binom.test(x = 5, n = 20, p = 0.5)
binom.test(t1)
t1 <-  HairEyeColor
t2 <- t1['Brown',,'Female']
chisq.test(t2)
t2
t1 <- diamonds
t2 <- t1[, c(2,3)]
chisq.test(t2)
test <- chisq.test(t1$cut,t1$color)[1]
t1$factor_price <- ifelse(t1$price >= mean(t1$price),1,0)
t1$factor_carat <- ifelse(t1$carat >= mean(t1$carat),1,0)
tail(t1)
barplot(c(t1$carat, t1$price))
main_stat <- chisq.test(t1$factor_price,t1$factor_carat)[1]
tc <- mtcars
fisher_test <- fisher.test(tc$vs,tc$am)$p.value

