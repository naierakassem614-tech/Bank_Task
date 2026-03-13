def drop_columns_with_missing(df, threshold=0.40):
    df_drop_col = df.loc[:, df.isnull().mean() <= threshold]
    print("\nShape after dropping columns with >40% missing:")
    print(df_drop_col.shape)
    return df_drop_col


def drop_rows_with_missing(df):
    before_rows = df.shape
    df_drop_rows = df.dropna()
    after_rows = df_drop_rows.shape

    print("\nDataset shape before dropping rows:")
    print(before_rows)

    print("\nDataset shape after dropping rows:")
    print(after_rows)

    return df_drop_rows


def impute_missing_values(df, num_cols, cat_cols):
    df_imputed = df.copy()

    for col in num_cols:
        df_imputed[col] = df_imputed[col].fillna(df_imputed[col].mean())

    for col in cat_cols:
        if df_imputed[col].isnull().sum() > 0:
            df_imputed[col] = df_imputed[col].fillna(df_imputed[col].mode()[0])

    print("\nMissing values after imputation:")
    print(df_imputed.isnull().sum())

    return df_imputed