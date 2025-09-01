df <- iris
library(psych)
a <- describeBy(x = df,group = df$Species, mat = T)
b <- subset(a, a$group1 %in% 'virginica')
hist(df$mpg, breaks = 20, xlab = "MPG")
boxplot(mpg ~ am, df)
plot(df$mpg, df$hp)
plot(df$mpg, df$am)
library(ggplot2)
ggplot(df, aes(x = mpg))+
  geom_histogram(fill = "white", col = "black", binwidth = 2)
ggplot(df, aes(x = mpg, fill = am))+
  geom_dotplot()
ggplot(df, aes(x = mpg, fill = am))+
  geom_density(alpha = 0.8)

ggplot(df, aes(x = am, y = hp, fill = vs))+
  geom_boxplot() + scale_fill_manual(values =c("red", "blue"))
my_plot <- ggplot(df, aes(x = mpg, y = hp, col = vs, size = qsec))+
  geom_point()
my_plot2 <- ggplot(df, aes(x = am, y = hp, col = vs))
my_plot2 + geom_boxplot()
df <- airquality

ggplot(df, aes(x = Month, y = Ozone, group = Month))+
  geom_boxplot()
df <- mtcars
ggplot(df, aes(x = mpg, y = disp, col = hp, ))+
  geom_point()
df <- iris
ggplot(df, aes(Sepal.Length, Sepal.Width, col = Species,size = Petal.Length)) +
  geom_point()
getwd()
write.csv(df, "iris4.csv")
t1 <- table(df$Species)
t1
