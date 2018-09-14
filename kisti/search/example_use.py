from datetime import datetime
from elasticsearch import Elasticsearch

# by default we connect to localhost:9200
es = Elasticsearch()
# result = es.get(index="website", doc_type="preprint", query="*칼로리발란스*")['_source']
result = es.search(index="website", doc_type="preprint", q="초록")
print(result)
