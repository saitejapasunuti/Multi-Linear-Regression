########################### MULTI LINEAR REGRESSION ######################

#prediction moodel for predicting price #################

#load the dataframe
corolla <- read.csv(file.choose())
View(corolla)

attach(corolla)

#gives all the column names
colnames(corolla)

#select the required columns
corolla_new <- corolla[,c('Price','Age_08_04','KM','HP','cc','Doors','Gears','Quarterly_Tax','Weight')]

#exploratory data analysis
#first moment business decision
summary(corolla_new)

#2nd moment business decision
sd(Price)
#3626.965
sd(Age_08_04)
#18.59999
sd(KM)
#37506.45
sd(HP)
#14.98108
sd(cc)
# 424.3868
sd(Doors)
#0.9526766
sd(Gears)
#0.1885104
sd(Quarterly_Tax)
#41.12861
sd(Weight)
#52.64112

##########variance########

var(Price)#13154872
var(Age_08_04)#345.9596
var(KM)#1406733707
var(HP)# 224.4327
var(cc)#180104.1
var(Doors)#0.9075927
var(Gears)#0.03553619
var(Quarterly_Tax)#1691.563
var(Weight)# 2771.088

#scatter plot among the variables of the dataframe
pairs(corolla_new)

#correlation matrix among the variables
cor(corolla_new)

#the linear model of interest
model.corolla <- lm('Price~Age_08_04+KM+HP+cc+Doors+Gears+Quarterly_Tax+Weight')
summary(model.corolla)
#Multiple R-squared:  0.8638,	Adjusted R-squared:  0.863 
# p-value: < 2.2e-16 for overall model
#pvalues for cc and Doors higher than the significance values

model_cc <- lm('Price~cc')
summary(model_cc)
#1.55e-06 pvalue<0.05

model_Doors <- lm('Price~Doors')
summary(model_Doors)
#p value=1.46e-12 <0.05

model2 <- lm('Price~cc+Doors')
summary(model2)
#both the p values are <0.05


##########partial correlation matrix###############
install.packages("corpcor")
library(corpcor)
cor(corolla_new)

cor2pcor(cor(corolla_new))

#######diagnostic plots#######
install.packages("car")
install.packages("carData")
library(carData)
library(car)
plot(model.corolla)

#deletion daignostic for identifying influential variables
influence.measures(model.corolla)
#index plot of influence measures
influenceIndexPlot(model.corolla)

#regression after deleting 81 observation
model.corolla1 <- lm('Price~Age_08_04+KM+HP+cc+Doors+Gears+Quarterly_Tax+Weight',data = corolla_new[-81])
summary(model.corolla1)

#variance inflation factor
vif(model.corolla1)
#vif<10
VIFage <- lm('Age_08_04~KM+HP+cc+Doors+Gears+Quarterly_Tax+Weight')
VIFKM <- lm('KM~Age_08_04+HP+cc+Doors+Gears+Quarterly_Tax+Weight')
VIFHP <- lm('HP~Age_08_04+KM+cc+Doors+Gears+Quarterly_Tax+Weight')
VIFcc <- lm('cc~Age_08_04+KM+HP+Doors+Gears+Quarterly_Tax+Weight')
VIFDoors <- lm('Doors~Age_08_04+KM+HP+cc+Gears+Quarterly_Tax+Weight')
VIFGears <- lm('Gears~Age_08_04+KM+HP+Doors+cc+Quarterly_Tax+Weight')
VIFQT <- lm('Quarterly_Tax~Age_08_04+KM+HP+cc+Doors+Gears+Weight')
VIFweight <- lm('Weight~Age_08_04+KM+HP+cc+Doors+Gears+Quarterly_Tax')

summary(VIFage)
summary(VIFKM)
summary(VIFHP)
summary(VIFcc)
summary(VIFDoors)
summary(VIFGears)
summary(VIFQT)
summary(VIFweight)

finalmodel <- lm('Price~Age_08_04+KM+HP+Gears+Quarterly_Tax+Weight')
summary(finalmodel)
#added variables plots
avPlots(model.corolla1)

vif(model.corolla1)
