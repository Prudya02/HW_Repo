library(ggplot2)

my_df <- read.csv("train.csv", sep=";")
my_df$hon <- as.factor(my_df$hon)
str(my_df)

ggplot(my_df, aes(read, math, col = gender))+
  geom_point(size = 5)+
  facet_grid(.~hon)+
  theme(axis.text=element_text(size=25),
        axis.title=element_text(size=25,face="bold"))


fit  <- glm(hon ~ read + math + gender, my_df, family = "binomial")
summary(fit)

exp(fit$coefficients)

head(predict(object = fit))

head(predict(object = fit, type = "response"))

my_df$prob  <- predict(object = fit, type = "response")

df <- mtcars
log_coef <- glm(am ~ disp + vs + mpg,df, family = "binomial")$coefficients

library("ggplot2")

obj <- ggplot(data = ToothGrowth, aes(x = supp, y = len, fill = factor(dose)))+
  geom_boxplot()

library(ROCR)

pred_fit <- prediction(my_df$prob, my_df$hon)
perf_fit <- performance(pred_fit,"tpr","fpr")
plot(perf_fit, colorize=T , print.cutoffs.at = seq(0,1,by=0.1))
auc  <- performance(pred_fit, measure = "auc")
str(auc)



perf3  <- performance(pred_fit, x.measure = "cutoff", measure = "spec")
perf4  <- performance(pred_fit, x.measure = "cutoff", measure = "sens")
perf5  <- performance(pred_fit, x.measure = "cutoff", measure = "acc")

plot(perf3, col = "red", lwd =2)
plot(add=T, perf4 , col = "green", lwd =2)
plot(add=T, perf5, lwd =2)

legend(x = 0.6,y = 0.3, c("spec", "sens", "accur"), 
       lty = 1, col =c('red', 'green', 'black'), bty = 'n', cex = 1, lwd = 2)

abline(v= 0.2, lwd = 2)


my_df$pred_resp  <- factor(ifelse(my_df$prob > 0.225, 1, 0), labels = c("N", "Y"))

my_df$correct  <- ifelse(my_df$pred_resp == my_df$hon, 1, 0)


ggplot(my_df, aes(prob, fill = factor(correct)))+
  geom_dotplot()+
  theme(axis.text=element_text(size=25),
        axis.title=element_text(size=25,face="bold"))

mean(my_df$correct)


test_df  <- read.csv("test.csv", sep = ";")
test_df$hon  <- NA

test_df$hon  <- predict(fit, newdata = test_df, type = "response")
View(test_df)


df <- read.csv('data.csv')
fit2 <- glm(admit ~ rank + gpa ,df, family = "binomial", na.action = na.exclude)
fit_pred <- predict(object = fit2, newdata=df[is.na(df$admit),], type = "response")
vec  <- fit_pred
length(vec[vec>=0.8])


install.packages("xtable")
library(xtable)
install.packages("stargazer")
library(stargazer)
fit1 <- lm(mpg ~ cyl + disp, mtcars)
fit2 <- aov(mpg~am*vs,mtcars)
fit_table1 <- xtable(fit1)
fit_table2 <- xtable(fit2) 
print(fit_table1, type = "html", file = "fit_table1.html")
print(fit_table2, type = "html", file = "fit_table2.html")
stargazer(fit1, type = "html", dep.var.labels = "mpg",
          covariate.labels = c("cyl, disp"), out = "models.html") 








