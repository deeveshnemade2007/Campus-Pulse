# ⚡ CampusPulse — Smart Campus Electricity Usage Analyzer

CampusPulse is a Python mini project that analyzes electricity consumption across different campus buildings. It provides an interactive dashboard to visualize usage patterns, compare buildings, identify unusually high electricity readings, and estimate potential energy savings.

The project uses simulated data to demonstrate how data analytics can help monitor campus electricity usage and encourage energy conservation.

## 🎯 Problem Statement

Electricity consumption can vary across campus buildings depending on their activities and equipment. Without a simple way to analyze usage patterns, unusually high consumption may go unnoticed.

CampusPulse provides a simple, interactive solution for analyzing electricity usage, comparing buildings, and identifying readings that exceed a selected threshold.

## ✨ Features

- **Electricity Usage Dashboard:** Displays total, average, highest, and lowest electricity readings.
- **Daily Consumption Analysis:** Visualizes electricity usage across 30 simulated days.
- **Building-wise Comparison:** Compares average electricity consumption across different buildings.
- **High Usage Alerts:** Identifies readings that exceed a user-defined electricity threshold.
- **Potential Savings Calculator:** Estimates possible electricity savings based on a selected reduction percentage.
- **Building Filter:** Allows users to analyze an individual building or all buildings.
- **Dataset Viewer:** Displays the generated dataset directly in the dashboard.
- **Automatic Data Generation:** Generates a sample dataset using NumPy and Pandas.

## 🏢 Buildings Included

- Computer Lab
- Library
- Classroom
- Office
- Workshop

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Streamlit

## 📂 Project Structure

```text
CampusPulse/
├── app.py
├── generate_data.py
├── requirements.txt
├── README.md
└── data/
    └── campus_data.csv
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/CampusPulse.git
cd CampusPulse
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Generate the dataset

```bash
python generate_data.py
```

This creates the `data/campus_data.csv` file containing 150 simulated records for five buildings over 30 days.

### 6. Launch the dashboard

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## 📊 How It Works

1. NumPy generates reproducible sample electricity readings.
2. Pandas organizes the readings into a tabular dataset.
3. The dashboard calculates electricity consumption statistics.
4. Matplotlib creates daily usage and building comparison charts.
5. Streamlit provides interactive filters, alerts, and a savings calculator.

## 🌱 Potential Impact

CampusPulse demonstrates how basic data analytics can support:

- Awareness of electricity consumption patterns.
- Identification of unusually high readings for further investigation.
- Comparison of energy usage across campus buildings.
- Estimation of potential electricity savings.

## ⚠️ Data Disclaimer

**All readings are simulated and are not actual measurements from any college.** The alert threshold is user-defined, and flagged readings indicate values that exceed that threshold—not confirmed faults or electricity wastage.

Potential savings are estimates based on a selected percentage reduction, not measured savings.

## 🚀 Future Enhancements

- Machine-learning-based electricity demand prediction.
- Automatic anomaly detection using historical usage patterns.
- Upload and analyze real electricity meter data.
- Electricity cost estimation based on configurable tariffs.
- Downloadable analytics reports.
- Integration with real-time energy meters.

## 🎓 Project Information

**Project Name:** CampusPulse  
**Project Type:** Python Mini Project  
**Domain:** Data Analytics and Energy Monitoring

CampusPulse demonstrates the use of Python programming, data processing, statistical analysis, data visualization, and interactive dashboards in a practical campus-related application.

---

*Built as a learning project to explore Python and data analytics.*