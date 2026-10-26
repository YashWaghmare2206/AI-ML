# Project 3 — Industrial Anomaly Detection

## 1. Project Overview

This project applies **Unsupervised Anomaly Detection techniques to real industrial sensor data**.

We will use the **UCI MetroPT-3 Dataset**, collected from the Air Production Unit (APU) compressor of a metro train. The dataset contains **1,516,948 observations and 15 sensor features** and covers multivariate time-series measurements collected during normal operation and periods associated with reported failures. UCI describes it as a dataset for predictive maintenance, anomaly detection, failure explanation, and related tasks.

Official dataset:

https://archive.ics.uci.edu/dataset/791/metropt+3+dataset

The dataset contains pressure, temperature, motor-current, and electrical/valve signals from an industrial compressor.

This project is specifically focused on:

- Statistical anomaly detection
- Isolation Forest
- One-Class SVM
- Local Outlier Factor (LOF)
- Multivariate anomalies
- Anomaly scores
- Threshold selection
- Contamination assumptions
- Temporal behavior
- False positives and false negatives
- Evaluation against known failure periods
- Practical interpretation

The goal is **not simply to label rows as normal/anomalous**.

The goal is to understand:

> **How can we learn what "normal" industrial behavior looks like and identify observations or periods that deviate from it, even when we do not train directly on failure labels?**

---

# 2. Main Aim

The primary objective is:

> **To develop practical understanding of anomaly detection by working with real multivariate sensor data, learning a representation of normal behavior, applying different anomaly-detection approaches, investigating their assumptions and parameters, and evaluating whether the detected anomalies correspond to meaningful operational events.**

The overall workflow:

```text
Raw Industrial Sensor Data
          ↓
Understand the System
          ↓
Time-Series Exploration
          ↓
Define Normal Operating Data
          ↓
Feature Selection / Representation
          ↓
Scaling / Preprocessing
          ↓
Baseline Statistical Methods
          ↓
┌─────────┼───────────────┐
↓         ↓               ↓
Isolation One-Class       LOF
Forest    SVM
↓         ↓               ↓
└─────────┼───────────────┘
          ↓
Anomaly Scores
          ↓
Threshold Selection
          ↓
Point-Level + Period-Level Analysis
          ↓
Compare With Failure Reports
          ↓
False Positive / False Negative Analysis
          ↓
Final Method Comparison
          ↓
Operational Interpretation
```

---

# 3. What We Are NOT Trying To Do

We are **NOT** trying to:

- build a supervised failure classifier
- maximize classification accuracy
- simply train an algorithm on all rows and accept its labels
- assume every statistical outlier is a real failure
- assume every failure is a single anomalous row
- optimize for a single anomaly-detection metric
- implement Isolation Forest, One-Class SVM, or LOF from scratch
- blindly use all 1.5M rows for every experiment
- treat time-series data as ordinary IID tabular data
- use the failure reports as training labels for the main anomaly-detection models

Instead, we are trying to understand:

> **What makes an observation anomalous, how different algorithms define abnormality differently, and how those definitions behave on real sensor data.**

---

# 4. Dataset

## UCI MetroPT-3 Dataset

**Official dataset:**

https://archive.ics.uci.edu/dataset/791/metropt+3+dataset

UCI reports:

- **1,516,948 instances**
- **15 features**
- Multivariate
- Time-series
- No missing values
- Data spanning February–August 2020
- Real industrial sensor measurements
- Failure reports available for evaluation

UCI also recommends using the **first month for training and the remaining period for testing**, which fits our anomaly-detection setup well.

---

# 5. Important Dataset Characteristics

## 5.1 Multivariate

We have multiple sensors describing the same physical system.

```text
Pressure
Temperature
Motor Current
Valve Signals
       ↓
Same compressor
       ↓
Interdependent behavior
```

This allows us to investigate:

> Can a combination of individually normal sensor values still represent an anomaly?

## 5.2 Time-Series

The data are ordered in time.

This means we must think about:

