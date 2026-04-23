# 📌 Spam Classification using ML → DL → Transformers

## 🚀 Overview

This project explores the evolution of machine learning models for classification by progressively improving architectures—from classical models like Logistic Regression to modern transformer-based models such as BERT.

The goal is not just to build a high-performing model, but to understand **why each model exists**, what limitations it has, and how newer architectures overcome them.

The project covers:

* Image classification using CNNs
* Text classification using TF-IDF, Embeddings, LSTM, Attention, and BERT

---

## 🧠 Motivation

Instead of directly applying advanced models like BERT, this project focuses on building intuition by:

* Identifying limitations of simpler models
* Understanding how each new architecture improves upon the previous one
* Connecting theory with practical performance improvements

---

## 🔄 Model Evolution

| Stage | Model               | Key Limitation                            |
| ----- | ------------------- | ----------------------------------------- |
| 1     | Logistic Regression | Cannot capture non-linear relationships   |
| 2     | Neural Network      | No spatial or sequential understanding    |
| 3     | TF-IDF              | No semantic meaning                       |
| 4     | Embeddings          | No sequence modeling                      |
| 5     | LSTM                | Weak long-range dependency handling       |
| 6     | Self-Attention      | Better contextual understanding           |
| 7     | BERT                | Pretrained deep contextual representation |

---

## 📊 Results

### 🔹 Text Classification (BERT)

* Accuracy: 99%
* Precision (Spam): 0.99
* Recall (Spam): 0.97

👉 High precision ensures minimal false positives
👉 Slightly lower recall indicates a few missed spam messages

---

### 🔹 Image Classification (CNN)

* Accuracy: ~99%
* Strong performance due to spatial feature learning via convolutional filters

---

## 🔍 Key Insights

* Feature representation is more important than model complexity
* TF-IDF fails to capture semantic relationships between words
* Embeddings enable generalization through semantic similarity
* LSTMs struggle with long-range dependencies due to sequential processing
* Attention allows direct interaction between all words
* BERT outperforms all models due to pretrained contextual embeddings

---

## 🛠️ Tech Stack

* Python
* Scikit-learn
* TensorFlow / Keras
* PyTorch
* HuggingFace Transformers

---

## 📁 Project Structure

```
image_classification/
    ├── notebooks/
    └── MNIST/

text_classification/
    ├── notebooks/
    └── data/
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/spam-classification-ml-to-bert.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run notebooks from:

* `text_classification/`
* `image_classification/`

---

## 🎯 Conclusion

This project demonstrates the progression from traditional machine learning models to modern deep learning architectures, emphasizing the importance of:

* representation learning
* contextual understanding
* and model design choices

It highlights why transformer-based models like BERT are state-of-the-art for NLP tasks.

---
