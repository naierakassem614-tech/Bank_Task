import pandas as pd

def data_understanding(df):
    print("First 5 rows:")
    print(df.head())

    print("\nShape of dataset:")
    print(df.shape)

    print("\nColumn names:")
    print(df.columns)

    print("\nDataset info:")
    df.info()


def check_data_types(df):
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    cat_cols = df.select_dtypes(include=['object', 'string']).columns.tolist()

    print("\nNumerical columns:")
    print(num_cols)

    print("\nCategorical columns:")
    print(cat_cols)

    return num_cols, cat_cols


def missing_values_analysis(df):
    print("\nMissing values in each column:")
    print(df.isnull().sum())

    missing_table = pd.DataFrame({
        "Column": df.columns,
        "Null Count": df.isnull().sum().values,
        "Null Percentage": (df.isnull().mean() * 100).values
    })

    print("\nMissing Values Table:")
    print(missing_table)

    return missing_table