import requests
#import urllib3
import socket
import pandas as pd
from pandas.io.json import json_normalize
#connect to our cluster
from pandasticsearch import Select, DataFrame
from elasticsearch import Elasticsearch

directory = 'C:/Users/Peter/Downloads/'

def process_hits(hits):
    for item in hits:
        # Process hits here
        a = Select.from_dict(data).to_pandas()
        print(a.shape)
        print(list(a.columns.values))
        return(a)

retry_count = 5
for retries in range(retry_count):
    try:
        res = requests.get('http://localhost:9200')
        #Jumps Out Of Loop
        break
    except (socket.gaierror, requests.ConnectionError) as e:
        if e.errno != 10054:
            continue
        reconnect()
#Does Something If Loop Never Breaks
else:
  print("Couldn't Connect")

es = Elasticsearch(hosts=["localhost"])
data = es.search(index="logs", body={
  "size": 0,
  "query": {
    "bool": {
      "must":  
         {
        
          "range": {
          "m_LogDate": {
            "gte": "2020-12-21T00:00:00.000Z",
            "lte": "2020-12-28T00:00:00.000Z"
          }
        }
      }
    }
  },
  "aggs": {
    "unique_domains": {
      "terms": {
        "field": "m_RecipientDomain.keyword",
        "size": "9999"
      }
    }
  }
}
)
#a = process_hits(data['aggregations']['unique_domains']['buckets'])
b = data['aggregations']['unique_domains']
print(b.keys())

a = pd.DataFrame.from_dict(b['buckets'])
print(a.shape)
onedrive = 'C:/Users/Peter/OneDrive - Email Switchboard Ltd/Data Cleaning Project/'

status = pd.read_csv(onedrive + "domain_status.csv",\
    encoding = "utf-8",low_memory=False, usecols=['name', 'status'])

df = pd.merge(a, status, left_on=['key'], right_on=['name'], how='left')


#print(df.shape)
print(df.head())
df.to_csv(directory + "uniqueRecipientDomains_mta1_281220.csv", index=False)

#to_dropcols = ['_id', '_index', '_score', '_type','m_LogDate','m_From','m_LogType','m_MessageId','m_SubmissionDate',\
 #    'm_LogEntry', 'm_StatusCode', 'm_SendingDomain', 'm_To', 'm_Status', 'm_MailerIp', 'm_Process', 'm_LogType',\
#     'm_CampaignId', 'm_MailerId', 'm_ConnectionId', 'm_Type']
#df_lst.drop(to_dropcols, axis=1, inplace=True)
#print (a.shape)
#print(list(a.columns.values))
#df_lst.drop_duplicates(keep='first', inplace=True)
#print (df_lst.shape)
#df_lst.to_csv(directory + "uniqueRecipientDomains_mta2.csv", index=False)
#print (data['hits'][1])
#print(df)
