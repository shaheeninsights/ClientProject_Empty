import pandas as pd

food = pd.read_csv("/Users/shaheenkhan/Desktop/AnalystTheBuilder/ClientProject_Empty/u_food_marketing.csv")


food['marital_Divorced'] = food['marital_Divorced'].replace({1:5,0:0})
food['marital_Married'] = food['marital_Married'].replace({1:4,0:0})
food['marital_Single'] = food['marital_Single'].replace({1:3,0:0})
food['marital_Together'] = food['marital_Together'].replace({1:2,0:0})
food['marital_Widow'] = food['marital_Widow'].replace({1:1,0:0})