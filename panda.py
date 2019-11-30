import pandas as pd 
cars =pd.read_csv('cars.csv')
newdata= pd.concat([cars.head(5),cars.tail(5)])
print('First five and last five rows resulting cars')
print (newdata)