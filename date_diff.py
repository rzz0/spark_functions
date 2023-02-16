from pyspark.sql.functions import datediff, col


def date_diff(input_df, col1, col2, new_col):
    """
    Calculates the difference in days between two date columns in a Spark dataframe.
    """
    output_df = input_df.withColumn(new_col, datediff(col(col1), col(col2)))
    return output_df
