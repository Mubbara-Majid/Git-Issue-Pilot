# 🤖 Git-Issue-Pilot

**Smart Triage AI** is an intelligent DevOps tool that automates GitHub issue management. It uses **DistilBERT** to classify issues (Bug, Feature, Question) and **FLAN-T5** to generate automated, context-aware responses.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Library](https://img.shields.io/badge/Library-HuggingFace-yellow)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red)

## 🚀 Features
- **Automated Classification:** Uses a fine-tuned DistilBERT model to categorize issues with >81% accuracy.
- **Smart Responses:** Leverages Google's FLAN-T5 LLM to suggest bug fixes or draft polite replies.
- **Real-time UI:** Built with Streamlit for instant feedback.

## 🛠️ Tech Stack
- **NLP Models:** DistilBERT (Fine-tuned), FLAN-T5 (Base)
- **Training:** PyTorch, Hugging Face Transformers
- **Deployment:** Streamlit
- **Dataset:** GitHub Bugs Prediction (150k samples)

## 📦 Installation

1. Clone the repo:
   ```bash
   git clone [https://github.com/Mubbara-Majid/Git-Issue-Pilot.git]
   cd Git-Issue-Pilot