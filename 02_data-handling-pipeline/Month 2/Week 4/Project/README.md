

# 🏠 House Prices Exploratory Data Analysis (EDA) Project

## Project Overview

This project was completed as part of my **AI/ML February Week 4 roadmap** and serves as a continuation of the Week 3 Feature Engineering project.

The objective of this project was to perform **Exploratory Data Analysis (EDA)** on the processed House Prices dataset developed during Week 3 and derive meaningful insights about the factors influencing house prices.

Rather than repeating the cleaning and preprocessing steps, this project focused on understanding the prepared dataset through visualizations and analysis.

---

## Dataset

* **Dataset:** House Prices: Advanced Regression Techniques
* **Source:** Kaggle
* **Dataset Used:** Feature-engineered dataset generated during the Week 3 project
* **Rows:** 1460
* **Columns:** 221
* **Target Variable:** `SalePrice`

---

## Project Workflow

### 1. Dataset Continuation from Week 3

* Imported the processed dataset created during the Feature Engineering project.
* Reused the cleaned and transformed data instead of repeating preprocessing steps.

**Why?**

Week 3 focused on preparing the data, while Week 4 focused on understanding the prepared dataset and extracting insights.

---

### 2. Target Variable Analysis

Analyzed the distribution of `SalePrice` using:

* Histogram
* Kernel Density Estimate (KDE)
* Boxplot

**Why?**

Understanding the target variable helps identify:

* Distribution patterns,
* Presence of skewness,
* Extreme observations,
* Suitability for future machine learning models.

---

### 3. Bivariate Analysis

Investigated relationships between important features and `SalePrice`.

The features were selected based on their importance identified during Week 3.

Analyzed relationships such as:

* `TotalSF` vs `SalePrice`
* `TotalBathrooms` vs `SalePrice`
* `OverallQual` vs `SalePrice`
* Other highly informative features identified through Mutual Information.

**Why?**

Bivariate analysis reveals how strongly individual features influence house prices.

---

### 4. Mutual Information Guided Exploration

Revisited the Mutual Information scores obtained during Week 3.

Used the highest-ranked features to guide further analysis.

**Why?**

Mutual Information captures both linear and nonlinear relationships between features and the target variable, allowing the analysis to focus on the most informative variables.

---

### 5. Correlation Analysis

Performed correlation analysis on important features selected from the Mutual Information results.

Included:

* Correlation matrix
* Correlation heatmap
* Examination of feature relationships

**Why?**

Correlation analysis helps identify:

* Strong predictors of house prices,
* Redundant variables,
* Potential multicollinearity among features.

---

### 6. Feature Engineering Evaluation

Revisited engineered features created during Week 3, including:

* `TotalSF`
* `TotalBathrooms`

Analyzed whether these newly created variables exhibited meaningful relationships with `SalePrice`.

**Why?**

EDA helps validate whether engineered features successfully capture useful information.

---

## Key Insights

* `SalePrice` exhibits a right-skewed distribution, indicating that expensive houses are relatively uncommon.
* A small number of high-priced properties appear as outliers in the dataset.
* `TotalSF` demonstrates a strong positive relationship with house prices.
* Houses with larger usable areas generally command higher prices.
* Engineered features such as `TotalBathrooms` provide additional explanatory power beyond individual original variables.
* Features identified through Mutual Information analysis also displayed strong visual relationships with `SalePrice`.
* Quality and size-related characteristics emerged as dominant factors influencing property values.
* Correlation analysis confirmed that only a subset of the 221 processed features strongly contributed to price variation.
* Certain highly correlated features may provide overlapping information during model building.
* The engineered dataset preserved meaningful patterns despite the increase in dimensionality caused by encoding.

---

## Dataset Evolution

```text
Original Dataset                  : 1460 × 81
After Feature Engineering         : 1460 × 221
EDA Dataset Analyzed              : 1460 × 221
```

---

## Conclusion

This project demonstrates how Exploratory Data Analysis can be used to extract meaningful insights from a processed dataset.

By building upon the preprocessing and feature engineering pipeline developed in Week 3, the analysis validated engineered features, identified influential variables, and established a deeper understanding of the factors affecting house prices.

Together, the Week 3 and Week 4 projects form a complete data preparation and exploration workflow, creating a strong foundation for subsequent machine learning model development.

---

### Continuity with Week 3

```text
Week 3:
Raw Housing Dataset
        ↓
Data Cleaning
        ↓
Missing Value Handling
        ↓
Feature Engineering
        ↓
Encoding & Scaling
        ↓
Mutual Information Analysis
        ↓
Processed Dataset (1460 × 221)

Week 4:
Processed Dataset
        ↓
Target Variable Analysis
        ↓
Bivariate Analysis
        ↓
Correlation Analysis
        ↓
Feature Engineering Validation
        ↓
Insights & Conclusions
        ↓
Ready for Machine Learning
```