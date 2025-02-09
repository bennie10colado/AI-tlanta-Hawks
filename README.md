# 🏀 AI-tlanta Hawks

A simple Data Science project for analyzing the performance of the Atlanta Hawks in the NBA.

## 📌 Objective
This project focuses on collecting, processing, and visualizing NBA statistics to analyze the **Atlanta Hawks** team.

## 🏗️ Project Structure

```
📂 AI-tlanta-Hawks/
│── 📂 data/                 # Stores generated CSV files
│── 📂 scripts/              # Main scripts
│   ├── fetch_nba_data.py   # Fetches NBA data from the API
│   ├── analyze_data.py     # Performs data analysis
│   ├── visualize.py        # Generates graphs
│── 📜 README.md            # Project documentation
│── 📜 requirements.txt     # Dependencies
│── 📜 run.py               # Main script to run everything
```

## 🛠️ Technologies Used
- **Python** (`requests`, `pandas`, `matplotlib`)
- **NBA API** for data collection

## 🚀 How to Run the Project
### 1️⃣ **Clone the repository**
```bash
git clone https://github.com/your-username/AI-tlanta-Hawks.git
cd AI-tlanta-Hawks
```

### 2️⃣ **Create a virtual environment and install dependencies**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

### 3️⃣ **Run the project**
```bash
python run.py
```

This will:
✅ **Fetch NBA data from the API**  
✅ **Analyze the data**  
✅ **Generate visualizations**  

### 4️⃣ **Run individual scripts manually**
```bash
python scripts/fetch_nba_data.py   # Collect NBA data
python scripts/analyze_data.py     # Run basic statistics
python scripts/visualize.py        # Generate charts
```

## 📊 Example Graph
This project generates simple graphs, such as the **win/loss performance of the Atlanta Hawks**.

![Example Graph](https://via.placeholder.com/600x400?text=Graph+Example)

## 🏀 Future Improvements
- Add more advanced statistics  
- Include historical analysis  
- Improve data visualizations  

---
### 🎯 **Final Notes**
This project is a **lightweight, easy-to-run** Python-based NBA analytics tool.  
Enjoy analyzing the **Atlanta Hawks' performance!** 🚀🔥🏀
