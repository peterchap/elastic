import requests
import pandas as pd
from pandas.io.json import json_normalize
#connect to our cluster
from pandasticsearch import Select
from elasticsearch import Elasticsearch

def blocker (row):
    if ('cyren') in row['m_LogEntry'].lower():
        return 'Cyren'
    if ('symantec') in row['m_LogEntry'].lower():
        return 'Symantec'
    if ('proofpoint') in row['m_LogEntry'].lower():
        return 'Proofpoint'
    if ('barracuda') in row['m_LogEntry'].lower():
        return 'Barracuda'
    if ('trend') in row['m_LogEntry'].lower():
        return 'Trend Micro'
    if ('mimecast') in row['m_LogEntry'].lower():
        return 'Mimecast'
    if ('cloudmark') in row['m_LogEntry'].lower():
        return 'Cloudmark'
    if ('spamhaus/invaluement/returnpath') in row['m_LogEntry'].lower():
       return 'Spamhaus/Invaluement/ReturnPath'    
    if ('spamhaus') in row['m_LogEntry'].lower():
        return 'Spamhaus'
    if ('invaluement') in row['m_LogEntry'].lower():
        return 'Invaluement'
    if ('return path') in row['m_LogEntry'].lower():
        return 'Return Path'
    if ('returnpath') in row['m_LogEntry'].lower():
        return 'Return Path'
    if ('ers-rbl') in row['m_LogEntry'].lower():
        return 'ERS-RBL'
    if ('spamcop') in row['m_LogEntry'].lower():
        return 'SpamCop'
    if ('sophos') in row['m_LogEntry'].lower():
        return 'Sophos'   
    return 'Unknown'

directory = 'C:/Users/Peter/Downloads/'

res = requests.get('http://localhost:9200')
es = Elasticsearch(hosts=["localhost"])
#
data = es.search(index="logs*", body={	
          "from" : 0, "size" : 9999,  
	  "query" : {
	  "bool":{
	    "must": [
	      {"match" :{"m_Status": "bounced defered"}}
	      ],
	      "filter": [
                {"terms" : {"m_LogEntry": 
                ["cyren", "symantec", "proofpoint", "barracuda", "trend", "mimecast",
                "cloudmark", "spamhaus", "invaluement","overquota" "return path", "returnpath"  ]}},
	        {"range" : {"m_LogDate" : { 
            "gte" : "2020-12-21T00:00:00.000Z", 
            "lte" : "2020-12-28"}}},
               
	        ]
	  }
	  }
})

df= Select.from_dict(data).to_pandas()
df.drop_duplicates(subset='m_To',keep='last',inplace=True)
df.to_csv(directory+"blocksall1306maymta2.csv", index=False)

df['Blocker'] = df.apply (lambda row: blocker(row), axis=1)
    
to_dropcols = ['m_LogEntry', 'm_LogDate','_id', '_index', '_score', '_type',\
'm_From','m_LogType','m_MessageId', 'm_SubmissionDate']
df.drop(to_dropcols, axis=1, inplace=True)
print (df.shape)
print(list(df.columns.values))
print(df)
#print (data['hits'][1])10.csv"
df.to_csv(directory+"blocks28decmta1.csv", index=False)
