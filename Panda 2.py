# PANDAS PROBLEM #2

import pandas as pd 
cars =pd.read_csv('cars.csv')

PROBLEM_a= cars[['Model','cyl','hp','wt','vs','gear']].head(5)

PROBLEM_b= cars.loc[cars['Model']=='Mazda RX4']


PROBLEM_c= cars.loc[cars['Model']=='Camaro Z28',['Model','cyl']]

D= cars.loc[cars['Model'].isin(['Mazda RX4 Wag','Honda Civic','Ford Pantera L'])]
PROBLEM_d= D[['Model','cyl','gear']]


