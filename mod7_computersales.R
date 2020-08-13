#######################commputer sales###############################
library(e1071)
cs <- read.csv(file.choose())
View(cs)

attach(cs)
cs <- cs[,-1]

#first moment business decision
summary(cs)

####################2nd moment business decision##################
#standard deviation

sd(price)#580.804
sd(speed)#21.15774
sd(hd)#258.5484
sd(ram)# 5.631099
sd(screen)#0.9051152
sd(ads)#74.83528
sd(trend)#7.873984

#variance

var(price)#337333.2
var(speed)#447.6498
var(hd)#66847.3
var(ram)# 31.70928
var(screen)#0.8192336
var(ads)#5600.32
var(trend)#61.99962

#################3rd moment business decision####################

#####load moments library##############
skewness(price)
#0.7115542
skewness(speed)#0.6568505
skewness(hd)#1.377689
skewness(ram)# 1.38587
skewness(screen)#1.633616
skewness(ads)#-0.5531955
skewness(trend)#0.2366127

##############normal qq plot#################

qqnorm(price)
qqline(price)

qqnorm(speed)
qqline(speed)

qqnorm(hd)
qqline(hd)

qqnorm(ram)
qqline(ram)

qqnorm(screen)
qqline(screen)

qqnorm(ads)
qqline(ads)

qqnorm(trend)
qqline(trend)

#scatterplot

pairs(cs)


colnames(cs)#gives the column names

model <- lm(price~speed + hd + ram + screen + ads + trend + cd + multi + premium, data = cs)
summary(model)
#Multiple R-squared:  0.7756<0.8=>moderate correlation
#p-value: < 2.2e-16<0.05=.overall model is good

model2 <- lm(price~.,data=cs[-c(1441,1701),])
summary(model2)
#Multiple R-squared:  0.7777,	Adjusted R-squared:  0.7774 
# p-value: < 2.2e-16

vif(model2)
#vif<10

avPlots(model2)

model3 <- lm(price~speed + hd + ram + screen + ads + trend  + premium, data = cs[-c(1441,1701),])
summary(model3)
#R-squared:  0.7701
# p-value: < 2.2e-16

avPlots(model3)
plot(model3)

qqPlot(model)













