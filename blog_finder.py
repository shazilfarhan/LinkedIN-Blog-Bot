import feedparser
from sql_db import article_exists
import random


def fetch_articles_by_interest(feed_dict, interests):
    results = []
    for category, urls in feed_dict.items():
        for url in urls:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                title = entry.get("title", "").lower()
                summary = entry.get("summary", "").lower()
                if any(kw.lower() in title or kw.lower() in summary for kw in interests):
                      
                    results.append({
                        "title": entry.title,
                        "url": entry.link,
                        "summary": entry.summary,
                        "category": category
                    })
    return results


def select_one_article(articles):
    chosen = random.choice(articles)
    while(article_exists(chosen['url'])):
        chosen = random.choice(articles)
    
    return chosen



