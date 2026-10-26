# Project 1 — Bank Customer Segmentation

## 1. Project Overview

This project applies **Unsupervised Learning techniques to segment bank customers into meaningful groups based on their characteristics and interaction behavior**.

We will use the **UCI Bank Marketing dataset**, which contains data from direct marketing campaigns conducted by a Portuguese banking institution. The full `bank-full.csv` dataset contains **45,211 records and 17 columns including the target variable**, with a mixture of numerical, categorical, and binary variables.

**Important:** This is NOT going to be a classification project.

The original dataset contains a target:

```text
y = whether the customer subscribed to a term deposit
```

We will **not use `y` to create the clusters**.

Instead, the project asks:

> **Can we discover naturally occurring customer segments without being told what the segments are?**

---

# 2. Main Aim

The primary objective is **not simply to obtain clusters**.

The real objective is:

> **To develop practical understanding of how different unsupervised learning algorithms behave on a realistic mixed-type dataset, how preprocessing and representation affect clustering, how to evaluate clusters, and how to interpret the resulting segments.**

By the end of the project, we should be able to approach an unfamiliar clustering problem like this:

```text
What does my data look like?
        ↓
What representation should I use?
        ↓
What preprocessing is appropriate?
        ↓
Which clustering algorithms make sense?
        ↓
What parameters should I try?
        ↓
How do I evaluate the clusters?
        ↓
Why are the clusters different?
        ↓
Are they actually meaningful?
        ↓
Which approach would I choose and why?
```

That is the main learning goal.

---

# 3. What We Are NOT Trying To Do

We are **NOT** trying to:

- maximize classification accuracy
- predict `y`
- build a bank marketing classifier
- blindly apply every clustering algorithm
- find one "perfect" number of clusters
- optimize a Kaggle leaderboard
- create dozens of meaningless visualizations
- implement algorithms from scratch
- use every possible ML technique just to make the project larger

Instead, we are trying to **understand the algorithms through experimentation**.

---

# 4. Dataset

## UCI Bank Marketing

**Official dataset:**  
https://archive.ics.uci.edu/dataset/222/bank+marketing

The dataset contains information related to direct marketing campaigns conducted through phone calls by a Portuguese banking institution. The full `bank-full.csv` version contains **45,211 observations and 17 columns**, including the target.

The input variables include characteristics such as:

- age
- job
- marital status
- education
- default status
- account balance
- housing loan
- personal loan
- contact type
- contact day/month
- call duration
- campaign contacts
- previous campaign information
- previous campaign outcome

The dataset contains a mixture of categorical, binary, integer, and other feature types.

### Dataset Citation

Moro, S., Rita, P., & Cortez, P. (2014). *Bank Marketing*. UCI Machine Learning Repository. DOI: 10.24432/C5K306.

---

# 5. Core Learning Questions

Throughout the project, continuously answer questions like:

## Data

- What does one row represent?
- Which variables describe the customer?
- Which describe the marketing campaign?
- Which variables are numerical?
- Which are categorical?
- Which variables have unusual distributions?
- Are there hidden issues in the representation?

## Preprocessing

- Why do clustering algorithms care about feature scale?
- What happens if we don't scale?
- How should categorical variables be represented?
- Does one-hot encoding create problems?
- Should every feature be included?
- Should highly skewed variables be transformed?
- What happens when we change the feature representation?

## Clustering

- Why does K-Means produce these clusters?
- Why does changing `k` change the result?
- Why does DBSCAN consider some customers noise?
- Why does hierarchical clustering produce different structures with different linkage methods?
- What does Spectral Clustering actually add?
- Why might GMM produce overlapping groups?

## Evaluation

- What does silhouette score actually measure?
- When can inertia be misleading?
- What does Davies-Bouldin tell us?
- What does Calinski-Harabasz tell us?
- Can a mathematically "better" cluster be less useful in practice?

## Interpretation

- What characteristics distinguish each cluster?
- Are the clusters actually meaningful?
- Can we describe a customer segment in human terms?
- Which algorithm gives the most useful segmentation?

---

# 6. Algorithms We Will Cover

This project will be used to practically revisit the clustering algorithms already studied.

## 6.1 K-Means

Deep experimentation with:

- choice of `k`
- random initialization
- K-Means++
- inertia / WCSS
- elbow method
- silhouette score
- different random seeds
- cluster stability
- cluster size
- effect of preprocessing
- interpretation of cluster centers

---

## 6.2 Hierarchical Clustering

Experiment with:

- agglomerative clustering
- dendrogram
- different linkage methods:
  - Ward
  - Complete
  - Average
  - Single
- different numbers of clusters
- comparison with K-Means

We should understand **why changing linkage changes the resulting structure**.

---

## 6.3 DBSCAN

