
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY") , base_url="https://openrouter.ai/api/v1")

def summarize_article(article_text):
    response = client.chat.completions.create(
        model="deepseek/deepseek-r1-0528:free",
        messages=[
            {"role": "system", "content": "You are a software engineer reading the article to stay upto date. You will be creating linkedIN posts, just return the post contents"},
            {"role": "user", "content": f"Summarize this article, include technical details and prepare it for a linkedin post:\n\n{article_text}"}
        ],
        stream= False
    )
    return response.choices[0].message.content.strip()

def generate_mcqs(text, client):
    prompt = f"""
    Based on the following content, generate 10 multiple-choice question with 4 options.
    Mark the correct answer with an asterisk (*):

    {text}
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
