my_calc <- function(x,y){
  s <- x + y
  
  return(s)
}
result <- my_calc(x = 10, y = 15)
my_calc2 <- function(x,y){
  s <- x + y
  d <- x - y
  return(c(s,d))
}
result <- my_calc2(x = 10, y =15)
my_calc3 <- function(x,y,z = 10){
  s <- x + y + z
  d <- x - y - z
  return(c(s,d))
}
result2 <- my_calc3(1, 4)
distr1 <- rnorm(100)
distr1[1:30] <- NA
distr1[is.na(distr1)] <- mean(distr1, na.rm = T)
source("ma.R")
distr1 <- my_na_rm(x = distr1)
my_na_rm(x = c("q", 2, NA))
distr2 <- rnorm(1000)
distr2[1:30] <- NA
distr2 <- my_na_rm(distr2)
d1 <- rnorm(2000)
d2 <- runif(2000)
d1[1:30] <- NA
d2[1:30] <- NA
d1 <- my_na_rm(d1)
d2 <- my_na_rm(d2)

NA.position <- function(x){
 na_vec <- which(is.na(x) == T)
 return(na_vec)
}
my_vector <- c(1, 2, 3, NA, NA)
NA.position(my_vector)
NA.counter <- function(x){
  num <- length(which(is.na(x) == T))
  return(num)
}
my_vector <- c(1, 2, 3, NA, NA)
NA.counter(my_vector)
NA.counter2 <- function(x){    
  return(sum(is.na(x)))}

dir(pattern =  "*.csv")
grants <- data.frame()
for (i in dir(pattern = "*.csv")){
  temp_df <- read.csv(i)
  grants <- rbind(temp_df, grants)
}
read_data <- function(){
  df <- data.frame()
  number <<-  0
  for (i in dir(pattern = "*.csv")){
    temp_df <- read.csv(i)
    df <- rbind(temp_df, df)
    number <<- number+1
  }
  print(paste(as.character(number),"файлов объединилось"))
  return(df)
}
grants2 <- read_data()
filtered.sum <- function(x){
  sum = 0 
  for (i in 1:length(x)){
    if(is.na(x[i]) == F & x[i] > 0 )
    sum <- sum + x[i]
  }
  return(sum)
}
mas <- c(1, -2, 3, NA, NA)
filtered.sum(mas)


outliers.rm <- function(x){
  return(x[x >= quantile(x, probs = c(0.25, 0.75))[1]-1.5*IQR(x) &
                  x <= quantile(x, probs = c(0.25, 0.75))[2]+1.5*IQR(x)])
}