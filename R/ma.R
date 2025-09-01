my_na_rm <- function(x){
  if (is.numeric(x)){
    stat_test <- shapiro.test(x)
    if (stat_test$p.value > 0.05){
      x[is.na(x)] <- mean(x, na.rm = T)
      print("Mean-замена")
    }
    else{
      x[is.na(x)] <- median(x, na.rm = T)
      print("Median-замена")
    }
    return(x)
  }
  else{
    print("X is not numeric")
  }
}