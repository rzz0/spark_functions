from pyspark.sql.functions import col


def calculate_column(input_df, col1, col2, new_col):
    output_df = input_df.withColumn(new_col, col(col1) + col(col2))
    return output_df
