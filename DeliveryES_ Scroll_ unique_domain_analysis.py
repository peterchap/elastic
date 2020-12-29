import requests
#import urllib3
import socket
import pandas as pd
from pandas.io.json import json_normalize
#connect to our cluster
from pandasticsearch import Select, DataFrame
from elasticsearch import Elasticsearch

directory = 'C:/Users/Peter/Downloads/'

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
#a = pd.DataFrame()

# Process hits here
def process_hits(hits):
    for item in hits:
        # Process hits here
        a = Select.from_dict(data).to_pandas()
        print(a.shape)
        print(list(a.columns.values))
        return(a)
#
data = DataFrame.from_es(index="logs", doc_type='mtalogentry', body={	
          "size" : 9999,   
	    "query": {
    "bool":{
    "must": {
        "range": {
          "m_LogDate": {
            "gte": "2020-04-04T00:00:00.000Z",
            "lte": "2020-03-07T00:00:00.000Z"
          }
        }
    }
    }
  },
  "aggs": {
    "unique_domains": {
      "terms": {
        "field": "m_RecipientDomain.keyword"
      }
    }
  }
}
)
df = data.to_pandas()
print(data.print_schema())

#a = Select.from_dict(data).to_pandas()

#print(a.shape)
print(df.shape)
print(df['m_RecipientDomain'].head())

to_dropcols = ['_id', '_index', '_score', '_type','m_LogDate','m_From','m_LogType','m_MessageId','m_SubmissionDate',\
    'm_LogEntry', 'm_StatusCode', 'm_SendingDomain', 'm_To', 'm_Status', 'm_MailerIp', 'm_Process', 'm_LogType', 'm_CampaignId', 'm_MailerId', 'm_ConnectionId', 'm_Type']
df.drop(to_dropcols, axis=1, inplace=True)
#print (a.shape)
#print(list(a.columns.values))
df.drop_duplicates(keep='first', inplace=True)
print (df.shape)
df.to_csv(directory + "uniqueRecipientDomains_mta1.csv", index=False)
#print (data['hits'][1])
#print(df)