- temporal ordering
- operating states
- transitions
- sustained anomalies
- isolated spikes
- failure periods
- temporal leakage

## 5.3 Failure Reports

The dataset is unlabeled at the row level, but UCI provides failure-event information with start and end times.

This gives us:

```text
Training:
Normal historical operation
        ↓
Learn normal behavior

Testing:
Future sensor data
        ↓
Detect anomalies
        ↓
Compare detected anomalies
with reported failure periods
```

The failure information is therefore primarily used for **evaluation and interpretation**, not for training the unsupervised models.

---

# 6. Sensor Features

The dataset contains 15 signals from analogue and digital sensors.

Important examples include:

### Continuous / analogue measurements

- `TP2` — compressor pressure
- `TP3` — pneumatic-panel pressure
- `H1` — pressure associated with the cyclonic separator filter
- `DV_pressure` — pressure drop associated with air-dryer discharge
- `Reservoirs` — downstream reservoir pressure
- `Oil_temperature` — compressor oil temperature
- `Motor_current` — motor current

### Digital / operational signals

- `COMP`
- `DV_electric`
- `TOWERS`
- `MPG`
- `LPS`
- `Pressure_switch`
- `Oil_level`
- `Caudal_impulse`

We should not simply treat all of these as interchangeable numerical features.

Understanding what each sensor means is part of the project.

---

# 7. Core Learning Questions

Throughout the project, continuously answer:

## What is an anomaly?

- Is an anomaly simply an extreme value?
- Can a normal-looking value be anomalous in context?
- Can a combination of normal values be anomalous?
- Does an anomaly need to persist over time?

## Statistical Detection

- How do z-score and IQR methods define abnormality?
- How does skewness affect statistical thresholds?
- What happens when distributions are not Gaussian?
- What happens when a feature contains multiple operating regimes?

## Isolation Forest

- Why does random partitioning help isolate anomalies?
- What does the anomaly score represent?
- How does `contamination` affect results?
- What happens when we change the number of trees?
- Why might Isolation Forest work well on high-dimensional data?

## One-Class SVM

- What does the learned boundary represent?
- What does `nu` control?
- How does `gamma` affect the boundary?
- Why does scaling matter?
- Why can One-Class SVM become computationally expensive?

## LOF

- What does "local" mean in anomaly detection?
- Why can a point be normal globally but anomalous locally?
- What does `n_neighbors` change?
- How does local density differ from global distance?

## Evaluation

- How do we select a threshold?
- What is a false positive?
- What is a false negative?
- Is point-level accuracy enough?
- Should a 10-second anomaly be treated differently from a 3-hour failure period?

## Practical Interpretation

- Which sensor changes around detected anomalies?
- Are anomalies isolated spikes or sustained periods?
- Do multiple sensors change together?
- Do detected anomalies occur around reported failures?

---

# 8. The Most Important Concept: Learn Normal Behavior

Anomaly detection is fundamentally different from classification.

Instead of:

```text
Normal + labeled examples
       +
Failure + labeled examples
       ↓
Classifier
```

we primarily want:

```text
Normal operational behavior
          ↓
Learn its structure
          ↓
Identify deviations
```

This distinction should remain central throughout the project.

---

# 9. Training/Test Strategy

We should take advantage of the temporal nature of the dataset.

UCI recommends using the **first month for training and the remaining period for testing**.

Conceptually:

```text
FIRST MONTH
──────────────
Training / normal behavior learning
          ↓
Model learns operational behavior


REMAINING MONTHS
─────────────────
Testing
          ↓
Generate anomaly scores
          ↓
Identify suspicious periods
          ↓
Compare with failure reports
```

This is preferable to a random train/test split because random splitting can leak future operating behavior into training.

---

# 10. Critical Question: Is the First Month Completely Normal?

We should **not blindly assume that the first month is perfectly clean**.

Investigate:

- reported failure periods
- sensor behavior
- obvious anomalies
- unusual operating states

If a reported failure occurs in the training period, document how we handle it.

