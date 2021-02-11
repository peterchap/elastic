import requests
#import urllib3
import socket
import pandas as pd
from pandas.io.json import json_normalize
#connect to our cluster
from pandasticsearch import Select
from elasticsearch import Elasticsearch

directory = 'C:/Users/Peter/Downloads/'

retry_count = 5
for retries in range(retry_count):
    try:
        res = requests.get('http://192.168.1.219:9200')
        #Jumps Out Of Loop
        break
    except (socket.gaierror, requests.ConnectionError) as e:
        if e.errno != 10054:
            continue
        reconnect()
#Does Something If Loop Never Breaks
else:
  print("Couldn't Connect")

es = Elasticsearch(hosts=['192.168.1.219'])
df_lst= pd.DataFrame()
# Process hits here
def process_hits(hits):
    for item in hits:
        # Process hits here
        a = Select.from_dict(data).to_pandas()
        print(a.shape)
        print(list(a.columns.values))
        return(a)
#
client_info = Elasticsearch.info(es)
print(client_info)
search_body = {	
        "from" : 0, "size" : 42,   
	    "query" : {  "constant_score" : {     
	        "filter" : {
            "term" :{"m_Status":  "DELIVERED"}
            }
#            {"terms": {
 #               "m_CampaignId" : ["OemPro-3555","2EEZHRC77","2EEZICRSZ"]
#                }
#            },
#            {"range" : {"m_LogDate" : { 
#                "gte" : "2021-01-06T00:00:00.000Z", 
#                "lte" : "2021-01-18"}}
         
                
                            }
                }
            }
search_body2 = {
        "size": 42,
        "query": {
            "match_all": {}
        }
    }
search_body3= {	
          "from" : 0, "size" : 9999,   
	  "query" : {
	    "bool":{
	    "must": [ 
	      {"match" :{"m_status": "DELIVERED"}} 
	      ],
        "terms":[ {
             "m_CampaignId" : ["OemPro-3555","2EEZHRC77","2EEZICRSZ"]
                    }
        ],
	      "filter": [
            
        	{"range" : {"m_LogDate" : { 
                "gte" : "2020-12-29T00:00:00.000Z", 
                "lte" : "2021-01-19"}}}
	        ]
	  }
	  }
}
data = es.search(index="mta*", scroll="3m",body=search_body3)

# Get the scroll ID
sid = data['_scroll_id']
scroll_size = len(data['hits']['hits'])
print(scroll_size)
while scroll_size > 0:
    print("Scrolling...", sid)
    data = es.scroll(scroll_id=sid, scroll='2m')

    # Process current batch of hits
    
    a = process_hits(data['hits']['hits'])
    df_lst = pd.concat([df_lst,a])
    # Update the scroll ID
    sid = data['_scroll_id']

    # Get the number of results that returned in the last scroll
    scroll_size = len(data['hits']['hits'])

#df= Select.from_dict(df_lst).to_pandas()
print (df_lst.shape)
print(list(df_lst.columns.values))

#to_dropcols = ['_id', '_index', '_score', '_type','m_MessageId']
#df_lst.drop(to_dropcols, axis=1, inplace=True)
print (df_lst.shape)
print(list(df_lst.columns.values))
#df_lst = df_lst.sort_values('m_LogDate').drop_duplicates('m_To',keep='last')
print (df_lst.shape)
#df_lst.to_csv(directory + "nomx_190121.csv", index=False)
#print (data['hits'][1])
#print(df)
