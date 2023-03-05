from pyspark.sql.functions import datediff, col


def date_diff(input_df, col1, col2, new_col):
    """
    Calculates the difference in days between two date columns in a Spark dataframe.

    Args:
        input_df (pyspark.sql.DataFrame): The input dataframe to be modified.
        col1 (str): The name of the first date column to use in the calculation.
        col2 (str): The name of the second date column to use in the calculation.
        new_col (str): The name of the new column to be created.

    Returns:
        pyspark.sql.DataFrame: The output dataframe with the new calculated column.

    """
    output_df = input_df.withColumn(new_col, datediff(col(col1), col(col2)))
    return output_df
