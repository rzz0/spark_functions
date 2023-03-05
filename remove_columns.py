def drop_columns(input_df, cols_to_drop):
    """
    Drops specified columns from a Spark dataframe.

    Args:
        input_df (pyspark.sql.DataFrame): The input dataframe to be modified.
        cols_to_drop (list of str): The names of the columns to be dropped.

    Returns:
        pyspark.sql.DataFrame: The output dataframe with the specified columns removed.

    """
    output_df = input_df.drop(*cols_to_drop)
    return output_df