Possible approaches:

- exclude known failure windows from training
- train on the recommended first month and acknowledge contamination
- compare both approaches if time permits

The important part is understanding the effect.

---

# 11. Data Exploration

Before applying any anomaly detector, understand the sensor data.

Investigate:

## Distribution

For each important sensor:

- mean
- median
- standard deviation
- quantiles
- min/max
- skewness
- outliers

## Time Behavior

Plot:

- sensor vs time
- selected periods
- operating transitions
- failure windows
- sensor relationships

## Correlation

Investigate:

- pressure relationships
- motor-current relationships
- temperature relationships
- sensor dependencies

But remember:

> Correlation is not the same as physical causation.

---

# 12. Operating Regimes

An industrial machine may have multiple legitimate operating states:

```text
OFF
 ↓
STARTING
 ↓
LOADED
 ↓
OFFLOADED
 ↓
STARTING
 ↓
...
```

A value that is unusual globally may be perfectly normal in a particular operating regime.

Therefore, investigate:

> **Are we detecting anomalies, or simply detecting different operating states?**

This is one of the most valuable lessons of the project.

---

# 13. Preprocessing

Preprocessing should be a meaningful section.

## Scaling

Investigate:

- StandardScaler
- RobustScaler

Understand why scaling matters especially for:

- One-Class SVM
- LOF
- distance-based methods

## Outliers

Do **not automatically remove outliers**.

In anomaly detection, the unusual points may be exactly what we want to detect.

Critical distinction:

```text
Ordinary ML:
Outlier → potentially remove

Anomaly Detection:
Outlier → potentially the target
```

---

# 14. Feature Selection

Investigate which sensors are useful.

Questions:

- Are all sensors needed?
- Are some redundant?
- Do digital signals help?
- Do continuous sensors dominate distance calculations?
- What happens if we remove highly correlated features?

Compare:

```text
All relevant sensors
        vs
Reduced sensor subset
```

The objective is understanding **how representation affects anomaly detection**.

---

# 15. Statistical Anomaly Detection

This should be our baseline.

Before advanced algorithms, implement simple statistical methods.

## 15.1 Z-Score

Understand:

```text
z = (x - μ) / σ
```

Investigate thresholds such as:

```text
|z| > threshold
```

Ask:

> What assumptions are we making?

Especially:

- approximate distribution assumptions
- mean/std sensitivity to outliers
- univariate nature

---

# 16. IQR Method

Use:

```text
IQR = Q3 - Q1

Lower = Q1 - 1.5 × IQR
Upper = Q3 + 1.5 × IQR
```

Investigate:

- which sensors produce many outliers
- effect of skewness
- comparison with z-score

This is primarily a **univariate baseline**.

---

# 17. Multivariate Statistical Thinking

After univariate methods, ask:

> What if no individual sensor is extreme, but the combination is unusual?

Critical transition:

```text
Univariate anomaly
        ↓
One feature looks unusual


Multivariate anomaly
        ↓
Combination of features is unusual
```

This motivates the machine-learning methods.

---

# 18. Isolation Forest

Isolation Forest is one of the main algorithms.

## Understand

```text
Randomly split the data
        ↓
Rare points get isolated quickly
        ↓
Common points require more splits
        ↓
Isolation → anomaly
```

## Experiments

Investigate:

- `n_estimators`
- `contamination`
- `max_samples`
- random seed

Observe:

- anomaly counts
- anomaly-score distributions
- detected time periods
- stability

---

# 19. Contamination — Important Experiment

Do not simply use the default contamination setting.

Investigate several plausible contamination levels based on the data.

Observe how changing contamination affects:

```text
Contamination
      ↓
Threshold
      ↓
Number of anomalies
      ↓
Failure-event coverage
      ↓
False alarms
```

Ask:

> Does setting contamination higher make the model better, or simply force more observations to be labeled anomalous?

---

# 20. Isolation Forest Anomaly Scores

Don't only look at:

```text
-1 = anomaly
 1 = normal
```

