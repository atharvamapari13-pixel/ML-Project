## End to End Machine learning project
# 📚 Student Exam Performance Predictor

A Machine Learning web application that predicts a student's **Mathematics Score** based on demographic information and academic performance indicators such as reading and writing scores.

---

## 🚀 Project Overview

The Student Exam Performance Predictor uses Machine Learning algorithms to predict the **Math Score** of a student using the following features:

* Gender
* Race/Ethnicity
* Parental Level of Education
* Lunch Type
* Test Preparation Course
* Reading Score
* Writing Score

The project follows a complete **MLOps pipeline**, including:

* Data Ingestion
* Data Transformation
* Model Training
* Model Evaluation
* Model Serialization
* Flask Deployment

---

## 📂 Project Structure

```text
ML Project/
│
├── artifacts/
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   │
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── templates/
│   ├── index.html
│   └── home.html
│
├── app.py
├── requirements.txt
├── setup.py
└── README.md
```

---

## 🛠️ Technologies Used

### Programming Language

* Python 3.x

### Libraries

* NumPy
* Pandas
* Scikit-Learn
* Flask
* Pickle
* Joblib

### Machine Learning Algorithms

* Linear Regression
* Ridge Regression
* Lasso Regression
* Decision Tree Regressor
* Random Forest Regressor
* K-Nearest Neighbors Regressor

---

## 📊 Dataset Features

| Feature                     | Type            |
| --------------------------- | --------------- |
| gender                      | Categorical     |
| race_ethnicity              | Categorical     |
| parental_level_of_education | Categorical     |
| lunch                       | Categorical     |
| test_preparation_course     | Categorical     |
| reading_score               | Numerical       |
| writing_score               | Numerical       |
| math_score                  | Target Variable |

---

## ⚙️ Machine Learning Pipeline

```text
Dataset
   ↓
Data Ingestion
   ↓
Train-Test Split
   ↓
Data Transformation
   ↓
Feature Engineering
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Serialization
   ↓
Flask Deployment
```

---

## 🧠 Data Preprocessing

### Numerical Features

* Reading Score
* Writing Score

Techniques Used:

* Median Imputation
* Standard Scaling

### Categorical Features

* Gender
* Race/Ethnicity
* Parental Education
* Lunch
* Test Preparation Course

Techniques Used:

* Most Frequent Imputation
* One-Hot Encoding
* Feature Scaling

---

## 📈 Evaluation Metric

The models are evaluated using:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)

---

## 🌐 Flask Application

### Home Route

```python
@app.route('/')
```

### Prediction Route

```python
@app.route('/predictdata', methods=['GET', 'POST'])
```

---

## ▶️ Installation

### Clone Repository

```bash
git clone <your-github-repository-link>
cd ML-Project
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Train Model

```bash
python src/pipeline/train_pipeline.py
```

---

## ▶️ Run Flask Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000/
```

---

## 📸 Application Features

✅ Predict Student Math Score

✅ Attractive Responsive Frontend

✅ Complete Machine Learning Pipeline

✅ Model Serialization using Pickle

✅ End-to-End Flask Deployment

---

## 🔮 Future Improvements

* Docker Containerization
* CI/CD Pipeline using GitHub Actions
* Cloud Deployment (AWS/Azure/GCP)
* Model Monitoring and Logging
* User Authentication System
* Performance Analytics Dashboard

---

## 👨‍💻 Author

**Atharva Mapari**

* MCA Student, DES Pune University
* Aspiring AI Engineer and Data Scientist
* Interested in Machine Learning, MLOps, and Artificial Intelligence

---

## ⭐ If you found this project useful, please consider giving it a Star on GitHub!
