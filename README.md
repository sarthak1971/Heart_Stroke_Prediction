# 🧠 Heart Stroke Prediction — Machine Learning Project

A binary classification project to predict the likelihood of a stroke in a patient based on health and lifestyle features. The project covers end-to-end ML pipeline: data exploration, preprocessing, class imbalance handling, model training, and evaluation.

---

## 📁 Project Structure

```
Heart-Stroke-Prediction/
├── Heart_Stroke.ipynb                   # Main notebook
├── healthcare-dataset-stroke-data.csv   # Dataset
├── DataExplore.py                       # Custom EDA utility class
├── preprocessor.py                      # Custom preprocessing class
├── outlier.py                           # Custom outlier removal class
└── README.md
```

---

## 📊 Dataset

- **Source:** [Stroke Risk Dataset — Kaggle](https://www.kaggle.com/datasets/ranaghulamnabi/stroke-risk-dataset)
- **Rows:** 5,110 patients
- **Features:** 11 input features + 1 target
- **Target:** `stroke` (1 = stroke occurred, 0 = no stroke)
- **Class Distribution:** Highly imbalanced — 4,861 non-stroke vs 249 stroke cases

### Features

| Feature | Type | Description |
|---|---|---|
| `id` | int | Unique patient identifier |
| `gender` | categorical | Male / Female / Other |
| `age` | int | Age of the patient |
| `hypertension` | binary | 1 if patient has hypertension |
| `heart_disease` | binary | 1 if patient has heart disease |
| `ever_married` | categorical | Yes / No |
| `work_type` | categorical | Type of employment |
| `Residence_type` | categorical | Urban / Rural |
| `avg_glucose_level` | float | Average blood glucose level |
| `bmi` | float | Body mass index |
| `smoking_status` | categorical | Smoking history |
| `stroke` | binary | **Target** — 1 if stroke occurred |

---

## ⚙️ ML Pipeline

### 1. Exploratory Data Analysis
- Custom `DataExplore` class used for data info and missing value analysis
- Distribution plots (e.g., BMI histogram via Seaborn)

### 2. Preprocessing
- **Missing value imputation** — numerical imputation via custom `Preprocessing` class
- **Outlier removal** — IQR-based method via custom `OutlierRemoval` class
- **Label Encoding** — categorical columns encoded using `sklearn.LabelEncoder`

### 3. Handling Class Imbalance
- Applied **Random Over Sampling** using `imblearn.over_sampling.RandomOverSampler` to balance stroke vs non-stroke classes

### 4. Model Training
- **Algorithm:** Logistic Regression (`sklearn.linear_model.LogisticRegression`)
- **Train/Test Split:** 80% / 20% (`random_state=42`)
- Two models trained:
  - `lsr` — trained on original (imbalanced) data
  - `lsr2` — trained on oversampled (balanced) data

### 5. Evaluation
- Metrics: Accuracy Score, Confusion Matrix, Classification Report

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install numpy pandas matplotlib seaborn scikit-learn imbalanced-learn kagglehub
```

### Run the Notebook

```bash
git clone https://github.com/your-username/heart-stroke-prediction.git
cd heart-stroke-prediction
jupyter notebook Heart_Stroke.ipynb
```

> **Note:** Update the dataset path in the notebook to point to your local copy of `healthcare-dataset-stroke-data.csv`.

---

## 📦 Dependencies

| Library | Purpose |
|---|---|
| `numpy` | Numerical operations |
| `pandas` | Data manipulation |
| `matplotlib` / `seaborn` | Visualization |
| `scikit-learn` | ML models and preprocessing |
| `imbalanced-learn` | Oversampling (SMOTE / RandomOverSampler) |
| `kagglehub` | Dataset download from Kaggle |

---

## 📌 Key Observations

- The dataset is **highly imbalanced** (~4.9% positive stroke cases), making raw accuracy a misleading metric.
- Applying **RandomOverSampler** before training significantly improves the model's ability to detect true stroke cases.
- Logistic Regression serves as a solid baseline; further improvements can be explored with ensemble methods (Random Forest, XGBoost).

---

## 🔮 Future Improvements

- [ ] Try advanced models: Random Forest, XGBoost, LightGBM
- [ ] Use SMOTE instead of simple random oversampling
- [ ] Add feature importance / SHAP analysis
- [ ] Hyperparameter tuning with GridSearchCV
- [ ] Deploy as a web app using Streamlit or Flask

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙋 Author

**Sarthak Somani** — feel free to connect or raise issues!
