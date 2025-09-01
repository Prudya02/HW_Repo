df <- mtcars
df$vs <- factor(df$vs, labels = c('C','V'))
df$am <- factor(df$am, labels = c('Auto','Manual'))
