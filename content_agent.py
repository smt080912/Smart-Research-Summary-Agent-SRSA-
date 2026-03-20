import openai
import requests
from bs4 import BeautifulSoup

class ContentAgent:
    def __init__(self, api_key, model="gpt-3.5-turbo"):
        self.api_key = api_key
        self.model = model
        openai.api_key = self.api_key

    def fetch_content(self, query):
        """
        简单搜索网页并抓取文本内容（演示用，真实爬取可用更复杂的方法）
        """
        try:
            search_url = f"https://www.google.com/search?q={query}"
            headers = {"User-Agent": "Mozilla/5.0"}
            resp = requests.get(search_url, headers=headers)
            soup = BeautifulSoup(resp.text, "html.parser")
            # 抓取前几个搜索结果的文本
            texts = [p.get_text() for p in soup.find_all("p")]
            content = "\n".join(texts[:5])
            return content if content else "未抓取到内容"
        except Exception as e:
            return f"抓取内容失败: {e}"

    def summarize_content(self, content):
        """
        用最新 OpenAI API 生成摘要
        """
        prompt = f"请帮我总结以下内容:\n{content}"
        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "你是一个帮助用户抓取资料并总结的助手"},
                    {"role": "user", "content": prompt}
                ]
            )
            summary = response.choices[0].message.content
            return summary
        except Exception as e:
            return f"生成摘要失败: {e}"

    def generate_summary_from_query(self, query):
        content = self.fetch_content(query)
        summary = self.summarize_content(content)
        return summary
