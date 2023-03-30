@author: jameslovell
"""

#importing libraries
import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm


#get dataset
data = pd.read_csv("Texas HS SAT Data.csv")


#forming final dataset
dataset = data.loc[:, ["District_Wealth_per_Student", "female_enrollment", "male_enrollment", "Total"]]


#looking at data structure
dataset.dtypes


#transform District Wealth per Student variable
dataset['District_Wealth_per_Student'] = dataset['District_Wealth_per_Student'].str.replace('$', '')
dataset['District_Wealth_per_Student'] = dataset['District_Wealth_per_Student'].str.replace(',', '')
dataset['District_Wealth_per_Student'] = dataset['District_Wealth_per_Student'].astype(float)


#summary statistics
pd.set_option('display.max_columns', None)
dataset.describe()


#plotting continuous variables against the dependent variable
sns.pairplot(data = dataset,
             x_vars = ['male_enrollment', 'female_enrollment', 'District_Wealth_per_Student'],
             y_vars = ['Total'])


#remove outliers
dataset = dataset[dataset["District_Wealth_per_Student"] < 200000]
dataset = dataset[dataset["female_enrollment"] < 2500]
dataset = dataset[dataset["male_enrollment"] < 2000]


#isolate X and Y variables
y = dataset.iloc[:, -1]
X = dataset.iloc[:, :-1]


#linear regression
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
model.summary()












OUTPUT

                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  Total   R-squared:                       0.048
Model:                            OLS   Adj. R-squared:                  0.046
Method:                 Least Squares   F-statistic:                     19.86
Date:                Thu, 30 Mar 2023   Prob (F-statistic):           1.47e-12
Time:                        11:41:31   Log-Likelihood:                -7031.7
No. Observations:                1185   AIC:                         1.407e+04
Df Residuals:                    1181   BIC:                         1.409e+04
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
===============================================================================================
                                  coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------------------
const                        1001.8381      4.054    247.134      0.000     993.885    1009.792
District_Wealth_per_Student    -0.0005      0.000     -4.574      0.000      -0.001      -0.000
female_enrollment               0.2156      0.038      5.613      0.000       0.140       0.291
male_enrollment                -0.1622      0.036     -4.521      0.000      -0.233      -0.092
==============================================================================
Omnibus:                        9.525   Durbin-Watson:                   1.507
Prob(Omnibus):                  0.009   Jarque-Bera (JB):               12.322
Skew:                          -0.091   Prob(JB):                      0.00211
Kurtosis:                       3.465   Cond. No.                     5.81e+04
==============================================================================