library(caret)
setwd("C:/Users/Alessandro/Dropbox/OnlineCourses/datasci_course_materials/assignment5/")
%%setwd("C:/Users/Alessandro/Desktop/Documenti/Dropbox/OnlineCourses/datasci_course_materials/assignment5/")

seaflow <- read.csv(file = 'seaflow_21min.csv')
%% this is to calculate question 2
length(seaflow$pop[seaflow$pop == 'synecho'])

 %% this is to calculate question 3
summary(seaflow)

%% this is to calculate question 4
%% require(caTools) # using the caTools package
set.seed(2345)   # setting the seed to be able to reproduce
trainIndex <- createDataPartition(seaflow$file_id, p=.5, list=FALSE)
seaTrain <- seaflow[trainIndex,]
seaTest  <- seaflow[-trainIndex,]

%%seaSplit <- sample.split(Y          = seaflow$file_id, 
%%                         SplitRatio = 0.5)
%%seaTrain <- seaflow[seaSplit, ]
%%seaTest  <- seaflow[!seaSplit, ]

mean <- mean(seaTrain$time)
mean

plot(seaflow$pe , seaflow$chl_small,col=c("red","blue","green","yellow","black")[seaflow$pop])
legend(x="topright", legend = levels(seaflow$pop), col=c("red","blue","green","yellow","black"), pch=1)

library(rpart)
fol <- seaTrain$pop ~ seaTrain$fsc_small + seaTrain$fsc_perp + seaTrain$fsc_big + seaTrain$pe + seaTrain$chl_big + seaTrain$chl_small
model <- rpart(fol, method="class", data=seaTrain)
print(model)

pred <- predict(model, newdata = seaTrain, type='class')
acc <- sum(seaTrain$pop == pred)/length(seaTrain$pop == pred)
acc 

%% question 10
library(randomForest)
model1 <- randomForest(fol,data=seaTrain)
pred1 <- predict(model1,newdata = seaTest[1:11],type='class')
acc1 <- sum(seaTrain$pop == pred1)/length(seaTrain$pop == pred1)
acc1

%% question 11
importance(model1)

%% question 12 
library(e1071) 
model2 <- svm(fol, data=seaTrain)
pred2 <- predict(model2,newdata = seaTrain,type='class')
acc2 <- sum(seaTrain$pop == pred2)/length(seaTrain$pop == pred2)
acc2

%% question 13 confusion matrix
conf <- table(pred = pred, true = seaTest[1:length(seaTrain$pop),]$pop)
conf1 <- table(pred = pred1, true = seaTest[1:length(seaTrain$pop),]$pop)
conf2 <- table(pred = pred2, true = seaTest[1:length(seaTrain$pop),]$pop)
conf

%% question 14
seaflownew <- seaflow[1]==208
seaflow2 <- seaflow[!seaflownew,]
set.seed(2345)
trainIndex <- createDataPartition(seaflow2$pop, p=.5, list=FALSE)
seaTrain1 <- seaflow2[trainIndex,]
seaTest1 <- seaflow2[-trainIndex,]


summary(seaTest)
fol1 <- seaTrain1$pop ~ seaTrain1$fsc_small + seaTrain1$fsc_perp + seaTrain1$fsc_big + seaTrain1$pe + seaTrain1$chl_big + seaTrain1$chl_small
model3 <- svm(fol, data=seaTrain1)
pred3 <- predict(model3,newdata = seaTrain1,type='class')
sum(seaTrain1$pop == pred3)/length(seaTrain1$pop == pred3)
acc3 <- sum(seaTrain1$pop == pred3)/length(seaTrain1$pop == pred3)
acc2 - acc3

mean
acc
acc1
acc2
acc2 - acc3


