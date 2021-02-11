import time
import progressbar 
import pandas as pd

from es_pandas import es_pandas

directory = 'C:/Users/Peter/Downloads/'
file = 'elastictest6.csv'
# Information of es cluseter
es_host = '192.168.1.219:9200'
index = 'mta1'

# crete es_pandas instance
ep = es_pandas(es_host)

# Example data frame
datecols = ['m_LogDate', 'm_SubmissionDate']
df = pd.read_csv(directory + file, low_memory=False, encoding = 'utf-8', parse_dates=datecols)


# init template if you want
doc_type = 'smtp'
ep.init_es_tmpl(df, doc_type)

# Example of write data to es, use the template you create
ep.to_es(df, index, doc_type=doc_type, thread_count=2, chunk_size=10000)

# Example of delete
#ep.to_es(df, index, doc_type=doc_type, _op_type='delete', thread_count=2, chunk_size=10000)

# Update doc by doc _id
#df.iloc[:1000, 1] = 'Bye'
#df.iloc[:1000, 2] = pd.datetime.now()
ep.to_es(df.iloc[:1000, 1:], index, doc_type=doc_type, _op_type='update')#