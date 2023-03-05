from pyspark.sql.functions import lower,  col


def string_to_lowercase(input_df, column):
    """
    Converts the values in a Spark dataframe column to lowercase.

    Args:
        input_df (pyspark.sql.DataFrame): The input dataframe to be modified.
        column (str): The name of the column to convert to lowercase.

    Returns:
        pyspark.sql.DataFrame: The output dataframe with the specified column converted to lowercase.

    """
    output_df = input_df.withColumn(column, lower(col(column)))
    return output_df
