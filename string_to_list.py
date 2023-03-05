from pyspark.sql.functions import split, col


def string_to_list(input_df, column, sep):
    """
    Splits a Spark dataframe column into a list of values based on a specified separator.

    Args:
        input_df (pyspark.sql.DataFrame): The input dataframe to be modified.
        column (str): The name of the column to be split into a list of values.
        sep (str): The separator used to split the values in the column.

    Returns:
        pyspark.sql.DataFrame: The output dataframe with the specified column
        split into a list of values.

    """
    output_df = input_df.withColumn(column, split(col(column), sep))
    return output_df
