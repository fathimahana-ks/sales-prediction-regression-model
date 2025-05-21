# Sales Prediction Using Linear Regression

A project to predict sales based on marketing budgets across TV, Radio, Social Media, and Influencer categories using linear regression.

---

##  Overview

This project demonstrates how to:

- Perform data preprocessing and cleaning  
- Conduct exploratory data analysis (EDA) with visualizations  
- Build and evaluate a linear regression model for sales prediction  
- Understand the influence of different marketing channels on sales  

---

##  Key Features

-  **Data Cleaning:** Handling missing values and duplicates  
-  **Exploratory Data Analysis:** Bar charts, scatter plots, histograms, boxplots, and heatmaps  
-  **Linear Regression Modeling:** Predict sales from TV, Radio, and Social Media budgets  
-  **Model Evaluation:** Coefficients, intercept, and R-squared metrics  

---

## Dataset
The dataset includes the following columns:

- *TV:* TV promotion budget (in million)  
- *Social Media:* Social Media promotion budget (in million)  
- *Radio:* Radio promotion budget (in million)  
- *Influencer:* Influencer category involved in promotion (Mega, Macro, Micro, Nano)  
- *Sales:* Sales generated (in million)  

This dataset is ideal for tasks such as data preprocessing, exploratory analysis, visualization, and building predictive models using linear regression.

---

##  Project Structure

Your folder structure should look like this:<br><br>
`sales-prediction/`<br>
│<br>
├── `data/`<br>
│  └── `Dummy Data HSS.csv`<br>
│<br>
├── `sales_prediction.py`<br>
└── `README.md`<br><br>

> The dataset CSV goes inside the `data/` folder.  
> The main script `sales_prediction.py` contains all code to run the analysis and modeling.

---

## 🛠️ Technologies Used

- Python  
- Pandas & NumPy  
- Matplotlib & Seaborn  
- Scikit-learn (Linear Regression)  

---

##  How to Run

1. Clone this repo  
2. Download the dataset and place `Dummy Data HSS.csv` in the `data/` folder  
3. Install dependencies:

   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn

3. Run the script:

   ```bash
   sales_prediction.py

---

##  Results

Upon running the script, you will get:

- **Model Coefficients:** Indicate the impact of each marketing channel (TV, Radio, Social Media) on sales.  
- **Intercept:** The baseline sales value when all marketing budgets are zero.  
- **R-squared Score:** Shows the proportion of variance in sales explained by the model (higher is better).

These results help understand which marketing efforts most strongly affect sales and how well the linear regression model fits the data.

---

##  Notes

- Ensure the dataset file is correctly placed in the `data` folder as `Dummy Data HSS.csv`.  
- The project script handles data preprocessing, exploratory analysis, visualization, and modeling end-to-end.  
- You can extend the project by experimenting with other regression models or feature engineering.

---

##  Contact

**Fathima Hana**  
📧 [fathimahanaks@gmail.com](mailto:fathimahanaks@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/fathimahan/)

Feel free to reach out for questions or collaboration!

