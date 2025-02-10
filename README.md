# 🏀 AI-tlanta Hawks

A Data Science and Machine Learning project for analyzing the performance of the **Atlanta Hawks** in the NBA.

## 📌 Objective
This project collects, processes, and visualizes NBA statistics, implementing **Machine Learning models** for performance predictions.

## 🏗️ Project Structure

```
📂 AI-tlanta-Hawks/
│── 📂 data/                 # Stores datasets and generated CSV files
│── 📂 scripts/              # Main scripts
│   ├── data_engineering/    # Data collection and preprocessing
│   ├── analysis/models/     # Machine learning and statistical models
│   ├── visualization/       # Graph generation
│   ├── dashboard/           # Streamlit dashboard scripts
│── 📂 logs/                 # Stores error logs
│── 📜 README.md             # Project documentation
│── 📜 requirements.txt      # Dependencies
│── 📜 main.py               # Runs Project Part 1 (Team Analysis)
│── 📜 main2.py              # Runs Project Part 2 (Player Analysis)
│── 📜 main3.py              # Runs Project Part 3 (Machine Learning)
```

## 🛠️ Technologies Used
- **Python 3.10**
- **NumPy, Pandas** (Data Processing)
- **Matplotlib, Seaborn** (Visualization)
- **Scikit-learn** (Machine Learning)
- **PyGAM** (Generalized Additive Models)
- **Streamlit** (Dashboard)

---

## 🚀 How to Run the Project
### 🏗 **1️⃣ Install WSL (Windows Only)**
If using **Windows**, enable **Windows Subsystem for Linux (WSL)** to ensure compatibility:
```sh
wsl --install
```
Then, open **WSL** and follow the next steps.

### 📥 **2️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/AI-tlanta-Hawks.git
cd AI-tlanta-Hawks
```

### 🛠 **3️⃣ Create a Virtual Environment**
```sh
python3.10 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 📦 **4️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

---

## 🎯 **How to Run Each Part of the Project**
### ✅ **Project Part 1 - Team Analysis**
```sh
python main.py
```
✔ **Streamlit Dashboard for Team Analysis**:  
```sh
streamlit run scripts/visualization/teams/team_dashboard.py
```

### ✅ **Project Part 2 - Player Analysis**
```sh
python main2.py
```
✔ **Streamlit Dashboard for Player Analysis**:  
```sh
streamlit run scripts/visualization/players/player_dashboard.py
```

### ✅ **Project Part 3 - Machine Learning & Predictions**
```sh
python main3.py
```
✔ **Streamlit Dashboard with ML Results**:  
```sh
streamlit run scripts/dashboard/app.py
```

---

## 📊 **Example Graphs**
### 📈 **Gumbel Analysis - Extreme Events**

### 📊 **Regression Model Predictions**

### 🤖 **GAMLSS Next-Game Predictions**

---

## 🏀 **Possible Future Improvements**
- Add **real-time data updates** using an API  
- Improve **ML model accuracy** by refining features  
- Expand **dashboard** to include interactive filtering  

---

### 🎯 **Final Notes**
This project is a **complete data-driven analysis** of the **Atlanta Hawks**.  
It combines **statistics, machine learning, and interactive visualizations**! 🚀🔥🏀  
