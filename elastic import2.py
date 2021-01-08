import time
import progressbar 
import pandas as pd

from es_pandas import es_pandas

directory = 'C:/Users/Peter/Downloads/'
file = 'elastictest2.csv'
# Information of es cluseter
es_host = '192.168.1.219:9200'
index = 'mta1'

# crete es_pandas instance
ep = es_pandas(es_host)

# Example data frame
df = pd.read_csv(directory + file, low_memory=False, encoding = 'utf-8')

# init template if you want
doc_type = 'smtp'
ep.init_es_tmpl(df, doc_type)

# Example of write data to es, use the template you create
ep.to_es(df, index, doc_type=doc_type, thread_count=2, chunk_size=10000)
#ep.to_es(df, index, doc_type=doc_type, _op_type='delete', thread_count=2, chunk_size=10000)