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
            f"Wygeneruj wysokiej jakości artykuł SEO o następujących specyfikacjach:\n\n"
            f"Tytuł: {self.title}\n"
            f"Podstawowe słowa kluczowe: {', '.join(self.keywords)}\n"
            f"Docelowa liczba słów: {self.length}\n"
            f"Ton głosu: {self.tone}\n\n"
            f"Proszę upewnić się, że artykuł jest dobrze zorganizowany, angażujący i zawiera odpowiednie podtytuły. Używaj słów kluczowych naturalnie i dostarczaj cennych informacji czytelnikom."
        )
        return prompt

def generate_article(article_spec: ArticleSpecification):
    """Generates an SEO article using the provided specifications."""
    prompt = article_spec.generate_prompt()
    
    response = ollama.chat(
        model="mwiewior/bielik",
        messages=[
            {"role": "system", "content": "Jesteś ekspertem w tworzeniu treści SEO."},
            {"role": "user", "content": prompt}
        ]
    )
    
    article_content = response.message.content
    print(article_content)
    return article_content

if __name__ == "__main__":
    article_spec = ArticleSpecification(
        title="Korzyści z AI w nowoczesnych firmach",
        keywords=["AI", "automatyzacja biznesu", "uczenie maszynowe"],
        length=1000,
        tone="profesjonalny i informatywny"
    )

    generate_article(article_spec)
