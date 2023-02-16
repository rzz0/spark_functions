def drop_columns(input_df, cols2):
    output_df = input_df.drop(*cols2)
    return output_df
