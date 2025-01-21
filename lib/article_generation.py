import ollama

class Article_Specification:
    def __init__(self, title, keywords, length, tone):
        self.title = title
        self.keywords = keywords
        self.length = length
        self.tone = tone

    def generate(self):
        self.content = generate_article(self.title)
        return self.content

def generate_article(article_specifications: Article_Specification):
    content = f"Generate a SEO inner content article with the following specifications:\n\nTitle: {article_specifications.title}\nKeywords: {', '.join(article_specifications.keywords)}\nLength: {article_specifications.length} words\nTone: {article_specifications.tone}"
    response = ollama.chat(
        model="llama3.2",
         messages=[
                {"role": "assistant", "content": content}
            ]
    )
    print(response.message.content)
    return response.message.content
    
article = Article_Specification("DUPA TITLE DUPA TUTLE", ["joke", "LLM models"], 10000, "funny")

generate_article(article)
