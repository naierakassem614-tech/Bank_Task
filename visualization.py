import matplotlib.pyplot as plt
import seaborn as sns

def plot_age_histogram(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(df["age"], bins=20)
    plt.title("Histogram of Age")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.savefig("age_histogram.png")
    plt.show()


def plot_balance_boxplot(df):
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df["balance"])
    plt.title("Boxplot of Balance")
    plt.xlabel("Balance")
    plt.savefig("balance_boxplot.png")
    plt.show()


def plot_duration_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(df["duration"], bins=20)
    plt.title("Distribution of Duration")
    plt.xlabel("Duration")
    plt.ylabel("Count")
    plt.savefig("duration_distribution.png")
    plt.show()


def plot_job_count(df):
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x="job", order=df["job"].value_counts().index)
    plt.title("Bar Chart of Job")
    plt.xlabel("Job")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.savefig("job_count.png")
    plt.show()


def plot_deposit_count(df):
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x="deposit")
    plt.title("Bar Chart of Deposit")
    plt.xlabel("Deposit")
    plt.ylabel("Count")
    plt.savefig("deposit_count.png")
    plt.show()


def plot_deposit_vs_housing(df):
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="deposit", hue="housing")
    plt.title("Count Plot of Deposit vs Housing")
    plt.xlabel("Deposit")
    plt.ylabel("Count")
    plt.savefig("deposit_vs_housing.png")
    plt.show()