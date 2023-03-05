def rename_column(input_df, old_column, new_column):
    """
    Renames a column in a Spark dataframe.

    Args:
        input_df (pyspark.sql.DataFrame): The input dataframe to be modified.
        old_column (str): The name of the column to be renamed.
        new_column (str): The new name for the column.

    Returns:
        pyspark.sql.DataFrame: The output dataframe with the specified column renamed.

    """
    output_df = input_df.withColumnRenamed(old_column, new_column)
    return output_df
