from pyspark.sql.functions import concat_ws, col


def merge_columns(input_df, column1, column2, new_column, sep):
    """
    Merges two columns in a Spark dataframe into a new column using a specified separator.

    Args:
        input_df (pyspark.sql.DataFrame): The input dataframe to be modified.
        column1 (str): The name of the first column to merge.
        column2 (str): The name of the second column to merge.
        new_column (str): The name of the new column to create.
        sep (str): The separator to use when merging the columns.

    Returns:
        pyspark.sql.DataFrame: The output dataframe with the merged column added.

    """
    output_df = input_df.withColumn(new_column, concat_ws(
        sep, col(column1), col(column2)))
    return output_df
