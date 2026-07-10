# 🚗 EV Adoption Likelihood Prediction
> An end-to-end Machine Learning application that predicts the likelihood of electric vehicle (EV) adoption using demographic, behavioral, socio-economic and transportation-related features.

---
## Overview
Electric Vehicle (EV) adoption is accelerating worldwide as governments and autombile manufacturers promote sustainable transportation. However, understanding **who is likely to adopt an EV** remains a complex challenge. This project leverages Machine Learning to predict an individual's likelihood of adopting an electric vehhicle (EV) based on demograhic information, travel behavior, charging accessibility, environmental awareness, and financial characteristics. The solution includes an interactive **streamlit application** that allow users to enter customer information and instantly receive and EV adoption prediction with probability score.

---

# Business Problem
Governments, automobile manufacturers, policymakers, and energy providers needs reliable methods to identify individual who are most likely to adopt electric vehicle. without predictive analytics, organizations often struggle to:

- Identify potential EV customer's
- Design targeted marketing campaign
- Improve charging infrastructure planning
- Evaluate factor influencing EV adoption
- Support sustainability initiatives

This project addresses these challenges using supervise machine learning.

---

# Objectives 
The primary onjectives are to:
- Predict EV adoption Likelihood
- Identify key factors that influence EV adoption
- Support decision-making for policy, marketing, and infrastructure development
- promote sustainable transportation through data driven insights

---

# 🔄 Project Workflow

```

Raw Dataset

      │

      ▼

Data Cleaning

      │

      ▼

Exploratory Data Analysis And Statistical Inference

      │

      ▼

Feature Engineering

      │

      ▼

Data Preprocessing

      │

      ▼
Model Selection
      │

      ▼

Model Training

      │

      ▼

RandomizedSearchCV

      │

      ▼

Model Evaluation

      │

      ▼

Model Deployment (Streamlit)

```

# ⚙️ Feature Engineering
Several domain-specific features were engineered to improve model performance.

Created Features include:

- Age Group
- Annual Income Bracket
- Commute Categories

These engineered variables capture meaningful behavioral patterns that improve prediction accuracy

---

# 🤖 Machine Learning Models

Several classification algorithms were evaluated.

Models considered include:

- Logistic Regression ✅ (Best Model)

- Random Forest

- XGBoost

- LightGBM 


Hyperparameter optimization was performed using RandomizedSearchCV only on logistic regression model.

---

# 🔍 Hyperparameter Tuning

RandomizedSearchCV was used to optimize model parameters.

Benefits:

- Improved generalization

- Reduced overfitting

- Better predictive performance

---

# 📊 Model Performance

| Metric | Score |
|---|---|
| Accuracy | **87.84%** |
| ROC-AUC | **96.63%** |

The Logistic Regression model achieved the best overall performance and was selected for deployment

---

## Web Application
<img width="158" height="311" alt="image" src="https://github.com/user-attachments/assets/f09fad2a-845f-4118-a5cb-90b580835215" />

Live Demo:
https://your-streamlit-link.streamlit.app

GitHub:

https://github.com/kolex24/EV-Adoption-Likelihood_Prediction

---
