#############MULTILINEAR REGRESSION ################
#pandas is used for data manipulation,cleaning,analysis
import pandas as pd
#it deals with numerical data
import numpy as np

#loading the data
strup=pd.read_csv('D:\\360digiTMG\mod 7 multi linear regression\mod7_MR_datasets\\50_startups.csv')

x=strup.iloc[:,:-1].values
y=strup.iloc[:,4].values

#we can use label encoder and one hotencoder to create dummy variables
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder=LabelEncoder()
x[:,3]=labelencoder.fit_transform(x[:,3])

onehotencoder=OneHotEncoder(categorical_features=[3])
x=onehotencoder.fit_transform(x).toarray()
##created dummy variables by converting one column to 3 columns

x=x[:,1:]
#removing first column index

#split data into 30 % test data and 70% train data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)

y_pred=regressor.predict(x_test)

import statsmodels.formula.api as sm
#We’ll input a matrix of 50 lines and one column with 1s inside.
#line=0,colums=1
x=np.append(arr=np.ones((50,1)).astype(int),values=x,axis=1)
x_opt=x[:,[0,1,2,3,4,5]]
regressor_ols=sm.OLS(endog=y,exog=x_opt).fit()
#endog=our dependent variables & exog=matrix with the intercept
regressor_ols.summary()
#x2= 0.990 consists of highest p value

x_opt=x[:,[0,1,3,4,5]]
regressor_ols=sm.OLS(endog=y,exog=x_opt).fit()
regressor_ols.summary()
#p value=0.953>0.05=>remove column 1
x_opt=x[:,[0,3,4,5]]
regressor_OLS=sm.OLS(endog=y,exog=x_opt).fit()
regressor_OLS.summary()
#p value=0.608>0.05=>remove column 4
x_opt=x[:,[0,3,5]]
regressor_OLS=sm.OLS(endog=y,exog=x_opt).fit()
regressor_OLS.summary()
#p-value=0.060>0.05=>remove column 5
x_opt=x[:,[0,3]]
regressor_OLS=sm.OLS(endog=y,exog=x_opt).fit()
regressor_OLS.summary()
#p value =0.000<0.05
#data that can predict profits with the highest impact is composed of only one category: R&D spending!

#R-squared: 0.947
#Prob (F-statistic): 3.50e-32<0.05


