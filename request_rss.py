import feedparser
import json
import datetime

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
    if 'published' in d and d['published']:
        if key == "technologyreview":
            res['date'] = datetime.datetime.strptime(d['published'], "%a, %d %b %Y %H:%M:%S %Z").strftime("%Y-%m-%dT%H:%M:%S+0000")
        else:
            res['date'] = d['published']
    if 'title' in d and d['title']:
        res['title'] = d['title']
    if 'author' in d and d['author']:
        res['author'] = d['author'] 
    if 'summary' in d and d['summary']:
        res['description'] = d['summary']
    if 'language' in d['title_detail'] and d['title_detail']['language']:
        res['language'] = d['title_detail']['language']
    if 'link' in d and d['link']:
        res['link'] = d['link']
    return res

if __name__ == "__main__":
    feed_dict = requestFromFile('/home/wamont1-2/Bureau/Python/chap12_elasticsearch/Exercices/es_rss/Flux_RSS_selection.json')
    #print(feed_dict['technologyreview'])