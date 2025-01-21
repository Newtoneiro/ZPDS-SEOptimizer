import ollama

class ArticleSpecification:
    def __init__(self, title, keywords, length, tone):
        self.title = title
        self.keywords = keywords
        self.length = length
        self.tone = tone

    def generate_prompt(self):
        """Generates a detailed prompt for SEO content creation."""
        prompt = (
            f"Generate a high-quality SEO article with the following specifications:\n\n"
            f"Title: {self.title}\n"
            f"Primary Keywords: {', '.join(self.keywords)}\n"
            f"Target Word Count: {self.length}\n"
            f"Tone of Voice: {self.tone}\n\n"
            f"Please ensure the article is well-structured, engaging, and includes relevant subheadings. Use keywords naturally and provide valuable insights to readers."
        )
        return prompt

def generate_article(article_spec: ArticleSpecification):
    """Generates an SEO article using the provided specifications."""
    prompt = article_spec.generate_prompt()
    
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": "You are an expert SEO content creator."},
            {"role": "user", "content": prompt}
        ]
    )
    
    article_content = response.message.content
    print(article_content)
    return article_content

if __name__ == "__main__":
    article_spec = ArticleSpecification(
        title="The Benefits of AI in Modern Businesses",
        keywords=["AI", "business automation", "machine learning"],
        length=1500,
        tone="professional and informative"
    )

    generate_article(article_spec)
