import pandas as pd 

directory = 'C:/Users/Peter/Downloads/'
file1 = 'elastictest4.csv'

colstouse = ['m_LogDate', 'm_SendingDomain','m_MailerIp','blocker']
values = ['Delivered', 'Expired', 'Verizon Undeliverable email','Google Spam Throttle',\
    '1&1 Throttled','BT Spam Throttle', 'Apple Throttled','Google Over Quota','Throttled',\
    'Other Undeliverable email', 'Google Over Quota', 'Other Unknown', 'Spam Throttle',\
    'Office365 Throttled', 'Office365 Unknown', 'Undeliverable email', 'Apple Over Quota',\
    'Microsoft Throttled', 'Virgin Unknown', 'No MX', 'Other Over Quota', 'Talk Talk Undeliverable email',\
    'GMail Unknown', 'Unknown', '1&1 Undeliverable email', 'Virgin Undeliverable email',\
    'Verizon Unknown', 'BT Throttled']
df = pd.read_csv(directory + file1, encoding = 'utf-8', usecols = colstouse)
df['m_LogDate'] = pd.to_datetime(df['m_LogDate']).round('D')
print(df.shape)
df1 = df[~df['blocker'].isin(values)].copy()
print(df1.shape)
print(df1['blocker'].value_counts())
df1.drop_duplicates(subset=colstouse,keep='last', inplace=True)
print(df1.shape)
df1.to_csv(directory + 'blocksummary.csv', index=False)