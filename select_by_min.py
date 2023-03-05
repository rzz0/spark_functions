from pyspark.sql.functions import min, col


def select_by_min(input_df, group_by_column, filter_column, filter_value):
    """
    Selects rows in a Spark dataframe based on the minimum value of a specified
    column grouped by another column.

    Args:
        input_df (pyspark.sql.DataFrame): The input dataframe to be modified.
        group_by_column (str): The name of the column to group by.
        filter_column (str): The name of the column to filter by.
        filter_value (any): The value to filter on.

    Returns:
        pyspark.sql.DataFrame: The output dataframe with rows filtered by the
        minimum value of the specified column.

    """
    min_values = input_df.groupBy(group_by_column).agg(
        min(col(filter_column)).alias(filter_column))
    output_df = input_df.join(min_values, on=[group_by_column, filter_column]).filter(
        col(filter_column) == filter_value)
    return output_df
