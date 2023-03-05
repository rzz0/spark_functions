from pyspark.sql.functions import to_date, col


def string_to_date(input_df, column, date_format):
    """
    Converts a Spark dataframe column from string to date data type.

    Args:
        input_df (pyspark.sql.DataFrame): The input dataframe to be modified.
        column (str): The name of the column to be converted to date data type.
        date_format (str): The date format of the values in the column.

    Returns:
        pyspark.sql.DataFrame: The output dataframe with the specified column
        converted to date data type.

    """
    output_df = input_df.withColumn(column, to_date(col(column), date_format))
    return output_df
