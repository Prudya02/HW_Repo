df <- iris
str(df)
df1 <- subset(df, Species != "setosa")
str(df1)
df1 <- droplevels(df1)
str(df1)
hist(df1$Sepal.Length)
ggplot(df1,aes(x = Sepal.Length))+
  geom_histogram(fill = "white", col ="black", binwidth = 0.41)+
  facet_grid(Species ~ .)
ggplot(df1, aes(x = Sepal.Length, fill = Species))+
  geom_density(alpha = 0.5)
ggplot(df1, aes(y = Sepal.Length, x = Species ))+
  geom_boxplot()
shapiro.test(df1$Sepal.Length)
shapiro.test(df1$Sepal.Length[df1$Species== "versicolor"])
shapiro.test(df1$Sepal.Length[df1$Species== "virginica"])
bartlett.test(Sepal.Length ~ Species, df1)
t.test(Sepal.Length ~ Species, df1)
test1 <- t.test(Sepal.Length ~ Species, df1)
str(test1)
t.test(Sepal.Length ~ Species, df1, var.equal = T)
t.test(df1$Sepal.Length, mu = 6.262)
t.test(df1$Sepal.Length, df1$Sepal.Width, paired = T)
df2 <- ToothGrowth
t_stat <- t.test(df2$len[df2$supp == "OJ" & df2$dose == 0.5],
       df2$len[df2$supp == "VC" & df2$dose == 2])[1]
df <- read.csv(url('https://stepic.org/media/attachments/lesson/11504/lekarstva.csv'))
str(df)
df$Group <-  as.factor(df$Group)
ggplot(df, aes(Pressure_before))+
  geom_boxplot()

ggplot(df, aes(Pressure_after))+
  geom_boxplot()
t.test(df$Pressure_before,df$Pressure_after, paired = T)

ggplot(df1, aes(Species, Sepal.Length))+
  stat_summary(fun.data = mean_cl_normal,geom = "errorbar", width = 0.1)+
  stat_summary(fun.y = mean, geom = "point", size = 4)
ggplot(df1, aes(Species, Sepal.Length))+
  stat_summary(fun.data = mean_cl_normal,geom = "pointrange", size = 1)
wilcox.test(Petal.Length ~ Species, df1)
ggplot(df1, aes(Species,Petal.Length))+
  geom_boxplot()
test2 <- wilcox.test(Petal.Length ~ Species, df1)
wilcox.test(df1$Petal.Length, df1$Petal.Width, paired = T)
ggplot(df1, aes(Species,Petal.Length))+
  geom_boxplot()
t1 <- read.table("dataset_11504_15.txt")
t1
bartlett.test(V1 ~ V2, t1)
wilcox.test(V1~V2, t1)
t1 <- read.table("dataset_11504_16.txt")
t1
t.test(t1$V1, t1$V2)
