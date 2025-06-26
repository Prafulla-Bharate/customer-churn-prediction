
# 📊 Customer Churn Prediction Web App

This project is a **Streamlit-based web application** that predicts whether a customer is likely to churn (leave a service) based on their demographic and service usage information.

---

## 🚀 Features
- Interactive web interface for inputting customer data
- Uses a pre-trained machine learning model to predict churn
- Highlights risk of churn clearly using color-coded results
- Handles categorical and numerical inputs with proper preprocessing

---

## 🧠 Model Information
- The model was trained using historical customer churn data
- Common ML algorithms like Logistic Regression or Random Forest were used (you can update this based on your actual model)
- Input features are encoded using one-hot encoding to match training format

---

## 🛠 Tech Stack
- Python 🐍
- Streamlit 📺
- Pandas & NumPy
- Scikit-learn or XGBoost (depending on the model)
- Pickle for model loading

---

## 📂 File Structure

├── app.py # Streamlit app file
├── churn_updated.ipynb # Jupyter notebook for model training and exploration
├── churn_prediction_model.pkl # Trained machine learning model
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🧪 How to Run Locally

### 1. Clone the Repository:
```bash
git clone https://github.com/your-username/churn-prediction-app.git
cd churn-prediction-app
2. Install Dependencies:
bash
Copy
Edit
pip install -r requirements.txt
3. Start the App:
bash
Copy
Edit
streamlit run app.py
📌 Sample Input Fields
Gender

Senior Citizen

Tenure

Phone/Internet/Streaming Services

Contract Type

Payment Method

Monthly & Total Charges

🔮 Prediction Output
✅ "Customer is NOT likely to Churn!"

⚠️ "Customer is likely to Churn!"
