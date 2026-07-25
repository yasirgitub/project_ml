# 🧠 Teen Mental Health Prediction & Web App

An end-to-end machine learning project designed to analyze teen lifestyle factors, digital habits, and psychological indicators to predict mental health risks. The project includes data exploratory analysis, model training, and an interactive web application deployed live.

---

## 🚀 Live Demo & Access

* **Try the web app:** [🌐](https://project-ml-2-4z3n.onrender.com)

---

## 📊 Project Workflow & Architecture

The project follows a standard data science and MLOps lifecycle:

1. **Exploratory Data Analysis & Preprocessing (`model_training.ipynb`):**
   * Loaded and cleaned the dataset (`Teen_Mental_Health_Dataset.csv`).
   * Handled categorical variables using data encoding techniques.
   * Examined distributions of numerical factors such as daily social media hours, sleep hours, stress levels, and academic performance.
2. **Model Training & Evaluation:**
   * Trained multiple classification models (including Logistic Regression, Random Forest, Gradient Boosting, AdaBoost, and XGBoost).
   * Evaluated model performance using metrics like Accuracy, Precision, Recall, F1-Score, and ROC-AUC.
3. **Model Serialization:**
   * Exported and saved the best-performing trained model as `depression_model.pkl` using joblib/pickle for fast live inference.
4. **Web Application & Deployment (`app.py`):**
   * Built an interactive user interface using **Streamlit** (learned dynamically via documentation during development) to accept user inputs and output real-time predictions from the serialized model.
   * Deployed the web application to **Render** for public accessibility.

---

## 🧠 Technologies Used

* **Language:** Python
* **Data Processing & ML Libraries:** `pandas`, `numpy`, `scikit-learn`, `xgboost`, `seaborn`, `matplotlib`, `joblib`
* **Frontend & UI Framework:** Streamlit
* **Deployment Platform:** Render
* **Environment:** Jupyter Notebook

---

## 📁 Repository Structure

| File | Description |
| :--- | :--- |
| `app.py` | Main Streamlit application script powering the interactive web UI. |
| `depression_model.pkl` | Pre-trained and serialized machine learning model used for real-time predictions. |
| `model_training.ipynb` | Jupyter Notebook containing data analysis, preprocessing, and model training pipelines. |
| `Teen_Mental_Health_Dataset.csv` | Dataset containing lifestyle and mental health metrics. |
| `requirement.txt` | Text file listing all Python package dependencies required to run the app. |
| `.gitignore` | Specifies intentionally untracked files to ignore. |

---

## 🛠️ Getting Started & Local Installation

If you want to run this project locally on your machine, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yasirgitub/project_ml.git
   cd project_ml
   ```

2. **Install Dependencies:**
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirement.txt
   ```

3. **Run the Streamlit App:**
   ```bash
   streamlit run app.py
   ```
