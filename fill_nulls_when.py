from pyspark.sql.functions import when, col


def replace_nulls(input_df, column, default_value):
    """
    Replaces null values in a Spark dataframe column with a default value.

    Args:
        input_df (pyspark.sql.DataFrame): The input dataframe to be modified.
        column (str): The name of the column to replace null values in.
        default_value: The default value to use when replacing null values.

    Returns:
        pyspark.sql.DataFrame: The output dataframe with null values in the
        specified column replaced.

    """
    output_df = input_df.withColumn(column, when(
        col(column).isNull(), col(default_value)).otherwise(col(column)))
    return output_df
