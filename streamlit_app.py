import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('punkt_tab')
nltk.download('stopwords')

ps = PorterStemmer()

def transform_text(text):
    text = nltk.word_tokenize(text.lower())

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words("english") and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

with open('vectorizer.pkl','rb') as file:
    tfidf = pickle.load(file)


# tfidf = pickle.load(open('vectorizer.pkl','rb'))
# model = pickle.load(open('model.pkl','rb'))

st.title('🎈 Email/SMS Spam Classifier')

input_sms = st.text_area("Enter the message here...")

# Pre process
transformed_sms = transform_text(input_sms)

# vectorize
vector_input = tfidf.transform([transformed_sms])

# predict
result = model.predict(vector_input)[0]

# display
if result == 1:
    st.header("Spam")
else:
    st.header("Not Spam")

