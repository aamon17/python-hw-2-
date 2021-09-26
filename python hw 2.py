import pandas as pd 
import numpy as np 

df = pd.read_csv(r"C:/GITLAB/uofm-stp-virt-fin-09-2021-u-c/material/02-Python/Homework/PyBank/Resources/budget_data.csv")
#print(df)
total_months = len(df)
# print(total_months)

net_profit = df['Profit/Losses'].mean()

sum_profit = df['Profit/Losses'].sum()
#print(sum_profit)

profitLossesList = list(df['Profit/Losses'])
dateProfitLossesList = df['Date']

changeList = []
counter = 0

numDB = np.array(profitLossesList)
dateNp = np.array(dateProfitLossesList)
date = ""

for i in range(len(df)-1):
    curr = profitLossesList[i]
    currDown = profitLossesList[i+1]
    changeList.append(currDown-curr)
    counter = sum(df['Profit/Losses'])
    minChange = min(changeList)
    maxChange = max(changeList)  
    avgChance = round(np.mean(changeList),2)



maxChangeMonth = dateProfitLossesList[changeList.index(max(changeList))]
minChangeMonth = dateProfitLossesList[changeList.index(min(changeList))]


print('Financial analysis') 
print('total_months: ', total_months)
print('sum profit: $', sum_profit)
print('net_profit/Losses: $', net_profit)
print('greatest increase profits:', maxChangeMonth, '$', maxChange)
print('greatest decrease profits:', minChangeMonth, '$', minChange)