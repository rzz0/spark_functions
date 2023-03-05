from pyspark.sql.functions import regexp_replace


def replace_blank_space(input_df, column_list):
    """
    Replaces blank spaces in column names with underscores in a Spark dataframe.

    Args:
        input_df (pyspark.sql.DataFrame): The input dataframe to be modified.
        column_list (list of str): A list of column names to have blank spaces replaced.

    Returns:
        pyspark.sql.DataFrame: The output dataframe with blank spaces replaced by
        underscores in the specified columns.

    """
    for column in column_list:
        output_df = input_df.withColumn(
            column, regexp_replace(column, r'\s', '_'))
        return output_df
