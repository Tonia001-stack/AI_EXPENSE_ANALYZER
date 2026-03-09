# AI_EXPENSE_ANALYZER
An AI-powered web application that predicts the category of an expense based on its description.

This project uses **Natural Language Processing (NLP)** and **Machine Learning** to classify expenses such as food, transport, shopping, and bills.

The application is built with **Python, Scikit-learn, and Streamlit**.

---

# 🚀 Features

* Classifies expense descriptions into categories
* Uses **TF-IDF text vectorization**
* Machine learning model built with **Multinomial Naive Bayes**
* Interactive web interface using **Streamlit**
* Displays prediction confidence level

Example:

Input:

```
Bought rice from market
```

Output:

```
Category: Food
Confidence: 92%
```

---

# 🧠 Machine Learning Model

The model pipeline includes:

1. **TF-IDF Vectorizer**

   * Converts text into numerical features
   * Uses **unigrams and bigrams**

2. **Multinomial Naive Bayes**

   * A probabilistic algorithm commonly used for text classification.

Pipeline structure:

```
TF-IDF Vectorizer → Multinomial Naive Bayes
```

---

# 🗂 Project Structure

```
expense_ai_app/
│
├── app.py                # Streamlit user interface
├── model.py              # Prediction function
├── train_model.py        # Model training script
├── expense_model.pkl     # Trained model
├── expenses_dataset.csv  # Training dataset
└── README.md             # Project documentation
```

---

# ⚙️ Installation

Clone the repository:

```
git clone https://github.com/yourusername/expense-ai-analyzer.git
```

Move into the project folder:

```
cd expense-ai-analyzer
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Start the Streamlit app:

```
streamlit run app.py
```

Then open the local URL shown in the terminal.

---

# 🌍 Deployment

This app can be deployed using:

* **Streamlit Community Cloud**
* **Render**
* **HuggingFace Spaces**

Deployment link:

```
(https://aiexpenseanalyzer-f5qvlabwhats4tzm9dqftr.streamlit.app)
```

---

# 📊 Model Accuracy

Current model accuracy:

**74%**

Accuracy improved by:

* Increasing dataset size
* Using **n-grams**
* Balancing category samples

---

# 📚 Technologies Used

* Python
* Scikit-learn
* Pandas
* Streamlit
* Joblib
* NumPy

---

# 🎯 Future Improvements

* Increase dataset size
* Add more expense categories
* Improve UI/UX
* Add expense history tracking
* Deploy mobile-friendly interface

---

# 👩‍💻 Author- TONIA

Built as part of a **Machine Learning learning project** focused on NLP and text classification.