Investigate the underlying anomaly scores.

Plot:

```text
Anomaly score
      ↓
Distribution
      ↓
Potential threshold
```

This helps demonstrate that anomaly detection is often fundamentally a **scoring + thresholding problem**.

---

# 21. One-Class SVM

One-Class SVM should be used to learn the boundary of normal behavior.

Understand:

```text
Normal data
     ↓
Learn boundary
     ↓
Inside → normal
Outside → anomaly
```

## Experiments

Investigate:

- `nu`
- `gamma`
- kernel choice
- scaling

Focus on:

> **How does the boundary change when we change the parameters?**

---

# 22. One-Class SVM Computational Considerations

Because the dataset is large, we should **not blindly fit One-Class SVM on all 1.5M observations**.

This becomes an important practical lesson.

We may need to:

- sample training data
- use a representative subset
- experiment on a manageable training window
- compare computational cost

The goal is not to force a model to process every row regardless of practicality.

---

# 23. Local Outlier Factor (LOF)

LOF focuses on **local density**.

Core intuition:

```text
Point
 ↓
Compare its local density
with nearby points
 ↓
Much lower density
 ↓
Potential anomaly
```

This differs from simple global distance.

---

# 24. LOF Experiments

Investigate:

- `n_neighbors`
- contamination
- distance behavior
- anomaly-score distribution

Compare:

```text
small neighborhood
       vs
large neighborhood
```

Ask:

> Does changing the neighborhood size change which observations are considered anomalous?

---

# 25. Point Anomalies vs Contextual/Temporal Anomalies

This should be a major conceptual section.

### Point anomaly

```text
One observation is unusual.
```

### Contextual/temporal anomaly

```text
The value may be normal globally,
but unusual given the current operating context.
```

Example:

```text
Motor Current = 7A

Normally:
7A → normal when compressor is loaded

But:
7A → potentially unusual during an expected OFF state
```

This teaches an important limitation of standard tabular anomaly detectors.

---

# 26. Temporal Aggregation / Windows

Because the data are time-series, investigate whether raw point-level detection is enough.

Potential representations:

```text
Raw point
   ↓
Rolling mean
Rolling std
Rolling min/max
Change / difference
Window statistics
```

For example:

```text
5-minute window
    ↓
mean pressure
pressure variance
mean motor current
temperature change
```

This is an optional but highly valuable experiment if time permits.

The goal is:

> **Does detecting anomalous windows make more sense than detecting individual sensor readings?**

---

# 27. Failure-Period Evaluation

The dataset provides known failure periods.

Use them **after model training** to evaluate unsupervised detectors.

Conceptually:

```text
Detected anomaly periods
          ↓
Compare
          ↓
Known failure periods
```

Investigate:

- overlap
- detection before failure
- detection during failure
- missed failures
- false alarms

This is more informative than calculating only a generic anomaly score.

---

# 28. Important Evaluation Concepts

## False Positive

Model says:

```text
ANOMALY
```

but there is no known failure/event.

## False Negative

Model says:

```text
NORMAL
```

during a known failure period.

Both matter.

In predictive maintenance:

> Missing a serious failure may be much worse than generating some extra alerts.

But we should discuss this trade-off rather than assume one universal cost.

---

# 29. Point-Level vs Event-Level Evaluation

Suppose a failure lasts:

```text
6 hours
```

and the model detects 5 minutes within that period.

At point level:

```text
Most failure rows → missed
```

But operationally:

```text
Failure event → detected
```

Therefore distinguish:

### Point-level detection

Was this individual row anomalous?

### Event-level detection

Did we successfully identify the failure period?

This is a valuable real-world anomaly-detection lesson.

---

# 30. Evaluation Metrics

Where appropriate, investigate:

- Precision
- Recall
- F1-score
- Confusion matrix
- PR-AUC where meaningful
- ROC-AUC cautiously
- event-level detection rate
- false alarm rate
- detection delay

However:

> **Do not blindly optimize one metric.**

