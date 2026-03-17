# 🩺 AI Health Symptom Checker

## 📌 Project Overview

The **AI Health Symptom Checker** is a Machine Learning project that predicts possible diseases based on symptoms entered by the user.

The user selects symptoms such as **fever, cough, headache, fatigue**, and the trained machine learning model predicts the most likely disease.
---

## 🚀 Technologies Used

* Python
* Pandas
* Scikit-learn
* Decision tree classifier
---
## ⚙️ How the Project Works

1. The dataset containing symptoms and diseases is loaded.
2. Symptoms are used as input features.
3. A **Decision Tree Classifier** model is trained on the dataset.
4. The user enters symptoms.
5. The model predicts the possible disease.

---
## 📊 Example Dataset Format

fever,cough,headache,fatigue,disease
1,1,1,1,Flu
1,1,0,1,Cold
0,1,0,0,Allergy
1,0,1,1,Malaria

Here:

* **1 = Symptom Present**
* **0 = Symptom Not Present**
---

## 💻 Example Output

Available Symptoms

fever
cough
headache
fatigue

Enter symptoms separated by comma:

fever,cough,fatigue

Possible Disease: Flu
Confidence level: 80%
---

## 🎯 Learning Outcomes

Through this project, I learned:

* Data preprocessing using Pandas
* Training machine learning models using Scikit-learn
* Handling user input for prediction
* Building a basic health diagnosis system using AI

---

## 👩‍💻 Author

Prachi Jain
Engineering Student | Aspiring AI/ML Engineer
