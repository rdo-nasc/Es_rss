from elasticsearch import Elasticsearch, helpers
import request_rss

def createIndex(index_name, mapping_file):
    with open(mapping_file) as source:
        mapping = json.load(source)
    es = Elasticsearch()
    es.indices.create(index_name , body = mapping)

createIndex('feed_rss', 'mappings.json')
