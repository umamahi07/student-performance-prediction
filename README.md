# 🎓 Student Performance Prediction Using Machine Learning

## 📌 Project Overview
This project is a **Flask-based Machine Learning web application** that predicts a student’s academic performance at an early stage based on internal assessment marks and previous academic results.

Early prediction helps institutions identify **at-risk students** and provide timely academic support.

---

## 🎯 Objectives
- Predict student performance as **Poor, Average, or Good**
- Use Machine Learning to analyze academic data
- Provide **personalized academic recommendations**
- Help faculty take preventive actions early

---

## 🧠 Machine Learning Approach
- Algorithm Used: **Support Vector Machine (SVM)**
- Feature Scaling: **StandardScaler**
- Label Encoding for categorical targets
- Model trained using historical student data

### Input Features:
- IAT 1 Marks
- IAT 2 Marks
- Model Exam Marks
- Previous Year Result (Poor / Average / Good / NIL)

### Output:
- Predicted Performance
- Recommendation message

---

## 🏗️ Project Structure

students_early_prediction/
│
├── app.py
├── requirements.txt
├── README.md
│
├── model/
│ ├── svm_model.pkl
│ ├── scaler.pkl
│ └── label_encoder.pkl
│
├── dataset/
│ └── raw_student_data_sem1.csv
│
├── templates/
│ └── index.html
│
├── static/
│ └── style.css

---

## ⚙️ Technologies Used
- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML & CSS

---

## 🚀 How to Run the Project Locally

### Step 1: Clone the repository

---

## ⚙️ Technologies Used
- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML & CSS

---

## 🚀 How to Run the Project Locally

### Step 1: Clone the repository
git clone https://github.com/umamahi07/student-performance-prediction.git

cd student-performance-prediction 

### Step 2: Install dependencies

pip install -r requirements.txt

### Step 3: Run the application
python app.py

### Step 4: Open in browser
http://127.0.0.1:5000


---

## 🌐 Deployment
The application can be deployed using **Render** by connecting this GitHub repository and running the Flask app with Gunicorn.

---

## 📊 Model Accuracy
Model accuracy is evaluated during training using test data and can be reported in the project documentation.

---

## 👩‍💻 Author
**Umamaheswari P**  
Computer Engineering  
Student Performance Prediction Project

---

## 📄 License
This project is developed for **academic purposes**.

