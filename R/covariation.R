df <- mtcars

cor.test(x = df$mpg, y = df$hp)
fit <- cor.test(x = df$mpg, y = df$hp)
library(ggplot2)
df$cyl <- as.factor(df$cyl)
fit$p.value
ggplot(df, aes(x = hp, y = mpg, col = cyl))+
  geom_point(size = 5)
cor.test(~ mpg + hp, df)
df_numeric <- df[,c(1,3:7)]
pairs(df_numeric)
cor(df_numeric)
fit3 <- cor(df_numeric)
library(psych)
fit2 <- corr.test(df_numeric)
fit2$r
fit2$p
corr.calc <- function(x){
  return(c(cor.test(x = x[[1]], y = x[[2]])$estimate, cor.test(x[[1]],x[[2]])$p.value))
}
g <- corr.calc( mtcars[, c(1,5)] )

filtered.cor <- function(x){
  fit <-cor(x[,sapply(x, is.numeric)])
  diag(fit) <- 0
  return(ifelse(abs(min(fit)) > max(fit), min(fit), max(fit)))
}
step6 <-  read.table("step6.csv",  header=TRUE, sep=',' )
iris$Petal.Length <- -iris$Petal.Length
ans <- filtered.cor(iris)

smart_cor <- function(x){
  return(ifelse(shapiro.test(x[[1]])$p.value >= 0.05 & shapiro.test(x[[2]])$p.value >= 0.05,
                cor.test(x = x[[1]], y = x[[2]],method = "pearson")$estimate,
                cor.test(x = x[[1]], y = x[[2]],method = "spearman")$estimate))
}

df <- mtcars
df_numeric <- df[,c(1,3:7)]

fit <- lm(mpg ~ hp, df)
summary(fit)

ggplot(df, aes(hp, mpg))+
  geom_smooth(method = lm)+
  facet_grid(.~cyl)
fitted_values_mpg <- data.frame(mpg = df$mpg, fitted = fit$fitted.values) 
new_hp <- data.frame(hp = c(100,150,129,300))
predict(fit, new_hp)