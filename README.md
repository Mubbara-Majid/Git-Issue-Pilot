````markdown
# 🤖 Git-Issue-Pilot
### Intelligent DevOps Automation: Bug Classification & Fix Suggestions

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![HuggingFace](https://img.shields.io/badge/Hugging%20Face-Transformers-yellow?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**Git-Issue-Pilot** is an end-to-end NLP pipeline designed to streamline software maintenance. It acts as an intelligent agent that automatically classifies GitHub issues (Bug, Feature, Question) using a fine-tuned **DistilBERT** model and generates context-aware responses or fix suggestions using **Google's FLAN-T5**.

---

## 🚀 Key Features

* **🔍 Smart Classification:** Distinguishes between critical Bugs 🐞, Feature Requests 🚀, and General Questions ❓ with **81.3% accuracy**.
* **✍️ Generative AI Agent:** Uses Large Language Models (LLMs) to draft polite auto-responses or suggest code fixes based on the issue description.
* **⚡ Real-Time Interface:** A lightweight, user-friendly web app built with Streamlit for instant model inference.
* **📊 Data-Driven:** Trained on a robust dataset of 150,000+ real GitHub issues.

---

## 🛠️ Tech Stack

* **Language:** Python
* **Deep Learning Framework:** PyTorch, Hugging Face Transformers
* **NLP Models:** * *Classifier:* DistilBERT (`distilbert-base-uncased`) - Fine-tuned
    * *Generator:* FLAN-T5 (`google/flan-t5-base`)
* **Web Framework:** Streamlit
* **Data Processing:** Pandas, NumPy, Scikit-Learn

---

## 📂 Project Structure

```bash
Git-Issue-Pilot/
├── app.py                                # Main Streamlit Application (Frontend)
├── SP23_BAI_027_NLP_SemesterProject.ipynb # Experimentation Notebook (Training & Eval)
├── requirements.txt                      # Project Dependencies
├── README.md                             # Documentation
└── .gitignore                            # Ignored files (models, cache)
````

-----

## 📊 Model Performance & Experimentation

To select the best architecture, I conducted a comparative analysis between Traditional Machine Learning models (TF-IDF) and Modern Transformers.

| Model | Feature Extraction | Accuracy | F1 Score | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Logistic Regression** | TF-IDF (Bag of Words) | 75.3% | 0.62 | Baseline |
| **Random Forest** | TF-IDF | 74.2% | 0.55 | Too Slow |
| **Naive Bayes** | TF-IDF | 71.6% | 0.51 | Underfitting |
| **DistilBERT (Fine-Tuned)** | **Contextual Embeddings** | **81.3%** 🏆 | **0.73** | **Selected** |

> **Insight:** The Transformer model (DistilBERT) outperformed the best traditional model (Logistic Regression) by **6%**, proving that contextual understanding is superior to keyword counting for technical text.

-----

## 💻 Installation & Usage

### 1\. Clone the Repository

```bash
git clone [https://github.com/Mubbara-Majid/Git-Issue-Pilot.git](https://github.com/Mubbara-Majid/Git-Issue-Pilot.git)
cd Git-Issue-Pilot
```

### 2\. Install Dependencies

It is recommended to use a virtual environment.

```bash
pip install -r requirements.txt
```

### 3\. Run the Application

```bash
streamlit run app.py
```

*The app will launch in your browser at `http://localhost:8501`*

-----

## 📸 Demo

> **Input:** *"I get a ZeroDivisionError when I try to calculate the average score with an empty list."*

**Output:**

  * **Category:** Bug 🐞
  * **AI Suggestion:** *"Explain this python error simply: You cannot divide by zero. Check if the list is empty before dividing."*

## *(Add a screenshot of your app here if you have one)*

## 🔮 Future Improvements

  * **Dockerization:** Containerize the app for easier deployment.
  * **RAG Implementation:** Connect the agent to a specific codebase to give more accurate code fix suggestions.
  * **CI/CD Pipeline:** Automate testing for model updates.

-----

## 👨‍💻 Author

**Mubbara Majid** BS Artificial Intelligence | COMSATS University Islamabad  
*Aspiring Software AI Engineer*

[LinkedIn](https://www.google.com/search?q=https://www.linkedin.com/in/mubbara-majid/) • [GitHub](https://www.google.com/search?q=https://github.com/Mubbara-Majid)

```
```