This should be a particularly experimental section.

Investigate:

- `eps`
- `min_samples`
- k-distance idea
- core points
- border points
- noise points
- number of discovered clusters
- percentage of noise
- sensitivity to parameters
- situations where DBSCAN struggles

The goal is not simply:

```python
DBSCAN().fit_predict(X)
```

The goal is to understand:

> **Why did DBSCAN produce this particular structure?**

---

## 6.4 Spectral Clustering

Investigate:

- graph-based interpretation
- affinity
- nearest-neighbor similarity
- number of clusters
- relationship to K-Means
- when graph-based clustering might help

We don't need to artificially spend hours tuning every possible parameter.

The goal is to understand **what makes Spectral Clustering conceptually different**.

---

## 6.5 Gaussian Mixture Models

Investigate:

- number of components
- hard vs soft clustering
- probability assignments
- covariance types
- EM intuition
- BIC
- AIC
- cluster overlap
- comparison with K-Means

Example:

```text
Customer A

Cluster 1 → 0.91
Cluster 2 → 0.07
Cluster 3 → 0.02
```

versus:

```text
Customer B

Cluster 1 → 0.48
Cluster 2 → 0.45
Cluster 3 → 0.07
```

This demonstrates why GMM can represent uncertainty in cluster membership.

---

# 7. Dimensionality Reduction

We will also use the dimensionality-reduction techniques already studied.

## 7.1 PCA

Use PCA to understand:

- explained variance
- number of components
- feature contributions/loadings
- 2D/3D visualization
- relationship between original features and principal components

PCA should be treated as a **real analytical tool**, not just a plotting trick.

---

## 7.2 t-SNE

Use t-SNE primarily for:

- visualization
- investigating local structure
- understanding parameter effects

Experiment with:

- perplexity
- random seed
- visualization stability

Important:

> **A beautiful t-SNE plot does NOT automatically mean that the underlying clusters are real.**

---

## 7.3 UMAP

Use UMAP to compare:

- local structure
- global structure
- visualization behavior
- parameter effects
- comparison with PCA and t-SNE

Again, distinguish:

```text
Visualization
      ≠
Clustering algorithm
```

---

# 8. Preprocessing Is a Major Part of the Project

Preprocessing should **not** be treated as a 5-minute section.

Because this dataset contains mixed feature types, preprocessing itself becomes an important learning exercise.

## Numerical Features

Investigate:

- distributions
- skewness
- outliers
- scaling
- potentially useful transformations

## Categorical Features

Investigate:

- One-Hot Encoding
- dimensionality created by encoding
- effect on distance-based algorithms

## Binary Features

Understand whether they should simply be treated as numerical 0/1 variables.

## Feature Representation

We will ask:

> **Does the representation of the data change the clusters?**

This is one of the most important practical lessons of the project.

---

# 9. Feature Selection

We should **not automatically feed every column into every algorithm**.

For every important feature, ask:

> Does this feature represent something meaningful for the segmentation objective?

We should also identify variables that are primarily associated with the **marketing campaign process** rather than intrinsic customer characteristics.

This creates an important real-world discussion:

```text
Customer characteristics
          vs
Campaign interaction characteristics
```

The resulting clusters can change depending on which perspective we want.

---

# 10. Target Leakage / Unsupervised Learning Rule

The original dataset contains:

```text
y
```

representing whether the client subscribed to a term deposit.

For the clustering stage:

### `y` MUST NOT be used.

It should not be:

- an input feature
- used to train clustering
- used to select clusters
- used to calculate clustering distances

Only after the clustering is finished may we optionally use `y` **as an external descriptive variable** to investigate whether discovered segments differ in subscription behavior.

For example:

```text
Cluster 0 → subscription rate
Cluster 1 → subscription rate
Cluster 2 → subscription rate
```

This is **post-hoc analysis**, not clustering supervision.

---

# 11. Evaluation Framework

We will not rely on a single metric.

## Internal Evaluation

Use:

- Silhouette Score
- Davies-Bouldin Index
- Calinski-Harabasz Index

For K-Means additionally:

- Inertia / WCSS

For GMM:

- BIC
- AIC

For DBSCAN:

- number of clusters
- percentage of noise
- cluster structure
- internal metrics where appropriate

---

# 12. Cluster Stability

This is an important practical component.

Suppose K-Means gives:

```text
Seed 1 → clusters A B C
Seed 2 → clusters A B C
Seed 3 → clusters A B C
```

That's encouraging.

But if:

```text
Seed 1 → A B C
Seed 2 → A C D
Seed 3 → B D E
```

we need to question the stability of the solution.

Investigate stability through:

- different random seeds
- repeated runs
- comparison of resulting assignments
- cluster size consistency

