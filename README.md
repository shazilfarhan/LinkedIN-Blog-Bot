
# 🧠 LinkedIn Blog Bot

A personal assistant that fetches tech blog articles from curated RSS feeds, summarizes the content using LLM, generates a short quiz, and sends it all to your email — **only if you pass the quiz**.

---

## 📌 Features

- ✅ Fetches latest articles from multiple RSS feeds
- ✅ Parses full article text using `newspaper3k`
- ✅ Summarizes content via OpenAI's GPT API
- ✅ Generates multiple-choice quiz questions based on the article
- ✅ Sends you the summary + link + GitHub attribution via email
- ✅ Skips sending if article was already used
- ✅ All logic runs locally using SQLite for storage

---

## 📂 Tech Stack

- Python 3.11+
- [feedparser](https://pypi.org/project/feedparser/)
- [newspaper3k](https://pypi.org/project/newspaper3k/)
- [OpenAI Python SDK (>=1.0)](https://pypi.org/project/openai/)
- [sqlite3](https://docs.python.org/3/library/sqlite3.html)
- [dotenv](https://pypi.org/project/python-dotenv/)
- SMTP (Gmail/Google Workspace for email)

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/shazilfarhan/linkedin-blog-bot.git
cd linkedin-blog-bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

```env
OPENAI_API_KEY=your-openai-key
EMAIL_ADDRESS=your@email.com
EMAIL_PASSWORD=your-app-password
```

> ⚠️ For Gmail/Google Workspace, use an App Password if 2FA is enabled.

### 4. Run the bot

```bash
python bot.py
```

You'll get a quiz in your terminal. If you pass, the article summary will be emailed to you.

---

## 📚 RSS Sources

The bot currently pulls from curated feeds on:

- Spring Boot
- Java Backend
- System Design
- AI & LLMs
- Optional: Hacker News, Reddit, etc.

You can customize this list in `bot.py`

---

## 📤 Email Output Example

- ✅ Clean LinkedIn-ready summary
- ✅ Preserves paragraph formatting
- ✅ Includes link to original article
- ✅ Attribution with bot + GitHub repo

---

## 🧪 Future Plans

- Add vector DB and semantic search (optional)
- Schedule summaries with cron or GitHub Actions
- Improve quiz generation with context from summary


