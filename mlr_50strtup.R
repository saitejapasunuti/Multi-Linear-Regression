library(data.table)
strtup <-fread("D:\360digiTMG\supervised\mod 7 multi linear regression\mod7_MR_datasets\\50_Startups.csv")
View(strtup)
attach(strtup)
summary(strtup)
unique(strtup$State)#to chech how many cities are there in the state
strtup <- cbind(strtup, ifelse(strtup$State=="New York",1,0), ifelse(strtup$State=="California",1,0), ifelse(strtup$State=="Florida",1,0))
#created dummy variables

#rename the column
setnames(strtup,"V2","New York")
setnames(strtup, 'V3','California')
setnames(strtup, 'V4','Florida')


#plotting the data
#pairs(strtup) giving error bcz of non numeric data
plot(strtup[,-c('State')])#gives the plot which includes dummy variables also
plot(strtup[,-c('State','New York','California','Florida')])#after removing the state and dummy columns

library(corpcor)#is used to estimate the covariance and corelation of the sample data
cor2pcor(cor(strtup[,-c('State','New York','Florida')]))
colnames(strtup)

Profit_Model <- lm(Profit~`R&D Spend`+Administration+`Marketing Spend`, data = strtup)
summary(Profit_Model)
# 0.602 pvalue of Administration is high so now check influencing records
#Multiple R-squared:  0.9507

library(car)
influenceIndexPlot(Profit_Model)#diagnostic plots
#Provides index plots of Cook's distances, leverages, Studentized residuals, and outlier significance levels for a regression object.
influencePlot(Profit_Model,id.n=3)

## Regression after deleting the 50 and 49th observation
Profit_Model_Inf <- lm(Profit~`R&D Spend`+Administration+`Marketing Spend`,data = strtup[-c(50,49),])
summary(Profit_Model_Inf)

Profit_Model <- lm(Profit~`R&D Spend`+Administration+`Marketing Spend`,data = strtup)
class(strtup$`Marketing Spend`)
vif(Profit_Model)
summary(Profit_Model)
#vif>10=>there exists collinearity among all variables
#added variable plots to check correlaton b/w o/p variables
avPlots(Profit_Model)

Profit_Model_Revised <- lm(Profit~`R&D Spend`+Administration+`Marketing Spend`+`New York`+California+Florida,data=strtup)

library(MASS)
stepAIC(Profit_Model_Revised)
#lower the AIC(Alkike Information Criterion) better the model AIC used only when u use multiple models

Profit_Model_Final <- lm(Profit~`R&D Spend`,data=strtup)
summary(Profit_Model_Final)
plot(Profit_Model_Final)
qqPlot(Profit_Model_Final,id.n=5)
#R-squared:  0.9465
#p-value: < 2.2e-16


