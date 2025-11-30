import streamlit as st
import torch
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification, AutoTokenizer, AutoModelForSeq2SeqLM

st.set_page_config(page_title="Git-Issue-Pilot", page_icon="🤖", layout="centered")

@st.cache_resource
def load_models():
    bert_path = "./saved_bert_model" 
    bert_tokenizer = DistilBertTokenizerFast.from_pretrained(bert_path)
    bert_model = DistilBertForSequenceClassification.from_pretrained(bert_path)

    t5_tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
    t5_model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
    
    return bert_tokenizer, bert_model, t5_tokenizer, t5_model

st.title("🤖 Git-Issue-Pilot")
st.markdown("Automated classification and response generation for software issues.")

with st.spinner("Loading AI Models..."):
    bert_tokenizer, bert_model, t5_tokenizer, t5_model = load_models()

# --- User Input ---
issue_text = st.text_area("Paste the GitHub Issue / Bug Report here:", height=150)

if st.button("Analyze Issue"):
    if not issue_text:
        st.warning("Please enter some text.")
    else:
        inputs = bert_tokenizer(issue_text, return_tensors="pt", truncation=True, padding=True, max_length=128)
        
        with torch.no_grad():
            logits = bert_model(**inputs).logits
            
        predicted_class_id = logits.argmax().item()
        labels = {0: 'Bug 🐞', 1: 'Feature Request 🚀', 2: 'Question ❓'}
        prediction = labels[predicted_class_id]
        
        st.subheader("1. Classification Result")
        if predicted_class_id == 0:
            st.error(f"Category: {prediction}")
        elif predicted_class_id == 1:
            st.success(f"Category: {prediction}")
        else:
            st.info(f"Category: {prediction}")

        if predicted_class_id == 0: 
            # "Explain error" works better than "Suggest fix" for T5-Base
            prompt = f"Explain this python error simply: {issue_text}"
        elif predicted_class_id == 1: # Feature
            prompt = f"Write a polite sentence thanking the user for this feature request: {issue_text}"
        else: 
            prompt = f"Answer this question briefly: {issue_text}"

        input_ids = t5_tokenizer(prompt, return_tensors="pt").input_ids
        outputs = t5_model.generate(input_ids, max_length=60, num_beams=4, early_stopping=True)
        response = t5_tokenizer.decode(outputs[0], skip_special_tokens=True)

        st.subheader("2. AI Suggested Reply")
        st.code(response, language='markdown')