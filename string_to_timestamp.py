from pyspark.sql.functions import to_timestamp, col


def string_to_timestamp(input_df, column):
    """
    Converts a Spark dataframe column from string to timestamp data type.

    Args:
        input_df (pyspark.sql.DataFrame): The input dataframe to be modified.
        column (str): The name of the column to be converted to timestamp data type.

    Returns:
        pyspark.sql.DataFrame: The output dataframe with the specified column
        converted to timestamp data type.

    """
    output_df = input_df.withColumn(column, to_timestamp(col(column)))
    return output_df