For anomaly detection, operational costs of false positives and false negatives matter.

---

# 31. Threshold Selection

Threshold selection should be a major experiment.

Instead of simply accepting:

```text
model.predict()
```

investigate:

```text
Anomaly Score
      ↓
Threshold
      ↓
Normal / Anomaly
```

Possible strategies:

- fixed quantile
- contamination-based threshold
- training-distribution threshold
- percentile-based threshold
- validation-based threshold, with known events used carefully and not as training labels

The key question:

> **Where should we place the boundary between normal and anomalous?**

---

# 32. Algorithm Comparison

At the end, compare:

| Method | Main Idea | Strengths | Weaknesses | Parameters | Result |
|---|---|---|---|---|---|
| Z-Score | Distance from mean | Simple | Distribution-sensitive | threshold | ... |
| IQR | Distribution spread | Robust baseline | Mostly univariate | multiplier | ... |
| Isolation Forest | Isolation | Scalable, multivariate | Parameter/threshold sensitivity | trees, contamination | ... |
| One-Class SVM | Normal boundary | Flexible boundary | Computationally expensive | nu, gamma, kernel | ... |
| LOF | Local density | Local anomalies | Neighborhood-sensitive | neighbors | ... |

The conclusion should **not** simply be:

> "Algorithm X had the highest F1."

Instead:

> **Which method is most appropriate for this industrial anomaly-detection problem, under what operating constraints, and why?**

---

# 33. Stability Analysis

Run important models with:

- different random seeds
- different contamination values
- different parameter settings
- different samples/windows where appropriate

Ask:

> Do the same time periods repeatedly appear anomalous?

Stable anomalies are more convincing than one-off detections.

---

# 34. Visualization

Visualizations should answer questions.

## Sensor Behavior

- sensor time-series
- selected failure periods
- operating-state transitions

## Statistical Methods

- distributions
- thresholds
- outliers

## Isolation Forest

- anomaly-score distribution
- anomaly points over time

## One-Class SVM

- score distribution
- selected feature-space visualization where feasible

## LOF

- local density/anomaly visualization
- score distribution

## Final Results

One of the key final visualizations should be:

```text
Sensor timeline
      +
Detected anomaly regions
      +
Known failure periods
```

---

# 35. Dimensionality Reduction

Dimensionality reduction is **supporting**, not the main topic.

Use PCA where useful for:

- understanding sensor variance
- visualizing normal vs suspicious regions
- investigating correlations

t-SNE/UMAP may optionally be used for exploratory visualization, but they should **not become the focus of this project**.

We should not assume that a 2D visualization faithfully represents anomaly structure.

---

# 36. Three-Day Structure

# DAY 1 — Understand the Industrial System + Build the Baseline

## Part 1 — Dataset Understanding

- Load dataset
- Understand sensor meanings
- Parse timestamps
- Sort chronologically
- Check missing values
- Understand time span
- Inspect failure reports

## Part 2 — Exploratory Time-Series Analysis

Investigate:

- sensor distributions
- time-series behavior
- operating regimes
- correlations
- sensor relationships
- failure periods

## Part 3 — Training/Test Strategy

Implement a chronological split:

```text
First month
    ↓
Training

Remaining months
    ↓
Testing
```

Investigate whether the training period contains known failure events.

## Part 4 — Preprocessing

- scaling
- sensor selection
- avoid deleting anomalies
- create a clean modeling representation

## Part 5 — Statistical Baselines

Implement:

- Z-score
- IQR

Compare:

- anomaly counts
- detected periods
- failure overlap

### Day 1 Goal

> **Understand what normal industrial behavior looks like and establish simple anomaly-detection baselines.**

---

# DAY 2 — Machine Learning Anomaly Detection

## Part 1 — Isolation Forest

Experiment with:

- contamination
- number of trees
- sample size
- random seeds
- anomaly scores

## Part 2 — One-Class SVM

Because of dataset size:

