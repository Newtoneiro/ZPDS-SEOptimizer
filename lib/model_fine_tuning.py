import os
import json
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
from datasets import Dataset

TRAIN_DATA_PATH = os.path.join(os.path.dirname(__file__), "fine_tune_data.json")

tokenizer = AutoTokenizer.from_pretrained("speakleash/Bielik-7B-Instruct-v0.1")
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained("speakleash/Bielik-7B-Instruct-v0.1")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def get_prompt(title, keywords, length, tone):
    prompt = [
        "Chcę, abyś odpowiedział w roli bardzo utalentowanego copywritera, który specjalizuje się w tworzeniu artykułów."
        "Chcę, abyś generował WYŁĄCZNIE treść artykułu - bez komentarzy, bez TAGÓW, bez tytułów sekcji, podsumowań, bez uwag - NICZEGO."
        "Masz zwrócić czysty tekst."
        "Wygeneruj wysokiej jakości artykuł SEO zgodnie z poniższymi wytycznymi:\n\n"
        f"Tytuł: {title}\n"
        f"Podstawowe słowa kluczowe: {', '.join(keywords)}\n"
        f"Docelowa liczba słów: {length}\n"
        f"Ton wypowiedzi: {tone}\n\n"
        "Upewnij się, że artykuł jest dobrze zorganizowany, angażujący i zawiera odpowiednie śródtytuły."
        "Używaj słów kluczowych w naturalny sposób i dostarczaj czytelnikom wartościowych informacji."
    ]
    return " ".join(prompt)


def prepare_dataset():
    with open(TRAIN_DATA_PATH, "r", encoding="utf-8") as file:
        raw_data = json.load(file)

    preprocessed_data = []
    for entry in raw_data:
        prompt = get_prompt(
            title=entry["title"], 
            keywords=entry["keywords"].split(","), 
            length=entry["length"], 
            tone=entry["tone"]
        )
        preprocessed_data.append({"prompt": prompt, "article": entry["article"]})

    hf_dataset = Dataset.from_dict({
        "prompt": [item["prompt"] for item in preprocessed_data],
        "article": [item["article"] for item in preprocessed_data]
    })

    return hf_dataset


def preprocess_function(examples):
    inputs = examples["prompt"]
    targets = examples["article"]

    # Tokenize inputs
    model_inputs = tokenizer(inputs, max_length=512, truncation=True, padding="max_length")
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(targets, max_length=512, truncation=True, padding="max_length")

    model_inputs["labels"] = labels["input_ids"]

    return model_inputs


if __name__ == "__main__":
    dataset = prepare_dataset()
    tokenized_dataset = dataset.map(preprocess_function, batched=False)

    training_args = TrainingArguments(
        output_dir="./results",
        eval_strategy="no",
        learning_rate=2e-5,
        per_device_train_batch_size=4,
        num_train_epochs=1,  # 1 epoch needed for example purposes
        save_total_limit=1,
        save_steps=500,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
    )

    trainer.train()
