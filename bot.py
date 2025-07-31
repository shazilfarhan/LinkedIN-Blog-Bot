from sql_db import * 
from blog_finder import *
from scraper import *
from llm_client import *
from email_summary import *
from linkedIN_prep import format
from quiz_taker import quizEngine


interests = ["spring boot", "system design", "LLM", "vector db", "kubernetes", "aws", "java"]


rss_feeds = {
    "spring_java_backend": [
        "https://www.baeldung.com/feed",
        "https://reflectoring.io/index.xml",
        "https://feeds.feedburner.com/javacodegeeks",
        "https://feed.infoq.com/java"
    ],
    "system_design": [
        "https://bytebytego-newsletter.beehiiv.com/feed",
        "http://highscalability.com/home/rss.xml"
    ],
    "ai_llm": [
        "https://www.latent.space/rss",
        "https://weaviate.io/blog/rss.xml",
        "https://www.pinecone.io/blog/rss.xml",
        "https://huggingface.co/blog/rss.xml"
    ],
    "cloud_devops_general": [
        "https://aws.amazon.com/blogs/aws/feed/",
        "https://cloud.google.com/blog/rss",
        "https://www.thoughtworks.com/en-us/rss"
    ]
}


def main():

    init_db()
    articles = fetch_articles_by_interest(rss_feeds, interests)
    chosen = select_one_article(articles)
    chosen_text = extract_article_text(chosen['url'])
    summary =summarize_article(chosen_text)
    if(quizEngine(chosen_text, chosen['url'])):
        send_email('LinkedIN Post for article '+ chosen['title'], format(summary,chosen['url']))
        save_article(chosen)
        update_full_text(chosen['url'],chosen_text)
        print('Email sent!')

    else:
        print("You didnt read/understand the article. You wont get the summary")

main()