This is much more useful than simply reporting:

> "Silhouette score = 0.43."

---

# 13. Algorithm Comparison

At the end, build a comparison such as:

| Algorithm | Cluster Shape | Important Parameters | Strengths | Weaknesses | Result |
|---|---|---|---|---|---|
| K-Means | ... | `k` | ... | ... | ... |
| Hierarchical | ... | linkage, clusters | ... | ... | ... |
| DBSCAN | ... | eps, min_samples | ... | ... | ... |
| Spectral | ... | affinity, clusters | ... | ... | ... |
| GMM | ... | components, covariance | ... | ... | ... |

The conclusion should **not** simply be:

> "Algorithm X had the highest silhouette score, therefore it is the best."

Instead:

> **Which algorithm produces the most useful and interpretable segmentation for this particular problem, and why?**

---

# 14. Cluster Profiling

This is where the project becomes a real segmentation project rather than an ML exercise.

For each final cluster, create a profile.

Example:

```text
Cluster 0
---------------------
Size: 28%

Typical age: ...
Average balance: ...
Housing loan: ...
Personal loan: ...
Previous campaign activity: ...
Dominant occupations: ...
```

Then give it a meaningful interpretation **only if the data supports it**.

For example:

```text
"Older, financially stronger, low-contact customers"
```

rather than:

```text
"Premium customers"
```

unless the data actually supports the term "premium."

---

# 15. Visualization

Visualizations should answer questions.

## Data Understanding

- numerical distributions
- categorical distributions
- correlation analysis where appropriate

## Clustering

- cluster-size plots
- PCA cluster visualization
- t-SNE visualization
- UMAP visualization
- dendrogram
- DBSCAN noise visualization
- GMM probability visualization where useful

## Cluster Profiling

- standardized feature comparison
- cluster-wise distributions
- cluster summary tables

Avoid making 30 plots just to make the notebook look impressive.

---

# 16. Three-Day Structure

## DAY 1 — Understand the Data + Build the Representation

### Part 1 — Dataset Understanding

- Load dataset
- Understand rows/columns
- Data dictionary
- Identify variable types
- Understand what each row represents
- Understand the original target

### Part 2 — EDA

Investigate:

- numerical distributions
- categorical distributions
- missing/unknown values
- outliers
- skewness
- correlations
- unusual values

### Part 3 — Decide Clustering Objective

Define:

> What exactly are we trying to segment?

Possibilities include:

- customer characteristics
- customer behavior
- marketing interaction patterns
- a combination

### Part 4 — Preprocessing Experiments

Build a proper preprocessing pipeline.

Experiment with:

- encoding
- scaling
- feature selection
- transformations

### Part 5 — Baseline K-Means

Start with a simple baseline.

Then investigate:

```text
What happens before scaling?
What happens after scaling?
```

This should provide our first major practical insight.

---

# DAY 2 — Deep Clustering Experiments

## K-Means

Deep dive into:

- K selection
- elbow
- silhouette
- initialization
- seeds
- stability
- cluster interpretation

## Hierarchical

Investigate:

- linkage
- dendrogram
- cluster cuts
- comparison with K-Means

## DBSCAN

Investigate:

- eps
- min_samples
- k-distance
- noise
- parameter sensitivity

## Spectral

Investigate:

- affinity
- nearest-neighbor representation
- comparison with K-Means

## GMM

Investigate:

- components
- covariance
- soft assignments
- BIC/AIC
- overlap

### Day 2 Goal

> **Understand why different algorithms produce different answers.**

---

# DAY 3 — Dimensionality Reduction + Evaluation + Final Segmentation

## Part 1 — PCA

- explained variance
- components
- loadings
- visualization

## Part 2 — t-SNE

- visualization
- perplexity
- stability

## Part 3 — UMAP

- visualization
- parameters
- comparison with t-SNE/PCA

## Part 4 — Evaluation

Build the evaluation framework:

```text
Silhouette
Davies-Bouldin
Calinski-Harabasz
Inertia
BIC/AIC
Stability
Interpretability
```

## Part 5 — Compare Algorithms

## Part 6 — Select Final Segmentation

## Part 7 — Profile Clusters

## Part 8 — Write Conclusions

Answer:

- What did we discover?
- Which algorithm worked best?
- Why?
- What preprocessing mattered?
- What didn't work?
- What limitations exist?
- What would we do with more time/data?

---

# 17. Scratch Implementation Policy

We are **not implementing the algorithms from scratch**.

We'll use:

```python
scikit-learn
```

and appropriate supporting libraries.

The reason is deliberate.

The mathematical mechanisms have already been studied.

This project is about developing the next skill:

> **Using ML algorithms intelligently rather than merely knowing how they work internally.**

We will still connect experiments back to the mathematics.

