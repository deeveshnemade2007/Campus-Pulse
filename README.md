# ⚡ CampusPulse — Smart Campus Electricity Usage Analyzer

CampusPulse is a Python-based mini project that analyzes electricity consumption across different campus buildings. It helps identify high electricity usage, compare building-wise consumption, and estimate potential energy and cost savings.

The project runs directly in the **VS Code terminal** and does not require a web application or graphical dashboard.

> **Note:** The electricity readings used in this project are simulated for educational purposes and do not represent actual campus electricity consumption.

## 🎯 Objectives

- Analyze electricity consumption across campus buildings.
- Calculate total, average, highest, and lowest electricity usage.
- Compare average electricity consumption between buildings.
- Identify readings that exceed a specified electricity usage limit.
- Estimate potential electricity savings and cost reductions.
- Generate and store electricity data in a CSV file.

## ✨ Features

- **Automatic Data Generation:** Generates simulated electricity readings for 30 days.
- **Electricity Summary:** Displays total, average, highest, and lowest consumption.
- **Building-Wise Analysis:** Compares average usage across five buildings.
- **High Usage Detection:** Identifies readings that exceed a user-defined limit.
- **Savings Estimator:** Estimates potential electricity savings and financial savings.
- **Daily Usage Report:** Displays total electricity consumption for each day.
- **CSV File Handling:** Saves generated data in a CSV file for analysis.
- **Menu-Driven Interface:** Provides a simple interface through the Python terminal.

## 🏢 Buildings Included

The project simulates electricity usage for these five buildings:

1. Computer Lab
2. Library
3. Classroom
4. Office
5. Workshop

## 🛠️ Technologies Used

- **Python** — Main programming language
- **Pandas** — Data handling and analysis
- **NumPy** — Generation of simulated electricity readings
- **CSV** — Storage of electricity consumption data

## 📁 Project Structure

```text
CampusPulse/
│
├── main.py
├── generate_data.py
├── requirements.txt
├── README.md
│
└── data/
    └── campus_data.csv
```

The `data` folder and CSV file are generated automatically when the program creates the dataset.

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/deeveshnemade2007/CampusPulse.git
```

### Step 2: Open the Project Folder

```bash
cd CampusPulse
```

### Step 3: Install the Required Libraries

```bash
python -m pip install pandas numpy
```

### Step 4: Run the Program

```bash
python main.py
```

## ▶️ How to Use

After running the program, a menu appears in the terminal.

```text
========================================
 CAMPUSPULSE ELECTRICITY ANALYZER
========================================

============== MAIN MENU ==============
1. Generate Electricity Dataset
2. View Electricity Summary
3. View Building-Wise Usage
4. Detect High Electricity Usage
5. Estimate Electricity Savings
6. View Daily Electricity Usage
7. Exit

Enter your choice (1-7):
```

Select an option by entering its corresponding number.

| Option | Function |
|---|---|
| 1 | Generate a new electricity dataset |
| 2 | View the electricity summary |
| 3 | Compare building-wise electricity usage |
| 4 | Detect high electricity usage |
| 5 | Estimate electricity and cost savings |
| 6 | View daily electricity consumption |
| 7 | Exit the program |

**Tip:** The dataset is generated automatically if it does not exist. You can also select option 1 to generate it manually.

## 📊 Dataset Information

The generated dataset contains **150 records**, representing 30 days of simulated readings for five buildings.

| Column | Description |
|---|---|
| Day | Day number from 1 to 30 |
| Building | Name of the campus building |
| Electricity_kWh | Simulated electricity consumption in kWh |

Occasional unusually high readings are included to demonstrate the high-usage detection feature.

## 💡 Applications

- Educational electricity consumption analysis
- Building-wise energy usage comparison
- Identification of unusually high readings
- Basic energy conservation planning
- Demonstration of Python data analysis and CSV file handling

## 🚀 Future Improvements

- Use real electricity meter readings.
- Add monthly and yearly consumption reports.
- Generate graphical reports and charts.
- Store historical readings in a database.
- Develop a web dashboard for real-time monitoring.
- Add machine learning for electricity consumption prediction.

## 🎓 Learning Outcomes

Through this project, users can practise:

- Python functions and loops
- Conditional statements
- Exception handling
- File and directory handling
- CSV data storage
- Data analysis using Pandas
- Numerical operations using NumPy
- Menu-driven programming

## 👨‍💻 Author

**Deevesh Nemade**

Electronics and Computer Engineering Student

## 📄 Disclaimer

CampusPulse is an educational mini project. The electricity readings are simulated and should not be treated as actual measurements or predictions of electricity consumption.

---

⭐ If you find this project useful, consider giving the repository a star!