import pandas as pd 

directory = 'C:/Users/Peter/Downloads/'
file1 = 'mta_bounced_211220.csv'

colstouse = ['m_LogDate', 'm_SubmissionDate', 'm_CampaignId', 'm_MessageId',\
     'm_LogEntry', 'm_StatusCode', 'm_SendingDomain', 'm_RecipientDomain',\
     'm_From', 'm_To', 'm_Status', 'm_MailerIp']

df = pd.read_csv(directory + file1, encoding = 'utf-8', usecols = colstouse)
text = 'The email account that you tried to reach is over quota'
google = df[df['m_LogEntry'].str.contains(text, regex=False)]
google.drop_duplicates(subset=['m_To'],keep='last', inplace=True)
print(google.shape)
print(google['m_To'])
google.to_csv(directory + 'google2.csv', index=False)