For example:

```text
K-Means objective
       ↓
WCSS / inertia
       ↓
Why scaling matters
       ↓
Why distance dominates
       ↓
Why feature representation matters
```

The math remains relevant without wasting project time reimplementing library algorithms.

---

# 18. Depth Standard

For every major algorithm, follow:

```text
1. Understand
       ↓
2. Apply baseline
       ↓
3. Change important parameters
       ↓
4. Observe what changes
       ↓
5. Explain why
       ↓
6. Evaluate
       ↓
7. Compare
       ↓
8. Decide when to use it
```

If we can't explain **why the result changed**, the experiment isn't finished.

This is the standard for the entire project.

---

# 19. Expected Final Notebook Structure

```text
01. Project Objective
02. Dataset Introduction
03. Business/ML Problem
04. Import Libraries
05. Load Dataset
06. Data Understanding
07. Data Dictionary
08. Exploratory Data Analysis
09. Data Quality Investigation
10. Feature Type Analysis
11. Clustering Objective
12. Feature Selection
13. Preprocessing Strategy
14. Representation Experiments
15. Baseline K-Means
16. K-Means Experiments
17. Hierarchical Clustering
18. DBSCAN
19. Spectral Clustering
20. Gaussian Mixture Models
21. PCA
22. t-SNE
23. UMAP
24. Cluster Evaluation
25. Stability Analysis
26. Algorithm Comparison
27. Final Model/Segmentation Selection
28. Cluster Profiling
29. Business Interpretation
30. Limitations
31. Key Learnings
32. Final Conclusion
```

This is the **target structure**, not a requirement that every section becomes enormous.

---

# 20. Final Deliverables

By the end of the three days:

```text
Project_01_Bank_Customer_Segmentation/
│
├── README.md
│
├── notebooks/
│   └── 01_Bank_Customer_Segmentation.ipynb
│
├── data/
│   └── README.md
│
├── images/
│   └── important_visualizations/
│
└── requirements.txt
```

We should **not upload the raw UCI dataset unnecessarily** if the repository can instead document how to obtain it.

---

# 21. GitHub Quality

The GitHub version should communicate:

### Problem

What are we trying to discover?

### Dataset

Where did it come from?

### Methodology

What did we try?

### Experiments

What changed when we changed preprocessing/parameters?

### Results

What did we discover?

### Interpretation

What do the clusters mean?

### Limitations

What should we be careful about?

### Learning

What did this project teach us?

This will make it much stronger than a notebook that simply contains:

```python
kmeans.fit(X)
```

followed by a scatter plot.

---

# 22. LinkedIn Angle

The interesting story is not:

> "I implemented K-Means on a dataset."

Instead:

> **I explored how different unsupervised learning algorithms discover customer segments from mixed-type banking data, and investigated how preprocessing, feature representation, hyperparameters, dimensionality reduction and cluster evaluation affect the resulting segmentation.**

This makes the project a stronger learning story.

---

# 23. What Success Looks Like

At the end of Project 1, you should be able to answer:

- **When would you choose K-Means over DBSCAN?**
- **Why did scaling change your clusters?**
- **Why can't you blindly use t-SNE for clustering?**
- **What does the silhouette score actually tell you?**
- **Why did DBSCAN label some customers as noise?**
- **Why did two linkage methods produce different hierarchical clusters?**
- **Why might GMM be preferable to K-Means?**
- **How do you decide the number of clusters?**
- **How do you know whether your clusters are stable?**
- **What makes a cluster useful beyond having a good metric?**

If you can answer those from your own experiments, **the project has succeeded.**

---

# 24. Final Project Definition

| Item | Decision |
|---|---|
| **Project 1** | Bank Customer Segmentation |
| **Dataset** | UCI Bank Marketing — `bank-full.csv` |
| **Scale** | ~45K records |
| **Time** | ~3 days × 3–4 hours |
| **Primary Goal** | Practical understanding of clustering |
| **Algorithms** | K-Means, Hierarchical, DBSCAN, Spectral, GMM |
| **Dimensionality Reduction** | PCA, t-SNE, UMAP |
| **Focus** | Preprocessing → experimentation → evaluation → stability → interpretation |
| **Scratch Implementation** | ❌ No |
| **GitHub** | ✅ |
| **LinkedIn-ready** | ✅ |
| **Classification using `y`** | ❌ |
| **Post-hoc analysis using `y`** | ✅ |
| **Project 2** | ❌ Not touched until Project 1 is complete |

---

## Project Philosophy

The project follows:

> **Learn → Experiment → Observe → Explain → Compare → Conclude**

Not:

> **Learn → call sklearn → get graph → done.**

The objective is to finish the project with **practical intuition about unsupervised learning**, not merely a completed notebook.
