# Cyberbullying Detection App (English) with Streamlit GUI

## Overview

A Cyberbullying Detection App designed to identify instances of cyberbullying in English text. The app incorporates a diverse set of machine learning and deep learning algorithms, including BERT, Random Forest (RF), Support Vector Machine (SVM), Decision Tree (DT), Multi-Layer Perceptron (MLP), and others.

## Key Features

- **Algorithmic Diversity:** A blend of traditional machine learning algorithms and cutting-edge deep learning models for robust cyberbullying detection.
- **Preprocessing:** Stringent text preprocessing involving tokenization, stemming/lemmatization, and removal of stop words, ensuring high-quality data for model training and assessment.
- **Feature Representation:** Varied feature representations such as bag-of-words, TF-IDF, and embeddings cater to different algorithmic requirements, capturing semantic connections within the text.
- **Model Performance:** A detailed classification report for the English dataset showcasing accuracy, precision, recall, and F1-score metrics for each algorithm.

## Dataset

The English dataset for this cyberbullying detection app employs multi-class classification, categorizing texts into four bullying categories (gender-based, age-related, religious, and ethnic) along with a "Not Bullying" class.

### Bullying Classifications:

1. **Gender-based Bullying:** Degrading words related to gender.
2. **Age-related Bullying:** Occurs in adolescent environments.
3. **Religious Bullying:** Discrimination or derision based on beliefs.
4. **Ethnic-based Bullying:** Prejudice or racial insults.

## Classification Report

| Algorithm | Accuracy | Precision | Recall | F1-Score |
|-----------|----------|-----------|--------|----------|
| BERT      | 0.95     | 0.95      | 0.95   | 0.95     |
| RF        | 0.93     | 0.93      | 0.93   | 0.93     |
| SVM       | 0.92     | 0.92      | 0.92   | 0.92     |
| DT        | 0.93     | 0.92      | 0.93   | 0.92     |
| MLP       | 0.90     | 0.90      | 0.90   | 0.90     |
| LR        | 0.92     | 0.92      | 0.92   | 0.92     |



### Live Site

You can also access the live version of the app on [Click Here](https://huggingface.co/spaces/Amiruzzaman/cbEnglish).


### Streamlit App in Action (Results)
## Cyberbullying
![image](https://github.com/amiruzzaman1/Cyberbullying-Detection-English/assets/68743925/befc7fda-0d68-4308-b5f5-0724b00d9722)


## Not Cyberbullying
![image](https://github.com/amiruzzaman1/Cyberbullying-Detection-English/assets/68743925/8961b1a3-c68c-4edd-8075-d907c19180ef)



### Sample Texts

1. "It's always the filthy bitch that creates a problem between us."
2. "Do you believe it is appropriate to refer to a Muslim as a terrorist?"
3. "I hope you're doing well and having a great day. Let's catch up soon! 😊"
4. "The team's score is disgraceful."
