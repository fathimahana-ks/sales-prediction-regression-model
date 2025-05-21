# Sales Prediction Using Linear Regression

Predict sales based on marketing budgets across different channels using a linear regression model. This project includes data cleaning, visualization, and building a prediction model.

---

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Project Details](#project-details)
- [Results](#results)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

This project uses a **dummy marketing and sales dataset** created for educational purposes, specifically designed for courses like *Data-Driven Marketing* and *Data Science for Business*.

The goal is to explore the relationship between promotional budgets across TV, Radio, Social Media, and influencer types, and how they impact sales. The project covers:

- Data preprocessing  
- Exploratory data analysis (EDA)  
- Visualization of marketing impact  
- Sales prediction using linear regression  
- Model evaluation

---

## Dataset

The dataset includes the following columns:

- **TV:** TV promotion budget (in million)  
- **Social Media:** Social Media promotion budget (in million)  
- **Radio:** Radio promotion budget (in million)  
- **Influencer:** Influencer category involved in promotion (Mega, Macro, Micro, Nano)  
- **Sales:** Sales generated (in million)  

This dataset is ideal for tasks such as data preprocessing, exploratory analysis, visualization, and building predictive models using linear regression.

---

## Prerequisites

Make sure you have Python 3 installed.  
You will need the following Python libraries:

- pandas  
- numpy  
- matplotlib  
- seaborn  
- scikit-learn  
- statsmodels  

Install all dependencies using:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels
```

## Installation

1. Clone this repository:

```bash
git clone <repo-url>
cd <repo-folder>
```

2. Download the dataset from [here](https://www.kaggle.com/harrimansaragih/dummy-advertising-and-sales-data) and place the CSV file inside a folder named `data` in the project directory.

 Your folder structure should look like this:<br>

`project-folder/`<br>
│<br>
├── `data/`<br>
│  └── `Dummy Data HSS.csv`<br>
│<br>
├── `sales_prediction.py`<br>
└── `README.md`<br>

## How to Run

1. Open your terminal or command prompt in the project directory.

2. Execute the Python script:

```bash
python sales_prediction.py
```
The script will:
Load and clean the dataset
Perform exploratory data analysis with visualizations
Train a linear regression model
Output the model coefficients and evaluation metrics

## Project Details

- **Data Cleaning:** - Handles missing values and removes duplicates for clean data analysis.  
- **Exploratory Data Analysis (EDA):** - Generates bar charts, scatter plots, histograms, box plots, and heatmaps to uncover insights and relationships in the data.  
- **Modeling:** - Implements a linear regression model to predict sales based on marketing budgets from TV, Radio, and Social Media channels.  
- **Model Evaluation:** - Displays model coefficients, intercept, and R-squared value to assess model performance and feature influence.  

## Results

Upon running the script, you will get:
- **Model Coefficients:** Indicate the impact of each marketing channel on sales.  
- **Intercept:** The baseline sales value when all marketing budgets are zero.  
- **R-squared Score:** Shows the proportion of variance in sales explained by the model (higher is better).  

These results help understand which marketing efforts most strongly affect sales and how well the linear regression model fits the data.




