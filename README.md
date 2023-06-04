# Summarization and Translation News Article
![./reports/img/work_page.png](reports%2Fimg%2Fwork_page.png)

I got interested in the news summarization and translation project. When I sketched out the idea for my project, I realized that it could be split into 4 parts:
1. Find the news in English 
2. Summarize it 
3. Translate 
4. Display 

![./reports/img/schema.png](reports%2Fimg%2Fschema.png)

When I started this project. I first wanted to write my own web scraper, find a dataset or collect the data myself, and then train my neural model, but after doing a little research on what libraries exist for such tasks. I quickly realized that I wouldn't need to write a lot of code. Each of these 4 parts can be abstracted using the awesome Python library: newspaper3k, transformers and streamlit respectively.

# The experiments
In my work, I did not do fine-tuning of models, but used ready-made ones. So I checked, only their accuracy, speed on my computer.

For summarization I used:
1. prophetnet-large-uncased-cnndm
2. pegasus-cnn_dailymail
3. bart-large-cnn. 

For machine translation: 
1. wmt19-en-ru
2. nllb-200-distilled-600M
3. Helsinki-NLP/opus-mt-en-ru

Test results:
![summ.png](reports%2Fimg%2Fsumm.png)
![mt.png](reports%2Fimg%2Fmt.png)

**Decided to use Bart and wmt19-en-en-ru models**

# Run
## Localhost
If you have docker with GPU& You can run this two scripts.
```bash
docker build -t article-st .
```

```bash
docker run -p 8501:80 article-st
```

## in Colab
If you don't have GPU. Use notebook [streamlit.ipynb](./notebooks/streamlit.ipynb)

![./reports/img/colab_run.png](reports%2Fimg%2Fcolab_run.png)

and a new page will open 
![./reports/img/start_page.png](reports%2Fimg%2Fstart_page.png)