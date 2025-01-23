# SEOptimiser  

SEOptimiser is a user-friendly **Streamlit application** designed to generate high-quality SEO-optimized articles effortlessly. It leverages the **Bielik-7B-Instruct model**, a powerful large language model fine-tuned for Polish text generation tasks.


<div style="text-align: center;">
    <img src="assets/image.png" alt="App Preview" />
</div>
---

## Features  
- Generate **SEO-optimized articles** based on a title, keywords, tone, and length.
- Easily customizable prompts to tailor article generation to your needs.
- Designed with simplicity and efficiency in mind.

---

## Prerequisites  
To run SEOptimiser, you’ll need to install and set up **Ollama**, as well as ensure you have Streamlit installed in your Python environment.


### For more details on the model, check out:
- Bielik model on Ollama: [mwiewior/bielik](https://ollama.com/mwiewior/bielik)  
- Bielik-7B-Instruct on Hugging Face: [speakleash/Bielik-7B-Instruct-v0.1](https://huggingface.co/speakleash/Bielik-7B-Instruct-v0.1)

---

### Step 1: Install Ollama  
Ollama allows you to easily run the Bielik model locally.

1. **Download Ollama**  
   Visit [ollama.com](https://ollama.com/download/windows) and download the installer for Windows. Follow the installation instructions.

2. **Run the Bielik model**  
   Once Ollama is installed, you can run the Bielik model using the following command:  
   ```bash
   ollama run mwiewior/bielik
   ```

### Step 2: Install Requirements  
Make sure you have the necessary Python dependencies installed.

```bash
pip install -r requirenents.txt
```

### Step 3: Run the Streamlit App
Make sure you have the necessary Python dependencies installed.

After installing all prerequisites, run the Streamlit app with the following command:
```bash
streamlit run app.py
```

This will launch the app in your default web browser. Start generating high-quality, SEO-optimized articles in no time!