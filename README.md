# 🐔 Chicken Disease Classification System

A **Deep Learning–based Chicken Disease Classification System** built using a **modular, production-ready project structure**. This project classifies chicken fecal images into **Healthy** or **Coccidiosis** using a **ResNet50** CNN model. It also includes a **Flask web application** to test predictions locally.

The main goal of this project is to demonstrate **clean architecture, modular coding practices, and end-to-end ML pipeline design** rather than just model accuracy.

---

## 📌 Project Highlights

* Binary image classification (Healthy vs Coccidiosis)
* Kaggle dataset: **Chicken-fecal-image**
* Transfer Learning using **ResNet50**
* Fully modular pipeline (Data Ingestion → Training → Evaluation → Prediction)
* Config-driven workflow using `config.yaml` and `params.yaml`
* Flask app for local testing
* Single entry-point execution via `main.py`

---
## Project workflow
1. Update config.yaml
2. Update params.yaml
3. Update the entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline
7. Update the main.py
8. Update the app.py

## 📂 Dataset Details

**Source:**  [*Chicken-fecal-image dataset*](https://drive.google.com/file/d/1pV0DAdyjzsjk0HL7f8_5qiS_mVyjYk25/view)

**Structure:**

```
Chicken-fecal-image/
│
├── Healthy/
│   ├── img1.jpg
│   ├── img2.jpg
│   └── ...
│
└── Coccidiosis/
    ├── img1.jpg
    ├── img2.jpg
    └── ...
```

---

## 🗂️ Project Structure

```
cnnClassifier/
│
├── .github/workflows/
│
├── src/cnnClassifier/
│   ├── components/          # Core ML components
│   │   ├── data_ingestion.py
│   │   ├── prepare_base_model.py
│   │   ├── model_trainer.py
│   │   ├── evaluation.py
│   │
│   ├── pipeline/            # Pipeline orchestration
│   │   ├── stage_01_data_ingestion.py
│   │   ├── stage_02_prepare_base_model.py
│   │   ├── stage_03_model_trainer.py
│   │   ├── stage_04_evaluation.py
│   │
│   ├── config/              # Configuration management
│   │   └── configuration.py
│   │
│   ├── entity/              # Config entities (dataclasses)
│   │   └── config_entity.py
│   │
│   ├── utils/               # Utility functions
│   │   └── common.py
│   │
│   ├── constants/           # Constants
│   └── __init__.py
│
├── config/
│   └── config.yaml          # Paths & pipeline configs
│
├── params.yaml              # Model hyperparameters
│
├── research/
│   │   ├── 01_data_ingestion.ipynb
│   │   ├── 02_prepare_base_model.ipynb
│   │   ├── 03_model_trainer.ipynb
│   │   ├── 04_model_evaluation.ipynb

# Experiments & testing
│
├── templates/
│   └── index.html           # Flask UI
│
├── app.py                   # Flask app
├── main.py                  # Pipeline entry point
├── requirements.txt
├── setup.py
└── README.md
```

---

## ⚙️ Tech Stack

* Python 3.9+
* TensorFlow / Keras
* ResNet50 (Transfer Learning)
* Flask
* NumPy, Pandas
* OpenCV, PIL
* YAML, Logging

---

## 🚀 How to Run This Project Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/arosha27/End_To_End_Chicken_Disease_Classifier
cd End_To_End_Chicken_Disease_Classifier
```

---

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv

# Activate
venv\Scripts\activate      # Windows
source venv/bin/activate     # Linux / Mac
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Download the Dataset

1. Download and extract it
2. Place it in the directory specified in `config/config.yaml`

Example:

```yaml
data_ingestion:
  source_URL: Chicken-fecal-image
```

---

### 5️⃣ Update Configuration Files

#### `config/config.yaml`

* Dataset paths
* Artifacts directory
* Model output paths

#### `params.yaml`

* Image size
* Batch size
* Epochs
* Learning rate

---

### 6️⃣ Run the Complete Training Pipeline

```bash
python main.py
```

This will execute:

* Data ingestion
* Base model preparation (ResNet50)
* Model training
* Model evaluation
* Save trained model and metrics

---

## 🔁 Project Workflow (Step-by-Step)

### 🔹 Stage 1: Data Ingestion

* Reads dataset from source
* Creates train/validation structure
* Stores data inside `artifacts/`

### 🔹 Stage 2: Prepare Base Model

* Loads pretrained **ResNet50**
* Freezes base layers
* Adds custom classification head

### 🔹 Stage 3: Model Training

* Compiles model
* Applies data augmentation
* Trains using train & validation data
* Saves trained model

### 🔹 Stage 4: Model Evaluation

* Evaluates model on validation data
* Saves accuracy and loss metrics

### 🔹 Stage 5: Prediction Pipeline

* Loads trained model
* Accepts new image
* Outputs prediction (Healthy / Coccidiosis)

---

## 🌐 Running the Flask Web App

Once the model is trained:

```bash
python app.py
```

Then open your browser:

```
http://127.0.0.1:5000/
```

### Features:

* Upload chicken fecal image
* Get real-time prediction
* Simple UI for local testing

---

## 📊 Model Performance

* **Transfer Learning (ResNet50)**
* Achieved strong validation accuracy
* Designed for extendability (multi-class support possible)

---

## 🔧 Future Improvements

* Multi-disease classification
* Grad-CAM visualizations
* Dockerization
* CI/CD integration
* Cloud deployment (AWS / Azure)
* DVC for experiment tracking

---

## 🙌 Acknowledgements

* Kaggle for the dataset
* TensorFlow & Keras
* Open-source ML community

---

## 📬 Contact

For questions or collaboration:

**Arosha Bakhtawar**
Data Science | Machine Learning | Deep Learning
---

⭐ If you find this project helpful, don’t forget to star the repository!