- use a manageable representative training subset
- experiment with `nu`
- experiment with `gamma`
- compare kernels where practical
- analyze computational behavior

## Part 3 — LOF

Experiment with:

- number of neighbors
- contamination
- local density
- anomaly scores

## Part 4 — Compare Methods

Investigate:

```text
Which observations
does each method
call anomalous?
```

This is more important than simply comparing scores.

### Day 2 Goal

> **Understand how different anomaly-detection algorithms define "abnormal."**

---

# DAY 3 — Evaluation + Temporal Analysis + Final Model

## Part 1 — Threshold Analysis

Investigate:

- score distributions
- thresholds
- contamination
- anomaly counts

## Part 2 — Failure Evaluation

Compare detections against:

- reported failure periods
- failure duration
- detection timing

## Part 3 — Event-Level Evaluation

Investigate:

- detected events
- missed events
- false alarms
- detection delay

## Part 4 — Temporal/Window Features

If time permits:

- rolling mean
- rolling std
- differences
- window-based features

Investigate whether these improve meaningful detection.

## Part 5 — Stability

Repeat important experiments.

## Part 6 — Final Comparison

Build the final method comparison.

## Part 7 — Final Interpretation

Answer:

- What constitutes an anomaly?
- Which algorithm worked best?
- Why?
- Which failure periods were detected?
- Which were missed?
- What false alarms occurred?
- What limitations remain?
- What would a real production system need?

### Day 3 Goal

> **Move from "the algorithm detected anomalies" to "we understand whether those anomalies are operationally meaningful."**

---

# 37. Scratch Implementation Policy

We are **not implementing the anomaly-detection algorithms from scratch**.

We will use established libraries such as:

```python
scikit-learn
```

The reason is deliberate.

The mathematical mechanisms have already been studied.

This project is about developing the practical ability to:

- prepare sensor data
- define normal behavior
- choose an anomaly detector
- tune its parameters
- interpret anomaly scores
- choose thresholds
- evaluate detections
- understand failure modes

We will still connect experiments back to the mathematical intuition.

---

# 38. Depth Standard

For every major method:

```text
1. Understand the method
       ↓
2. Establish a baseline
       ↓
3. Apply it to the sensor data
       ↓
4. Change important parameters
       ↓
5. Observe what changes
       ↓
6. Explain why
       ↓
7. Evaluate against known events
       ↓
8. Analyze false positives/negatives
       ↓
9. Compare with other methods
       ↓
10. Decide when it is appropriate
```

If we cannot explain **why a model detected a period as anomalous**, the experiment is not finished.

---

# 39. Expected Final Notebook Structure

```text
01. Project Objective
02. Dataset Introduction
03. Industrial System Overview
04. Anomaly Detection Problem Definition
05. Import Libraries
06. Load Dataset
07. Data Dictionary / Sensor Meaning
08. Timestamp Processing
09. Data Quality Investigation
10. Exploratory Data Analysis
11. Sensor Distributions
12. Time-Series Analysis
13. Operating Regime Analysis
14. Failure Event Analysis
15. Train/Test Strategy
16. Preprocessing
17. Feature Selection
18. Statistical Anomaly Detection
19. Z-Score
20. IQR Method
21. Statistical Baseline Evaluation
22. Isolation Forest
23. Isolation Forest Experiments
24. One-Class SVM
25. One-Class SVM Experiments
26. Local Outlier Factor
27. LOF Experiments
28. Anomaly Score Analysis
29. Threshold Selection
30. Point-Level Evaluation
31. Event-Level Evaluation
32. Failure Period Comparison
33. False Positive Analysis
34. False Negative Analysis
35. Temporal/Window Feature Experiment
36. Stability Analysis
37. PCA / Optional Visualization
38. Algorithm Comparison
39. Final Detection Strategy
40. Operational Interpretation
41. Limitations
42. Key Learnings
43. Final Conclusion
```

This is the **target structure**, not a requirement that every section becomes enormous.

---

# 40. Final Deliverables

By the end of the three days:

