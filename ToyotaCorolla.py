############## MULTI LINEAR REGRESSION ##################

#pandas deals with the data manipulation,data cleaning and analysis
import pandas as pd
#numpy deals with the numeric data
import numpy as np
corolla=pd.read_csv("D:\\360digiTMG\mod 7 multi linear regression\mod7_MR_datasets\ToyotaCorolla.csv",encoding="latin",index_col=0)

index=corolla.index
index#gives the index of the dataset

columns=corolla.columns
columns#gives the column names

values=corolla.values
values
# pick the required columns and drop the remaining columns 
corolla=corolla[['Price','Age_08_04','KM','HP','cc','Doors','Gears','Quarterly_Tax','Weight']]

#exploratory data analysis
corolla.describe()

#scatter plot betwen the variables along with the histograms
#seaborn is data visualization library based on matplotlib
import seaborn as sns
sns.pairplot(corolla.iloc[:,:9])

#correlation matrix
corolla.corr()

#statsmodel provides classes and functions to explore data ,estimate statistical models and to perform statistical calculations
import statsmodels.formula.api as sm

#
mdl1=sm.ols('Price~Age_08_04+KM+HP+cc+Doors+Gears+Quarterly_Tax+Weight',data=corolla).fit()
mdl1.summary()
#ols regression results
#R-squared: 0.864>0.8=>strong correlation
#Adj. R-squared:  0.863
#Prob (F-statistic):0.00<0.05=>overall the model is good

#p values of cc and Doors are above the significance levels

#calculating vif values for independent variables
rsq_Age_08_07=sm.ols('Age_08_04~KM+HP+cc+Doors+Gears+Quarterly_Tax+Weight',data=corolla).fit().rsquared
vif_Age_08_04=1/(1-rsq_Age_08_07)
#1.8846198056602868

rsq_KM=sm.ols('KM~Age_08_04+HP+cc+Doors+Gears+Quarterly_Tax+Weight',data=corolla).fit().rsquared
vif_KM=1/(1-rsq_KM)
#1.7569047782042881

rsq_HP=sm.ols('HP~Age_08_04+KM+cc+Doors+Gears+Quarterly_Tax+Weight',data=corolla).fit().rsquared
vif_HP=1/(1-rsq_HP)
#1.4194221086310974

rsq_cc=sm.ols('cc~Age_08_04+KM+HP+Doors+Gears+Quarterly_Tax+Weight',data=corolla).fit().rsquared
vif_cc=1/(1-rsq_cc)
#1.1638939849423797

rsq_Doors=sm.ols('Doors~Age_08_04+KM+HP+cc+Gears+Quarterly_Tax+Weight',data=corolla).fit().rsquared
vif_Doors=1/(1-rsq_Doors)
#1.156575207076043

rsq_Gears=sm.ols('Gears~Age_08_04+KM+HP+cc+Doors+Quarterly_Tax+Weight',data=corolla).fit().rsquared
vif_Gears=1/(1-rsq_Gears)
#1.098723019347037

rsq_Quarterly_Tax=sm.ols('Quarterly_Tax~Age_08_04+KM+HP+cc+Doors+Gears+Weight',data=corolla).fit().rsquared
vif_Quarterly_Tax=1/(1-rsq_Quarterly_Tax)
#2.311430811531038

rsq_Weight=sm.ols('Weight~Age_08_04+KM+HP+cc+Doors+Gears+Quarterly_Tax',data=corolla).fit().rsquared
vif_Weight=1/(1-rsq_Weight)
#2.516419837445868

#storing vif values in a dataframe
d1={'variables':['Age_08_04','KM','HP','cc','Doors','Gears','Quarterly_Tax','Weight'],'VIF':[vif_Age_08_04,vif_KM,vif_HP,vif_cc,vif_Doors,vif_Gears,vif_Quarterly_Tax,vif_Weight]}
Vif_frame=pd.DataFrame(d1)
Vif_frame
# all vif values are less than 10

mdl_cc=sm.ols('Price~cc',data=corolla).fit()
mdl_cc.summary()
# 0.000 

mdl_Doors=sm.ols('Price~Doors',data=corolla).fit()
mdl_Doors.summary()
#0.000

mdl_2=sm.ols('Price~cc+Doors',data=corolla).fit()
mdl_2.summary()
#0.000

import statsmodels.api as sma
sma.graphics.influence_plot(mdl1)
#influnce plot is used to know the values which influnce the model

#removing the index values which influence the model
corolla_new=corolla.drop(corolla.index[[81]],axis=0)

mdl_new=sm.ols('Price~Age_08_04+KM+HP+cc+Doors+Gears+Quarterly_Tax+Weight',data=corolla_new).fit()
mdl_new.summary()

final_mdl=sm.ols('Price~Age_08_04+KM+HP+Gears+Quarterly_Tax+Weight',data=corolla_new).fit()
final_mdl.summary()
#R-squared:0.863>0.8=>strong correlation
#Adj. R-squared: 0.863
#Prob (F-statistic): 0.00=>overall the model is good

#spliting the data into test and train data
from sklearn.model_selection import train_test_split
corolla_train,corolla_test=train_test_split(corolla,test_size=0.3)

#preparing the model based on train data
model_train=sm.ols('Price~Age_08_04+KM+HP+Gears+Quarterly_Tax+Weight',data=corolla_train).fit()

#train dataset prediction
train_pred = model_train.predict(corolla_train)

#train residual values
train_resid=train_pred-corolla_train.Price

#rmse values for train data
train_rmse=np.sqrt(np.mean(train_resid*train_resid))
#1339.6242497581725

#prediction on test dataset
test_pred=model_train.predict(corolla_test)

#test residual values
test_resid=test_pred-corolla_test.Price

test_rmse=np.sqrt(np.mean(test_resid*test_resid))
#1343.2711111314393








