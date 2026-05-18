# 📊 Data Visualization Cheat Sheet
> Quick revision guide covering Matplotlib, Seaborn, and Pandas plotting

---

## 🔧 Installation & Import

```python
pip install matplotlib
pip install seaborn

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
```

---

## 📐 Matplotlib Anatomy

| Term | Description |
|---|---|
| **Figure** | The overall window/page everything is drawn on |
| **Axes** | The area on which data is plotted (the actual plot) |
| **Axis** | Simply the x-axis and y-axis lines |
| **x-label** | Name of the x-axis |
| **y-label** | Name of the y-axis |
| **Major Ticks** | Subdivides the axis into major units |
| **Minor Ticks** | Subdivides major tick units further |
| **Title** | Title of each individual plot (Axes) |
| **Legend** | Describes elements in the plot (e.g. blue and green curves) |
| **Suptitle** | The common title of ALL plots (used in subplots) |

---

## 🎛️ Common Matplotlib Controls

```python
plt.figure(figsize=(15, 10))         # Set figure size

plt.xlabel('X Label Name')           # X axis label
plt.ylabel('Y Label Name')           # Y axis label

plt.title('Title of the plot')       # Title for single plot

fig.suptitle('Title of the figure')  # Title for all subplots

plt.xticks(rotation=90)              # Rotate x tick labels
plt.yticks(rotation=90)              # Rotate y tick labels

plt.legend()                         # Show legend
```

---

## 📦 Types of Data

```
Data
├── Categorical (Qualitative)
│   ├── Ordinal      → Has order     (e.g. low, medium, high)
│   └── Nominal      → No order      (e.g. gender: male/female)
│
└── Numerical (Quantitative)
    ├── Discrete     → Finite values  (e.g. year: 2010, 2011)
    └── Continuous   → Any value      (e.g. temperature, pressure)
```

---

## 🪟 Subplots

### Method 1 — `plt.subplot()` (positional)

```python
plt.figure(figsize=(20, 12)).suptitle("Sales by Region", fontsize=20)

plt.subplot(2, 3, 1)   # 2 rows, 3 cols, position 1
sns.scatterplot(x='NA_Sales', y='EU_Sales', data=df)

plt.subplot(2, 3, 3)
sns.scatterplot(x='NA_Sales', y='JP_Sales', data=df, color='red')

plt.subplot(2, 3, 4)
sns.scatterplot(x='NA_Sales', y='Other_Sales', data=df, color='green')

plt.subplot(2, 3, 6)
sns.scatterplot(x='NA_Sales', y='Global_Sales', data=df, color='orange')
```

### Method 2 — `plt.subplots()` (object-oriented, preferred)

```python
fig, ax = plt.subplots(2, 2, figsize=(20, 12))
fig.suptitle("Sales by Region", fontsize=20)

ax[0, 0].scatter(df['NA_Sales'], df['EU_Sales'])
ax[0, 1].scatter(df['NA_Sales'], df['JP_Sales'], color='red')
ax[1, 0].scatter(df['NA_Sales'], df['Other_Sales'], color='green')
ax[1, 1].scatter(df['NA_Sales'], df['Global_Sales'], color='orange')
```

> ✅ **Prefer Method 2** — direct axis access is cleaner and less error-prone.

---

## 04. Univariate Analysis
> Analyzing **one variable** at a time.

### A. Categorical Data

#### Count Plot (type of bar plot)
```python
sns.countplot(data=df, x='Genre')
```
Shows frequency of each category.

#### Pie Chart
```python
y = np.array([35, 25, 25, 15])
labels = ["Toyota", "Suzuki", "Mercedes", "Bugatti"]

plt.pie(y, labels=labels)
plt.show()
```

---

### B. Numerical Data

#### Histogram
```python
sns.histplot(data=df, x='Year')

# Pandas shorthand
df['Median'].plot(kind='hist')
```
Shows distribution / frequency of values in bins.

#### KDE Plot (Kernel Density Estimate)
```python
sns.kdeplot(data=df, x='Year')
```
Smooth version of histogram — shows the probability density curve.

#### Box Plot
```python
sns.boxplot(data=df, x='Global_Sales')
```
Shows median, quartiles, and outliers. Good for spotting skewness.

```
|---[  Q1 | median | Q3  ]---|   ← whiskers show range
            *                    ← outlier
```

---

## 05. Bivariate Analysis
> Analyzing **two variables** together.

### A. Numerical vs Numerical

#### Line Plot
```python
sns.lineplot(data=df, x='Year', y='NA_Sales')

# Pandas
df.plot(x='Rank', y='Median')
```
Best for trends over time.

