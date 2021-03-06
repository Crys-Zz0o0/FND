import pickle
import streamlit as st
from vncorenlp import VnCoreNLP
from preprocessing import text_preprocessing

def main():
    annotator = VnCoreNLP('VnCoreNLP-1.1.1.jar', annotators="wseg,pos,ner,parse", max_heap_size='-Xmx2g')
    st.set_page_config(
        page_title="Fake news detector",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.title("Fake News Detector")

    model_dict = {
            "Passive Aggressive Classifier": "models/pac.pkl",
            "Logistic Regression": "models/lr.pkl", 
            }
    pac_path = 'PAC_pkl'
    lrc_path = 'LRC_pkl'

    with open(pac_path, "rb") as f:
        pac_model = pickle.load(f)

    with open(lrc_path, "rb") as f:
        lrc_model = pickle.load(f)
        
    with open("Vectorizer_pkl", "rb") as f:
        vectorizer = pickle.load(f)

    with st.columns([6, 4]):
        model_name = st.selectbox("Choose your model", index=0, options=['Passive Aggressive Classifier', 'Logistic Regression'])
        news = st.text_area("Your news here:")
        entered_items = st.empty()

    button = st.button("Predict")

    st.markdown(
        "<hr />",
        unsafe_allow_html=True
    )

    if button:
        with st.spinner("Predicting..."):
            if model_name == 'Passive Aggressive Classifier':
                model = pac_model
            else:
                model = lrc_model
            preprocessed_news = text_preprocessing(news)
            news_vectorized = vectorizer.transform(preprocessed_news)     
            prediction = model.predict(news_vectorized)
            if prediction == 1:
                st.markdown("This is real news")
            else:
                st.markdown("This is fake news")


if __name__ == "__main__":
    main()