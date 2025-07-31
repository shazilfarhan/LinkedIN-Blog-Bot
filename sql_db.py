import sqlite3

def init_db():
    conn = sqlite3.connect("articles.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            url TEXT UNIQUE,
            summary TEXT,
            category TEXT,
            saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def article_exists(url):
    conn = sqlite3.connect("articles.db")
    c = conn.cursor()
    c.execute("SELECT 1 FROM articles WHERE url = ?", (url,))
    exists = c.fetchone() is not None
    conn.close()
    return exists


def save_article(article):
    conn = sqlite3.connect("articles.db")
    c = conn.cursor()
    c.execute('''
        INSERT INTO articles (title, url, summary, category)
            VALUES (?, ?, ?, ?)
        ''', (article['title'], article['url'], article['summary'], article['category']))
    conn.commit()
    conn.close()

def update_full_text(url, full_text):
    conn = sqlite3.connect("articles.db")
    c = conn.cursor()
    c.execute("UPDATE articles SET summary = ? WHERE url = ?", (full_text, url))
    conn.commit()
    conn.close()

def drop_table():
    conn = sqlite3.connect("articles.db")
    c = conn.cursor()
    c.execute("DROP TABLE articles")
    conn.commit()
    conn.close()

def getAnySummary():
    conn = sqlite3.connect("articles.db")
    c = conn.cursor()
    c.execute("SELECT summary from articles")
    summary = c.fetchone()
    conn.close()
    return summary

