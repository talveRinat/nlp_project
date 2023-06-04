from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import streamlit as st
import newspaper
import nltk

nltk.download('punkt')


def summarize_text(text, tokenizer, model, max_length=512, min_length=30):
    inputs = tokenizer(text, max_length=max_length, truncation=True, return_tensors='pt')
    summary_ids = model.generate(inputs.input_ids, num_beams=4, max_length=max_length, min_length=min_length, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary


def translate_text(text, tokenizer, model, max_length=512):
    inputs = tokenizer(text, max_length=max_length, truncation=True, return_tensors='pt')
    translation_ids = model.generate(inputs.input_ids, num_beams=4, max_length=max_length, early_stopping=True)
    translation = tokenizer.decode(translation_ids[0], skip_special_tokens=True)
    return translation


# Define the streamlit app
def main():
    st.title('Article Summarizer and Translation')

    url = st.text_input('', placeholder='Paste the URL of the article and press Enter')

    if url:
        try:
            article = newspaper.Article(url)
            article.download()
            article.parse()

            img = article.top_image
            st.image(img)

            title = article.title
            st.subheader(title)

            article.nlp()

            tab1, tab2, tab3 = st.columns(3)

            with tab1:
                st.subheader('Full Text')
                txt = article.text.replace('Advertisement', '')
                st.write(txt)

            with tab2:
                st.subheader('Summary')
                summary = summarize_text(txt, summarizer_tokenizer, summarizer_model)
                st.write(summary)

            with tab3:
                st.subheader('Russian Translation')
                translation = translate_text(summary, translator_tokenizer, translator_model)
                st.write(translation)

        except:
            st.error('Sorry, something went wrong')


if __name__ == "__main__":
    summarizer_tokenizer = AutoTokenizer.from_pretrained("/app/models/tokenizer")
    summarizer_model = AutoModelForSeq2SeqLM.from_pretrained("/app/models/summarizer")

    translator_tokenizer = AutoTokenizer.from_pretrained("/app/models/tokenizer")
    translator_model = AutoModelForSeq2SeqLM.from_pretrained("/app/models/translator")

    main()
