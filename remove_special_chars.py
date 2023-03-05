from pyspark.sql.functions import regexp_replace, col


def remove_special_chars(input_df, column_name):
    """
    Removes special characters from a column in a Spark dataframe.

    Args:
        input_df (pyspark.sql.DataFrame): The input dataframe to be modified.
        column_name (str): The name of the column to be modified.

    Returns:
        pyspark.sql.DataFrame: The output dataframe with special characters
        removed from the specified column.

    """
    output_df = input_df.withColumn(column_name, regexp_replace(
        col(column_name), "[^0-9a-zA-Z]+", ""))
    return output_df
