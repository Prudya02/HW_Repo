df <- swiss
str(swiss)
library(ggplot2)
ggplot(df, aes(x = Fertility, y = Examination, size = (Education)))+
  geom_point()
hist(df$Fertility, col = 'red', breaks  = 7)
fit <- lm(Fertility ~ Examination + Catholic, data = df)
summary(fit)
fit2 <- lm(Fertility ~ Examination * Catholic, data = df)
summary(fit2)
confint(fit2)
test_data <- as.data.frame(list(x_1 = c(8, 6, 14, 8, 16, 8, 12, 13, 18, 13),
                                x_2 = c(35, 41, 48, 36, 37, 37, 33, 44, 31, 41),
                                y = c(8, NA, 14, NA, NA, 13, 15, 9, NA, NA)))
fill_na <- function(x){
  fit <- lm(x$y ~ x$x_1 + x$x_2, x)
  for (i in 1:length(x$y)){
    if (is.na(x$y[i]))
      x$y_full[i] <- predict(fit,x)[i]
    else
      x$y_full[i] <- x$y[i]
  }
  return(x)
}
fill_na(test_data)
mtcars
df <- subset(mtcars, select = c(mpg, disp, drat, wt, hp))
fit <- lm(wt ~ mpg + disp+hp, df)
summary(fit)
df <- attitude
fit_3 <- lm(rating ~ complaints * critical, df)
summary(fit_3)
df <- swiss
hist(swiss$Catholic, col = 'red')
df$Religious <- ifelse(df$Catholic > 60, 'Lots', 'Few')
df$Religious <- as.factor(df$Religious)
fit_4 <-lm(Fertility ~ Examination + Religious, df)
summary(fit_4)
fit_5 <-lm(Fertility ~ Examination * Religious, df)
summary(fit_5)
ggplot(df, aes(x = Fertility, y = Examination))+
  geom_point()+facet_grid(df$Religious)+geom_smooth(method = 'lm')
fit_6 <- lm(Fertility ~  Religious * Infant.Mortality *Examination, df)
summary(fit_6)
df2 <- mtcars
df2$am <- factor(df2$am, labels = c('Automatic', 'Manual'))
fit7 <- lm(mpg~wt*am, df2)
summary(fit7)

library(ggplot2)
# сначала переведем переменную am в фактор
mtcars$am <- factor(mtcars$am)

# теперь строим график
my_plot <- ggplot(mtcars, aes(x = wt, y = mpg, col = am))+
  geom_smooth(method = 'lm')
rm(swiss)
swiss <- data.frame(swiss)
fit_full <- lm(Fertility ~., data = swiss)
summary(fit_full)
fit_reduced1 <- lm(Fertility ~ Infant.Mortality + Examination + Catholic + Education, data = swiss)
summary(fit_reduced1)
anova(fit_full, fit_reduced1)
fit_reduced2 <- lm(Fertility ~ Infant.Mortality + Agriculture + Catholic + Education, data = swiss)
summary(fit_reduced2)
anova(fit_full, fit_reduced2)
step(fit_full, direction = 'backward')


model_full <- lm(rating ~ ., data = attitude) 
model_null <- lm(rating ~ 1, data = attitude)
step(model_full,scope = list(lower = model_null, upper = model_full), direction = 'backward')
mod1 <- lm(formula = rating ~ complaints + learning, data = attitude)
anova(model_full, mod1)

model <- lm(sr~.*.,data = LifeCycleSavings)
summary(model)
