mydata <- read.csv("shops.csv")
boxplot(price~origin, data = mydata)
ggplot(mydata, aes(x = origin, y = price))+
  geom_boxplot()
fit <- aov(price ~ origin, data = mydata)
summary(fit)
fit2 <- aov(price~origin+store, data = mydata)
summary(fit2)
model.tables(fit2, "mean")
fit <- aov(price~origin+store+origin:store, data = mydata)
summary(fit)
df <- npk
fit <- aov(yield ~ N + P + K, data = df)
summary(fit)
ggplot(mydata, aes(x = food, y = price, fill = origin))+
  scale_fill_manual(values =c("red", "blue"))+ xlab('Еда') + ylab('Цена')+
  geom_boxplot()
fit5 <- aov(price ~ food, data = mydata)
summary(fit5)
fit5
TukeyHSD(fit5)
df <- iris
fit <- aov(Sepal.Width ~ Species, data = df)
summary(fit)
TukeyHSD(fit)
ggplot(df, aes(x = Sepal.Width, y = Species))+
  geom_boxplot()
df2 <- read.csv("therapy_data.csv", stringsAsFactors = T)
df2$subject <- as.factor(df2$subject)
str(df2)
fit1 <- aov(well_being ~ therapy, data = df2)
summary(fit1)
fit1b <- aov(well_being ~ therapy + Error(subject/therapy), data = df2)
summary(fit1b)
fit2 <- aov(well_being ~ therapy*price, data = df2)
summary(fit2)

ggplot(df2, aes(x = price, y = well_being))+
  geom_boxplot()
fit2b <- aov(well_being ~ therapy*price + Error(subject/(therapy*price)), data = df2)
summary(fit2b)
ggplot(df2, aes(x = price, y = well_being))+
  geom_boxplot()+
  facet_grid(~subject)
fit3 <- aov(well_being ~ therapy*price*sex, data = df2)
summary(fit3)
fit3b <- aov(well_being ~ therapy*price*sex + Error(subject/(therapy*price)), data = df2)
summary(fit3b)
data3 <- read.csv("Pillulkin.csv", stringsAsFactors = T)
str(data3)
data3$patient <- as.factor(data3$patient)
fit7 <- aov(temperature~ pill + Error(patient/pill), data = data3)
summary(fit7)
fit8 <- aov(temperature~ pill*doctor + Error(patient/(pill*doctor)), data = data3)
summary(fit8)
ggplot(ToothGrowth, aes(x = as.factor(dose), y = len, col = supp, group = supp))+
  stat_summary(fun.data = mean_cl_boot, geom = 'errorbar', width = 0.1, position = position_dodge(0.2))+
  stat_summary(fun.data = mean_cl_boot, geom = 'point', size = 3, position = position_dodge(0.2))+
  stat_summary(fun.data = mean_cl_boot, geom = 'line', position = position_dodge(0.2))