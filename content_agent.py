import openai
import requests
from bs4 import BeautifulSoup

class ContentAgent:
    def __init__(self, api_key):
        openai.api_key = api_key

    # 资料抓取
    def fetch_web_content(self, query):
        # 抓取维基百科内容
        url = f"https://en.wikipedia.org/wiki/{query.replace(' ','_')}"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        paragraphs = soup.find_all("p")
        content = "\n".join([p.get_text() for p in paragraphs])
        return content

    # 使用GPT生成摘要
    def summarize_content(self, content):
        prompt = f"请根据以下内容生成简明摘要：\n\n{content}"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    # 一步完成搜索并概括
    def generate_summary_from_query(self, query):
        content = self.fetch_web_content(query)
        summary = self.summarize_content(content)
        return summary