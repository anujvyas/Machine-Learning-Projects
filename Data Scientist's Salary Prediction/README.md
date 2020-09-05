![DSSP](readme-resources/data-scientist-salary-banner.png)
![Dataset](https://img.shields.io/badge/Dataset-Ken_Jee-blue.svg) ![Python 3.6](https://img.shields.io/badge/Python-3.6-brightgreen.svg) ![library](https://img.shields.io/badge/Library-sklearn-orange.svg)

## Project Overview
• Created a machine learning model that **estimates salary of data scientist based on the features like rating, company_founded, etc.**<br/>
• Engineered features from the text of each job description to quantify the value companies put on python, excel, tableau and sql

## How will this project help?
• This project **helps data scientist/analyst to negotiate their income for an existing or a new job**

## Resources Used
• Packages: **pandas, numpy, sklearn, matplotlib, seaborn.**<br/>
• Dataset by **Ken Jee**: https://github.com/PlayingNumbers/ds_salary_proj

## Exploratory Data Analysis (EDA) and Data Cleaning
• **Removed unwanted columns**: 'Unnamed: 0'<br/>
• **Plotted bargraphs and countplots** for numerical and categorical features respectively for EDA<br/>
• **Numerical Features** (Rating, Founded): **Replaced NaN or -1 values with mean or meadian based on their distribution**<br/>
![rating](readme-resources/rating.png) ![rating1](readme-resources/rating1.png)<br/>
• **Categorical Features: Replaced NaN or -1 values with 'Other'/'Unknown' category**<br/>
• **Removed unwanted alphabet/special characters from Salary feature**<br/>
• **Converted the Salary column into one scale** i.e from (per hour, per annum, employer provided salary) to (per annum)

## Feature Engineering
• **Creating new features** from existing features e.g. **job_in_headquaters from (job_location, headquarters)**, etc.<br/>
![jih](readme-resources/jih.png)<br/>
• Trimming columns i.e. **Trimming features having more than 10 categories to reduce the dimensionality**<br/>
• **Handling ordinal and nominal categorical features**<br/>
• Feature Selection using **information gain (mutual_info_regression) and correlation matrix**<br/>
![infogain](readme-resources/infogain.png)<br/>
![corr1](readme-resources/corr1.png)<br/>
• Feature Scaling using **StandardScalar**

## Model Building and Evaluation
Metric: Negative Root Mean Squared Error (NRMSE)<br/>
• Multiple Linear Regression: -27.523<br/>
• Lasso Regression: -27.993<br/>
• **Random Forest: -17.637**<br/>
• Gradient Boosting: -24.429<br/>
• Voting (Random Forest + Gradient Boosting): -19.136<br/>
_**Note: Evaluation scores are obtained using cross validation.**_

## Model Prediction
![Prediction](readme-resources/prediction.PNG)
