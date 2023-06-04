FROM python:3.9

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Create a directory to store the models
RUN mkdir models

# Download and save the models to the "models" directory
RUN python -c "from transformers import AutoModelForSeq2SeqLM, AutoTokenizer; \
    tokenizer_name = 'facebook/bart-large-cnn'; \
    summarizer_model_name = 'facebook/bart-large-cnn'; \
    translator_model_name = 'facebook/wmt19-en-ru'; \
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name); \
    tokenizer.save_pretrained('/app/models/tokenizer'); \
    summarizer_model = AutoModelForSeq2SeqLM.from_pretrained(summarizer_model_name); \
    summarizer_model.save_pretrained('/app/models/summarizer'); \
    translator_model = AutoModelForSeq2SeqLM.from_pretrained(translator_model_name); \
    translator_model.save_pretrained('/app/models/translator')"

COPY . .

CMD ["streamlit", "run", "--server.port", "80", "main.py"]
