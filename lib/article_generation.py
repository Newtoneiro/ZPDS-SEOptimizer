import ollama


def generate_article(prompt):
    response = ollama.chat(
        model="llama3.2",
        messages=[
        {"role": "user", "content": prompt}
        ]
    )
    print(response.message.content)

    return response.message.content
    


generate_article("Tell me a joke about LLM models")
