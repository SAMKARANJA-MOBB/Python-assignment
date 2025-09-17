# ---------------------------------------------------------
# Data Analysis & Visualization with pandas, matplotlib, seaborn
# Dataset: Iris
# ---------------------------------------------------------

# 1️⃣ Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2️⃣ Load and explore dataset
try:
    df = sns.load_dataset("iris")   # you can replace this with pd.read_csv("your_file.csv")
    print("✅ Dataset loaded successfully!\n")
except FileNotFoundError:
    print("❌ File not found. Please check your dataset path.")
    raise
except Exception as e:
    print("❌ An error occurred while loading the dataset:", e)
    raise

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head(), "\n")

# Check dataset info
print("Dataset Info:")
print(df.info(), "\n")

# Check missing values
print("Missing values per column:")
print(df.isnull().sum(), "\n")

# Clean missing values (if any)
df = df.dropna()

# 3️⃣ Basic data analysis
print("Descriptive Statistics:")
print(df.describe(), "\n")

print("Average Sepal Length per Species:")
print(df.groupby("species")["sepal_length"].mean(), "\n")

print("Observations:")
print("- Virginica flowers tend to have the longest sepal length.")
print("- Setosa flowers have the shortest.\n")

# 4️⃣ Data Visualizations
# ---------------------------------------------------------

# Line Chart: Sepal length over index (simulate time series)
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal_length"], label="Sepal Length", color="purple")
plt.title("Sepal Length Trend (Index as Time)")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.tight_layout()
plt.show()

# Bar Chart: Average petal length per species
avg_petal = df.groupby("species")["petal_length"].mean()

plt.figure(figsize=(7,5))
avg_petal.plot(kind="bar", color=["skyblue", "orange", "green"])
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Histogram: Distribution of sepal length
plt.figure(figsize=(7,5))
plt.hist(df["sepal_length"], bins=20, edgecolor="black")
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Scatter Plot: Sepal length vs Petal length
plt.figure(figsize=(7,5))
sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=df, s=70)
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.tight_layout()
plt.show()

# 5️⃣ Findings
print("SUMMARY & FINDINGS:")
print("- The dataset contains 150 rows and 5 columns.")
print("- There are no missing values after cleaning.")
print("- Virginica has the largest petals and sepals.")
print("- Sepal length and petal length are positively correlated.")
print("- Sepal length follows an approximately normal distribution.")
