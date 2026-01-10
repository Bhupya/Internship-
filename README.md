# 🚢 Titanic Dataset Analysis (Python Project)

## 📌 Project Overview
This project performs Exploratory Data Analysis (EDA) on the Titanic dataset to identify key factors that influenced passenger survival.  
The analysis includes data cleaning, summary statistics, and visualizations using Python libraries.

---

## 🛠 Tech Stack
- Python 3
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook / Google Colab

---

## 📂 Project Structure
Titanic-Data-Analysis/
│
├── titanic_analysis.ipynb   # Executable notebook
├── README.md               # Project documentation

---

## 📊 Dataset
- Name: Titanic Survival Dataset
- Source: Public online dataset (CSV loaded via URL)

---

## ⚙️ How to Run the Project

### ▶ Option 1: Google Colab (Recommended)
1. Open Google Colab
2. Upload the notebook `titanic_analysis.ipynb`
3. Click Runtime → Run all

No installation required.

---

### ▶ Option 2: Run Locally (Jupyter Notebook)

#### Step 1: Install Required Libraries
pip install pandas matplotlib seaborn notebook

#### Step 2: Launch Jupyter Notebook
jupyter notebook

#### Step 3: Open and Run
Open `titanic_analysis.ipynb` and run all cells.

---

## 🧹 Data Preprocessing
- Missing values in Age filled using median
- Missing values in Embarked filled using mode
- No duplicate record filtering applied
- Pandas 3.0 compatible code (no inplace usage)

---

## 📈 Visualizations Included
- Survival count plot
- Survival by gender
- Survival by passenger class
- Age distribution histogram
- Fare vs survival boxplot
- Correlation heatmap

---

## 🧠 Key Insights
- Female passengers had higher survival rates
- Higher-class passengers survived more
- Higher fare increased survival probability
- Younger passengers had better survival chances
- Overall survival rate was approximately 38%

---

## 🎓 Intended Use
- Academic assignment
- Data analysis practice
- Viva and presentation reference

---

## 📜 License
This project is for educational purposes only.
