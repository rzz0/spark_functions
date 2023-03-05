from pyspark.sql.functions import when, col


def replace_string(input_df, column_name, old_str, new_str):
    """
    Replaces occurrences of a string in a column of a Spark dataframe.

    Args:
        input_df (pyspark.sql.DataFrame): The input dataframe to be modified.
        column_name (str): The name of the column to be modified.
        old_str (str): The string to be replaced.
        new_str (str): The string to replace the old string with.

    Returns:
        pyspark.sql.DataFrame: The output dataframe with the specified string
        replaced in the specified column.

    """
    output_df = input_df.withColumn(column_name, when(
        col(column_name) == old_str, new_str).otherwise(col(column_name)))
    return output_df
