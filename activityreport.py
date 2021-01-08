import pandas as pd 

directory = 'C:/Users/Peter/Downloads/'
file1 = 'cross-business-export_02_01_2021 18_21_01.csv'

colstouse = ['Sent date', 'Send time', 'Application', 'Offer name', 'Campaign id',\
       'Sent', 'Delivered', 'Bounces', 'Hardbounces', 'Opens', 'Clicks',\
       'Distinct clicks', 'Unsubs', 'Complaints', 'Subject Line', 'List name',\
       'Master filter', 'List and Filter', 'Mailing Category',\
       'Persona Filter', 'Brand', 'List owner']
df = pd.read_csv(directory + file1,encoding = 'ISO-8859-1', usecols = colstouse)

print(df.shape)
print(df.columns)
df.to_csv(directory + 'campaignlookup_dec20.csv', index=False)