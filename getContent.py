import feedparser
import re
import json

with open('moteurdeRecherche/Flux_RSS_selection.json') as json_selection:
    fluxRSS_dict = json.load(json_selection)
    print(fluxRSS_dict)

selected_keys = ['title','summary','link','published','author']
def getContent(file):
    content = []
    feed = feedparser.parse(file)
    p = re.compile("<.*?>")
    for newsitem in feed['items']:
        article = {}
        for k in selected_keys:
            if k in newsitem:
                article[k] = p.sub ("",newsitem[k])
            if'summary_detail'in newsitem and 'language' in newsitem ['summary_detail']:   
                article['language'] = newsitem['summary_detail']['language']
            content.append(article)
    return content


def allContent (fluxRSS_dict):
    rss_list =[]
    for k,v in fluxRSS_dict.items():
        rss_list.append(getContent(v))
    return rss_list


