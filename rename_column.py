def rename_column(input_df, old, new):
    output_df = input_df.withColumnRenamed(old, new)
    return output_df