```text
Project_03_Industrial_Anomaly_Detection/
│
├── README.md
│
├── notebooks/
│   └── 01_Industrial_Anomaly_Detection.ipynb
│
├── data/
│   └── README.md
│
├── images/
│   └── important_visualizations/
│
└── requirements.txt
```

The raw CSV is approximately **208 MB**, so we should generally avoid committing the raw dataset directly to GitHub. The README should explain how to obtain it from UCI.

---

# 41. GitHub Quality

The GitHub project should communicate:

### Problem

What industrial anomaly problem are we solving?

### Dataset

What sensors do we have and where did the data come from?

### Normal Behavior

How did we define the training period?

### Methods

Which anomaly detectors did we use?

### Experiments

What happened when parameters changed?

### Evaluation

Did the detected anomalies overlap known failure events?

### Interpretation

Why were specific periods flagged?

### Limitations

What can these models not detect?

### Learning

What did the project teach us?

A strong project should make it possible to understand **why an alert was generated**, not just display a column containing `-1` and `1`.

---

# 42. LinkedIn Angle

The interesting story is not:

> "I used Isolation Forest on a dataset."

Instead:

> **I built an unsupervised industrial anomaly-detection pipeline using 1.5M+ multivariate sensor observations from a metro-train compressor. I compared statistical methods, Isolation Forest, One-Class SVM and LOF, investigated threshold sensitivity, and evaluated whether detected anomalies aligned with real reported failure periods.**

This communicates actual practical learning.

---

# 43. What Success Looks Like

At the end of Project 3, you should be able to answer:

- **What makes an observation anomalous?**
- **Why is anomaly detection different from classification?**
- **Why shouldn't we automatically remove outliers during preprocessing?**
- **What is the difference between a point anomaly and a contextual/temporal anomaly?**
- **Why can a combination of normal sensor values be anomalous?**
- **How does Z-score differ from IQR?**
- **How does Isolation Forest detect anomalies?**
- **What does contamination actually control?**
- **Why is One-Class SVM sensitive to scaling?**
- **What does `nu` represent?**
- **How does LOF detect local anomalies?**
- **Why does `n_neighbors` matter?**
- **Why might different algorithms flag different observations?**
- **How should anomaly thresholds be selected?**
- **Why is event-level evaluation important for industrial failures?**
- **How do you evaluate an unsupervised detector when labels are limited?**
- **What makes an anomaly detector useful in a real production system?**

If you can answer those from your own experiments, **the project has succeeded.**

---

# 44. Final Project Definition

| Item | Decision |
|---|---|
| **Project 3** | Industrial Anomaly Detection |
| **Dataset** | UCI MetroPT-3 |
| **Scale** | 1,516,948 observations, 15 sensor features |
| **Domain** | Metro train compressor / predictive maintenance |
| **Time** | ~3 days × 3–4 hours |
| **Primary Goal** | Practical understanding of anomaly detection |
| **Statistical Methods** | Z-Score, IQR |
| **ML Algorithms** | Isolation Forest, One-Class SVM, LOF |
| **Core Focus** | Normal behavior → anomaly scores → thresholds → evaluation |
| **Temporal Focus** | Yes |
| **Failure Reports** | Used for post-hoc evaluation, not primary training |
| **Scratch Implementation** | ❌ No |
| **GitHub** | ✅ |
| **LinkedIn-ready** | ✅ |
| **Dimensionality Reduction** | Supporting analysis only |
| **Project 1** | Clustering |
| **Project 2** | Association Rule Learning |
| **Project 3** | Anomaly Detection |

---

# Project Philosophy

The project follows:

> **Understand → Establish Normal → Detect → Experiment → Evaluate → Investigate → Compare → Interpret → Conclude**

Not:

> **Load dataset → fit Isolation Forest → mark -1 → done.**

The objective is to finish Project 3 with **practical intuition about anomaly detection**, including why different detectors disagree, how thresholds affect alerts, how time changes the meaning of an anomaly, and how to determine whether an alert is actually useful.