#### Scatter Plot
```python
sns.scatterplot(data=df, x='Rank', y='Global_Sales')

# Pandas
df.plot(x='col1', y='col2', kind='scatter')
df.plot(x='Median', y='Unemployment_rate', kind='scatter')
```
Shows correlation/relationship between two numeric variables.

---

### B. Categorical vs Categorical

#### Dodged Bar Plot (grouped)
```python
sns.countplot(data=df, x='Publisher', hue='Platform')
```
Compare counts across two categories side by side.

#### Stacked Bar Plot
```python
sns.countplot(data=df, x='Publisher', hue='Genre', dodge=False)
```
Stacks categories on top of each other for proportional view.

---

### C. Categorical vs Numerical

#### Box Plot
```python
sns.boxplot(data=df, x='Publisher', y='Global_Sales')
```
Compare distribution of a numeric variable across categories.

#### Bar Plot (mean by default)
```python
sns.barplot(data=df, x='Genre', y='Global_Sales')

# Pandas
df['Major_category'].value_counts().plot(kind='bar')
```
Shows average (mean) of numeric variable per category.

---

## 06. Multivariate Analysis
> Analyzing **three or more variables** together.

### A. Numerical + Numerical + Categorical → Scatter with Color (Hue)

```python
sns.scatterplot(data=df, x='NA_Sales', y='EU_Sales', hue='Publisher')
```
Color encodes the third (categorical) variable.

---

### B. Categorical + Categorical + Numerical → Dodged Box Plot

```python
sns.boxplot(data=df, x='Publisher', y='Global_Sales', hue='Genre')
```
Compare distribution across two categorical variables.

---

### C. Numerical + Numerical + Numerical → Bubble Chart

```python
sns.scatterplot(
    data=df,
    x='NA_Sales',
    y='JP_Sales',
    size='Rank',
    sizes=(1, 200)       # min and max bubble size
)
```
Size of bubble encodes the third numeric variable.

---

## 🔗 Joint Plot
> Shows **two variables** with marginal distributions on the sides.

```python
sns.jointplot(x='NA_Sales', y='EU_Sales', data=df, hue='Genre')
```

Combines scatter plot + histogram/KDE on each axis — great for seeing both correlation and distribution at once.

---

## 🔁 Pair Plot
> Scatter plot for **every pair** of numeric columns in the dataset.

```python
sns.pairplot(data=df, hue='Genre')
```

- Diagonal shows distribution of each variable
- Off-diagonal shows scatter plot between pairs
- `hue` colors points by category

---

## 🌡️ Correlation & Heatmap

```python
# Compute correlation matrix and plot
sns.heatmap(df.corr(), cmap='Blues', annot=True)
```

| Parameter | Meaning |
|---|---|
| `df.corr()` | Computes pairwise correlation (-1 to 1) |
| `cmap` | Color map (e.g. `'Blues'`, `'coolwarm'`, `'RdYlGn'`) |
| `annot=True` | Show correlation values inside each cell |

**Interpreting values:**
```
 1.0  → perfect positive correlation
 0.0  → no correlation
-1.0  → perfect negative correlation
```

---

## 🐼 Plotting with Pandas (Quick Shorthand)

```python
# Line plot
df.plot(x='col1', y='col2')

# Scatter plot
df.plot(x='Median', y='Unemployment_rate', kind='scatter')

# Histogram
df['Median'].plot(kind='hist')

# Bar plot (categorical counts)
df['Major_category'].value_counts().plot(kind='bar')
```

---

## 🗺️ Quick Reference — Which Plot to Use?

| Goal | Variables | Plot |
|---|---|---|
| Distribution of one variable | 1 Numerical | Histogram, KDE, Boxplot |
| Frequency of categories | 1 Categorical | Countplot, Pie chart |
| Relationship between two numbers | 2 Numerical | Scatter, Line |
| Compare category vs number | 1 Cat + 1 Num | Boxplot, Barplot |
| Compare two categories | 2 Categorical | Dodged/Stacked Barplot |
| Three variables (color as 3rd) | 2 Num + 1 Cat | Scatter with hue |
| Three numeric variables | 3 Numerical | Bubble chart |
| All pairwise relationships | All columns | Pairplot |
| Correlation overview | All numerical | Heatmap |
| Two variables + their distributions | 2 Numerical | Jointplot |

---

## ⚡ Tips

- Use `figsize=(width, height)` to prevent cramped plots
- `hue` in seaborn adds a color-coded third dimension for free
- `annot=True` in heatmap is essential for readability
- `rotation=90` on ticks helps when x-labels are long category names
- Always label axes and add a title — unlabeled plots are useless in reports
- `dodge=False` in countplot stacks bars instead of grouping them
