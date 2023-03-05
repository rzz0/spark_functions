from pyspark.sql.functions import when, col


def fill_nulls(input_df, column, default_value):
    """
    Fills null values in a Spark dataframe column with a default value.

    Args:
        input_df (pyspark.sql.DataFrame): The input dataframe to be modified.
        column (str): The name of the column to fill null values in.
        default_value: The default value to use when filling null values.

    Returns:
        pyspark.sql.DataFrame: The output dataframe with null values in the specified column filled.

    """
    output_df = input_df.withColumn(column, when(
        col(column).isNull(), default_value).otherwise(col(column)))
    return output_df
