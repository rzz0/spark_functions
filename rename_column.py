def rename_column(df, old_name, new_name):
    df = df.withColumnRenamed(old_name, new_name)
    return df
