from data_loader import load_data
from utils import data_understanding, check_data_types, missing_values_analysis
from data_cleaning import drop_columns_with_missing, drop_rows_with_missing, impute_missing_values
from visualization import (
    plot_age_histogram,
    plot_balance_boxplot,
    plot_duration_distribution,
    plot_job_count,
    plot_deposit_count,
    plot_deposit_vs_housing
)

def main():
    file_path = "bank.csv"

    df = load_data(file_path)

    data_understanding(df)

    num_cols, cat_cols = check_data_types(df)

    missing_values_analysis(df)

    drop_columns_with_missing(df, threshold=0.40)
    drop_rows_with_missing(df)
    df_imputed = impute_missing_values(df, num_cols, cat_cols)

    plot_age_histogram(df_imputed)
    plot_balance_boxplot(df_imputed)
    plot_duration_distribution(df_imputed)
    plot_job_count(df_imputed)
    plot_deposit_count(df_imputed)
    plot_deposit_vs_housing(df_imputed)

if __name__ == "__main__":
    main()