def drop_columns(df, columns):
    df = df.drop(*columns)
    return df
