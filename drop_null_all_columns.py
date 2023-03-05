from pyspark.sql.functions import col


def drop_nulls_in_all_columns(input_df):
    """
    Drops rows with null values in all columns of a Spark dataframe.

    Args:
        input_df (pyspark.sql.DataFrame): The input dataframe to be modified.

    Returns:
        pyspark.sql.DataFrame: The output dataframe with null rows dropped.

    """
    for column in input_df.columns:
        output_df = input_df.filter(col(column).isNotNull())
    return output_df
