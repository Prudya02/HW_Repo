patients <- rbind(c(25,1), c(3,30))
colnames(patients) <- c("yes", "no")
rownames(patients) <- c("Placebo", "Aspirin")
mosaicplot(patients, color = T, shade = T, ylab = "Thromdosis", xlab = "Group", cex.axis = 1, main = "")

dtp <- rbind(c(10,40), c(35,15))
colnames(dtp) <- c("был в дтп", "не был в дтп")
rownames(dtp) <- c("Проходит курсы", "Не проходит курсы")
mosaicplot(dtp, color = T, shade = T, ylab = "был ли в дтп", xlab = "проходил ли курсы", cex.axis = 1, main = "")


fisher.test(cbind(c(1,3),c(3,1)))
 