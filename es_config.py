from elasticsearch import Elasticsearch, helpers
import request_rss as rrss
import json

def createIndex(index_name, mapping_file):
    with open(mapping_file) as source:
        mapping = json.load(source)
    es = Elasticsearch()
    return es.indices.create(index_name , body = mapping)

def putBulk(feed_dict):
    es = Elasticsearch()
    return helpers.bulk(es, feed_dict)

def gendata(feed_dict):
    for key, value in feed_dict.items():
        for doc in value:
            doc["_index"] = "feed_rss"
            doc["_type"] = "_doc"
            yield doc


if __name__ == "__main__":
    #es = Elasticsearch()
    #es.indices.delete('feed_rss')
    createIndex('feed_rss', 'mappings.json')
    feed_dict = rrss.requestFromFile('/home/wamont1-2/Bureau/Python/chap12_elasticsearch/Exercices/es_rss/Flux_RSS_selection.json')
    putBulk(gendata(feed_dict))
