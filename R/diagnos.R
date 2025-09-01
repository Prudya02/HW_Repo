data(swiss)
str(swiss)
pairs(swiss)
library(ggplot2)
ggplot(swiss, aes(x = Examination, y = Education))+
  geom_point()
ggplot(swiss, aes(x = Examination, y = Education))+
  geom_point() + geom_smooth(method = 'lm')
ggplot(swiss, aes(x = Examination))+
  geom_histogram()
ggplot(swiss, aes(x = log(Education)))+
  geom_histogram()


my_vector <- c(0.027, 0.079, 0.307, 0.098, 0.021, 0.091, 0.322, 0.211, 0.069, 
               0.261, 0.241, 0.166, 0.283, 0.041, 0.369, 0.167, 0.001, 0.053,
               0.262, 0.033, 0.457, 0.166, 0.344, 0.139, 0.162, 0.152, 0.107,
               0.255, 0.037, 0.005, 0.042, 0.220, 0.283, 0.050, 0.194, 0.018,
               0.291, 0.037, 0.085, 0.004, 0.265, 0.218, 0.071, 0.213, 0.232,
               0.024, 0.049, 0.431, 0.061, 0.523)
shapiro.test(sqrt(my_vector))
shapiro.test(log(my_vector))



beta.coef <- function(x){
  return(lm(scale(x[1]) ~ scale(x[2]))$coefficients)
}

fit <- lm(scale(mtcars[,1]) ~ scale(mtcars[,3]))$coefficients

normality.test <- function(x){
  res = vector(length = length(x))
  for(i in 1:length(x)){
    res[i] <- shapiro.test(x[[i]])$p.value
  }
  names(res) <- names(x)
  return(res)
}
normality.test  <- function(x){    
  return(sapply(x, FUN =  shapiro.test)['p.value',])}
normality.test(mtcars[,1:6])

ggplot(swiss, aes(x = Examination, y = Education))+
  geom_point()+geom_smooth()
lm1 <- lm(Education ~ Examination, swiss)
summary(lm1)
swiss$ExaminationSquared <- (swiss$Examination)^2
lm2 <- lm(Education ~ Examination + ExaminationSquared, swiss)
summary(lm2)
anova(lm2, lm1)
swiss$lm1_fitted <- lm1$fitted
swiss$lm2_fitted <- lm2$fitted
swiss$lm1_resid <- lm1$residuals
swiss$lm2_resid <- lm2$residuals
swiss$obs_num <- 1:nrow(swiss)

ggplot(swiss, aes(x = Examination, y = Education))+
  geom_point(size = 3) +
  geom_line(aes(x = Examination, y = lm1_fitted), col = 'red',lwd = 1)+
  geom_line(aes(x = Examination, y = lm2_fitted), col = 'blue',lwd = 1)


ggplot(swiss, aes(x = lm1_fitted, y =lm1_resid))+
  geom_point(size = 3) + geom_hline(yintercept = 0, col = 'red', lwd = 1)
ggplot(swiss, aes(x = lm2_fitted, y =lm2_resid))+
  geom_point(size = 3) + geom_hline(yintercept = 0, col = 'red', lwd = 1)


ggplot(swiss, aes(x = obs_num,y = lm1_resid))+
  geom_point(size = 3)+geom_smooth()
ggplot(swiss, aes(x = obs_num,y = lm2_resid))+
  geom_point(size = 3)+geom_smooth()
df <- read.csv('homosc.csv')
fit <- lm(DV ~ IV,data = df)
install.packages(gvlma)
library(gvlma)
x <- gvlma(fit)
summary(x)

resid.norm  <- function(fit){
  resid1 <- fit$residuals
  if (shapiro.test(resid1)$p.value < 0.05)
    return(ggplot(fit, aes(x = resid1)) + 
             geom_histogram(fill = 'red'))
  else
    return(ggplot(fit, aes(x = resid1)) + 
             geom_histogram(fill = 'green'))
}
fit <- lm(mpg ~ disp, mtcars)
my_plot <- resid.norm(fit)
my_plot
fit <- lm(mpg ~ wt, mtcars)
my_plot <- resid.norm(fit)
my_plot

high.corr <- function(x){
  corel <- cor(x)
  diag(corel) <- 0
  return(c(colnames(corel)[which(abs(corel) == max(abs(corel)), arr.ind = T)[2]],
           (rownames(corel)[which(abs(corel) == max(abs(corel)), arr.ind = T)[1]])))
}
high.corr(test_data)
test_data <- as.data.frame(list(V1 = c(-0.3, 1.2, -0.8, 1.6, -1.5), 
                                V2 = c(0.5, -0.5, 1.7, 1.1, 0.5), 
                                V3 = c(-2.4, 1.8, -1, 0, -0.3), 
                                V4 = c(0.5, 0.5, 0.3, -0.4, 0.9), 
                                V5 = c(-0.2, 2.5, 1.5, -0.7, 0.4), 
                                V6 = c(0.4, 0.3, 0.6, 0, -0.9), 
                                V7 = c(0.6, -0.2, 1.7, 1.3, -1.1), 
                                V8 = c(0.3, -0.7, 0.1, -1, -0.2), 
                                V9 = c(-1.2, 1.3, -0.6, -2.6, -0.4), 
                                V10 = c(0.3, 0.6, -2.2, -0.1, 2.1), 
                                V11 = c(2.4, -1.8, 1, 0, 0.3)))
corel <- cor(test_data)
diag(corel) <- 0
colnames(corel)[which(abs(corel) == max(abs(corel)), arr.ind = T)][2]
