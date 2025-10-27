# Claude Code Web - Data Analysis Demo

A comprehensive repository demonstrating data analysis capabilities using Claude Code on the web. This project showcases various data science techniques including data cleaning, exploratory analysis, visualization, statistical testing, and machine learning.

## 📊 Overview

This repository contains:
- Sample datasets for sales and customer data
- Python scripts for various data analysis tasks
- Interactive Jupyter notebook tutorials
- Machine learning examples
- Data visualization demonstrations

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/juanklopper/ClaudeCodeWebForDataAnalysis.git
cd ClaudeCodeWebForDataAnalysis
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## 📁 Project Structure

```
ClaudeCodeWebForDataAnalysis/
├── data/                          # Sample datasets
│   ├── sales_data.csv            # Sales transactions data
│   └── customer_data.csv         # Customer information data
├── scripts/                       # Analysis scripts
│   ├── 01_data_loading.py        # Data loading and exploration
│   ├── 02_data_cleaning.py       # Data cleaning and preprocessing
│   ├── 03_exploratory_analysis.py # EDA and summary statistics
│   ├── 04_visualization.py       # Data visualization examples
│   └── 05_statistical_analysis.py # Statistical tests and analysis
├── notebooks/                     # Jupyter notebooks
│   └── data_analysis_tutorial.ipynb # Interactive tutorial
├── examples/                      # Advanced examples
│   └── ml_prediction_example.py  # Machine learning workflow
├── outputs/                       # Generated plots and results
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🔍 Features

### 1. Data Loading and Exploration
Learn how to:
- Load CSV data using pandas
- Inspect data types and structure
- Check for missing values
- View basic statistics

**Run:** `python scripts/01_data_loading.py`

### 2. Data Cleaning
Demonstrates:
- Date/time conversions
- Handling duplicates
- Data validation
- Creating derived features

**Run:** `python scripts/02_data_cleaning.py`

### 3. Exploratory Data Analysis
Includes:
- Summary statistics
- Grouping and aggregation
- Category and regional analysis
- Correlation analysis

**Run:** `python scripts/03_exploratory_analysis.py`

### 4. Data Visualization
Creates various plots:
- Bar charts (revenue by category)
- Line plots (sales trends)
- Pie charts (regional distribution)
- Histograms (age distribution)
- Scatter plots (relationships)
- Heatmaps (correlations)

**Run:** `python scripts/04_visualization.py`

### 5. Statistical Analysis
Performs:
- Descriptive statistics
- Confidence intervals
- Hypothesis testing (ANOVA, t-tests)
- Linear regression
- Correlation tests

**Run:** `python scripts/05_statistical_analysis.py`

### 6. Machine Learning
Demonstrates:
- Feature engineering
- Model training (Linear Regression, Random Forest)
- Model evaluation
- Feature importance analysis
- Making predictions

**Run:** `python examples/ml_prediction_example.py`

## 📓 Interactive Tutorial

Launch the Jupyter notebook for an interactive learning experience:

```bash
jupyter notebook notebooks/data_analysis_tutorial.ipynb
```

The notebook covers all topics with step-by-step explanations and visualizations.

## 📊 Sample Datasets

### Sales Data
Contains 28 transactions with the following columns:
- `date`: Transaction date
- `product`: Product name
- `category`: Product category (Electronics, Furniture, Supplies)
- `quantity`: Units sold
- `price`: Unit price
- `revenue`: Total revenue
- `region`: Sales region (North, South, East, West)

### Customer Data
Contains 20 customer records with:
- `customer_id`: Unique identifier
- `age`: Customer age
- `gender`: Gender (M/F)
- `income`: Annual income
- `purchase_frequency`: Purchases per year
- `satisfaction_score`: Rating (1-5)
- `member_since`: Membership start date

## 🛠️ Technologies Used

- **pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib**: Static visualizations
- **Seaborn**: Statistical data visualization
- **scikit-learn**: Machine learning
- **SciPy**: Scientific computing and statistics
- **Jupyter**: Interactive notebooks
- **Plotly**: Interactive visualizations

## 📈 Example Outputs

The scripts generate various visualizations saved in the `outputs/` directory:
- Revenue analysis charts
- Sales trend graphs
- Customer distribution plots
- Correlation heatmaps
- Feature importance charts
- Prediction comparison plots

## 🎯 Learning Objectives

After working through this repository, you will be able to:
1. Load and explore datasets effectively
2. Clean and preprocess data for analysis
3. Perform comprehensive exploratory data analysis
4. Create meaningful visualizations
5. Conduct statistical hypothesis testing
6. Build and evaluate machine learning models
7. Interpret results and derive insights

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Add more examples
- Improve documentation

## 📝 License

This project is open source and available for educational purposes.

## 🔗 Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/index.html)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Jupyter Documentation](https://jupyter.org/documentation)

## 💡 Tips for Using Claude Code

This repository is designed to demonstrate Claude Code's capabilities:
- Use it to understand data analysis workflows
- Experiment with the code and modify parameters
- Ask Claude to explain specific concepts
- Request alternative approaches or optimizations
- Explore additional analysis techniques

## 📧 Contact

For questions or feedback, please open an issue in this repository.

---

**Happy Analyzing! 📊🚀**
