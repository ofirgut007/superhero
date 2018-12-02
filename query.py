import sys

from elasticsearch import Elasticsearch
 
es = Elasticsearch()
if len(sys.argv) > 1:
   name=sys.argv[1]
else:
   name = 'names'
res = es.search(index="hero", doc_type="superhero", body={"query": {"match": {"name": name}}})
print("we have found %d number of hits for: %s " % (res['hits']['total'],name))
for doc in res['hits']['hits']:
    print("%s) %s" % (doc['_id'], doc['_source']['name']))

