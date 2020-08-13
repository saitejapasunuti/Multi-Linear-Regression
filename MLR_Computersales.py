################computer sales##################
#pandas deals with the data cleaning ,manipulation,and analysis
import pandas as pd
#numpy deals with the numerical data
import numpy as np

#load the dataset
cs=pd.read_csv("D:\\360digiTMG\module 7\mod7_MR_datasets\Computer_Data.csv")
cs.describe()
cs.head()

#create dummy variables
cs_dummies=pd.get_dummies(cs,columns=['cd','multi','premium'],drop_first=True)
cs.head()


x=cs_dummies.iloc[:,2:11].values
y=cs_dummies.iloc[:,1].values

import seaborn as sns
sns.pairplot(cs_dummies.iloc[:,1:8])#plot excluding dummy variables


import statsmodels.formula.api as sm
mdl1=sm.ols('price ~ speed + hd + ram + screen + ads + trend + cd_yes + multi_yes + premium_yes',data=cs_dummies).fit()
mdl1.summary()
#R-squared:  0.776<0.8=>moderate corelation

rsq_speed = sm.ols('speed ~ + hd + ram + screen + ads + trend + cd_yes + multi_yes + premium_yes',data=cs_dummies).fit().rsquared  
vif_speed = 1/(1-rsq_speed)
#1.2653637174997174
rsq_hd = sm.ols('hd~ speed + ram + screen + ads + trend + cd_yes + multi_yes + premium_yes',data=cs_dummies).fit().rsquared  
vif_hd = 1/(1-rsq_hd)
#4.207394801604396
rsq_ram = sm.ols('ram~ speed + hd + screen + ads + trend + cd_yes + multi_yes + premium_yes',data=cs_dummies).fit().rsquared  
vif_ram = 1/(1-rsq_ram)
#2.9746283364519175
rsq_screen = sm.ols('screen~ speed + hd + ram + ads + trend + cd_yes + multi_yes + premium_yes',data=cs_dummies).fit().rsquared  
vif_screen = 1/(1-rsq_screen)
#1.081643567772372
rsq_ads= sm.ols('ads~ speed + hd + ram + screen+ trend + cd_yes + multi_yes + premium_yes',data=cs_dummies).fit().rsquared  
vif_ads = 1/(1-rsq_ads)
#1.2172178284996031
rsq_trend= sm.ols('trend~ speed + hd + ram + screen+ ads + cd_yes + multi_yes + premium_yes',data=cs_dummies).fit().rsquared  
vif_trend = 1/(1-rsq_trend)
#2.022789919481578
rsq_cd_yes= sm.ols('cd_yes~ speed + hd + ram + screen+ ads + trend + multi_yes + premium_yes',data=cs_dummies).fit().rsquared  
vif_cd_yes = 1/(1-rsq_cd_yes)
#1.8593704748322275
rsq_multi_yes = sm.ols('multi_yes ~ speed + hd + ram + screen+ ads + trend + cd_yes + premium_yes',data=cs_dummies).fit().rsquared  
vif_multi_yes  = 1/(1-rsq_multi_yes)
#1.2905684545693232
rsq_premium_yes = sm.ols('premium_yes ~ speed + hd + ram + screen+ ads + trend + cd_yes + multi_yes',data=cs_dummies).fit().rsquared  
vif_premium_yes  = 1/(1-rsq_premium_yes)
#1.109387913325947

#create dataframe to store all vif values in that
d1 = {'Variables':['speed','hd','ram','screen','ads','trend','cd_yes','multi_yes','premium_yes'],'VIF':[vif_speed,vif_hd,vif_ram,vif_screen,vif_ads,vif_trend,vif_cd_yes,vif_multi_yes,vif_premium_yes]}
vif_frame=pd.DataFrame(d1)
vif_frame

#split data into 30 % test data and 70% train data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)

y_pred=regressor.predict(x_test)

x=np.append(arr=np.ones((6259,1)).astype(int),values=x,axis=1)
x_opt=x[:,[0,1,2,3,4,5,6,7,8,9]]
regression_OLS=sm.OLS(endog=y,exog=x_opt).fit()
regression_OLS.summary()
#R-squared:  0.776<0.8=>moderate corelation
#Adj. R-squared:                  0.775
#Prob (F-statistic):               0.00
