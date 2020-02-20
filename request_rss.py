import feedparser
import json

def requestFromFile(file):
    with open(file) as source:
        file_dict = json.load(source)
    feed_dict = {}
    for key, value in file_dict.items():
        feed_dict[key] = [getCleanItem(item, key) for item in feedparser.parse(value)['entries']]
    return feed_dict
        

def getCleanItem(d, key):
    res = {}
    res['publication'] = key
    res['date'] = d['published'] if 'published' in d else None
    res['title'] = d['title'] if 'title' in d else None
    res['author'] = d['author'] if 'author' in d else None
    res['description'] = d['summary'] if 'summary' in d else None
    res['language'] = d['title_detail']['language'] if 'language' in d['title_detail'] else None
    res['link'] = d['link'] if 'link' in d else None
    return res

if __name__ == "__main__":
    feed_dict = requestFromFile('/home/wamont1-2/Bureau/Python/chap12_elasticsearch/Exercices/es_rss/Flux_RSS_selection.json')
    print(feed_dict['technologyreview'])