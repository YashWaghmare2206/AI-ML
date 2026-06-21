# 🏠 House Prices Feature Engineering Project

## Project Overview

This project was completed as part of my **AI/ML February Week 3 roadmap**. The objective was to build a complete **data preprocessing and feature engineering pipeline** using the Kaggle House Prices dataset, without training any predictive model.

---

## Dataset

* **Dataset:** House Prices: Advanced Regression Techniques
* **Source:** Kaggle
* **File Used:** `train.csv`
* **Rows:** 1460
* **Original Columns:** 81
* **Target Variable:** `SalePrice`

---

## Project Workflow

### 1. Data Understanding

* Explored dataset structure using shape, info, and descriptive statistics.
* Identified numerical, categorical, and missing-value columns.

---

### 2. Missing Value Handling

Missing values were handled using domain knowledge instead of applying a single strategy.

Examples:

* `Alley`, `PoolQC`, `Fence`, `FireplaceQu` → `"None"`
* Basement-related features → `"None"`
* Garage-related features → `"None"`
* `Electrical` → Mode
* `LotFrontage` → Grouped imputation

**Why?**
Many missing values represented the absence of amenities rather than missing information.

---

### 3. Outlier and Distribution Analysis

* Used histograms and boxplots.
* Checked skewness before applying transformations.

**Why?**
Outliers and skewed distributions affect imputation and feature quality.

---

### 4. Log Transformations

Applied `log1p()` to:

* `LotFrontage`
* `MasVnrArea`

**Why?**
To reduce right skewness and minimize the effect of extreme values.

---

### 5. Feature Engineering

Created new features such as:

* `HouseAge`
* `GarageAge`
* `RemodelAge`
* `TotalBathrooms`
* `TotalSF`
* `TotalPorchSF`
* `TotalOutsideSF`
* `HasGarage`
* `HasBasement`
* `HasFireplace`

**Why?**
Engineered features often capture information more effectively than raw variables.

---

### 6. Encoding

#### Ordinal Encoding

Applied to ordered categories such as:

* ExterQual
* KitchenQual
* HeatingQC
* GarageFinish

#### One-Hot Encoding

Applied to nominal features such as:

* Neighborhood
* MSZoning
* SaleCondition
* GarageType

**Why?**
Different categorical variables require different encoding techniques.

---

### 7. Mutual Information

Used **Mutual Information Regression** to identify the most informative features for predicting `SalePrice`.

**Why?**
To measure the relationship between features and the target variable, including nonlinear relationships.

---

### 8. Feature Scaling

Applied **StandardScaler** to selected continuous variables used in clustering.

**Why?**
Distance-based algorithms are sensitive to feature scales.

---

### 9. K-Means Clustering

Performed clustering using important features such as:

* TotalSF
* GrLivArea
* OverallQual

Cluster quality was evaluated using:

* Elbow Method
* Silhouette Score

**Why?**
To explore natural groupings of houses based on their characteristics.

---

## Key Insights

* `TotalSF` emerged as the most informative feature.
* Engineered features such as `HouseAge` and `TotalBathrooms` ranked highly in Mutual Information.
* Quality-related features strongly influenced house prices.
* Missing values often represented the absence of amenities rather than incomplete records.
* Only a subset of the 221 processed features carried substantial information.

---

## Dataset Evolution

```text
Original Dataset      : 1460 × 81
After Feature Engineering
and Encoding          : 1460 × 221
```

---

## Conclusion

This project demonstrates a complete preprocessing and feature engineering workflow on a real-world dataset. It highlights the importance of thoughtful data preparation, feature engineering, and feature selection before applying machine learning techniques.
