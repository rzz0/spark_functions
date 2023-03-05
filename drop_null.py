from pyspark.sql.functions import col


def drop_nulls(input_df, column):
    """
    Drops rows with null values in a specified column of a Spark dataframe.

    Args:
        input_df (pyspark.sql.DataFrame): The input dataframe to be modified.
        column (str): The name of the column to check for null values.

    Returns:
        pyspark.sql.DataFrame: The output dataframe with null rows dropped for the specified column.

    """
    output_df = input_df.filter(col(column).isNotNull())
    return output_df
