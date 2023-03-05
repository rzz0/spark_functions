from pyspark.sql.functions import when, col


def replace_values_with_expression(input_df, column, expression, new_value):
    """
    Replaces values in a Spark dataframe column based on a given expression.

    Args:
        input_df (pyspark.sql.DataFrame): The input dataframe to be modified.
        column (str): The name of the column to be modified.
        expression (pyspark.sql.Column): The expression to evaluate against the column.
        new_value (any): The value to replace the original value with when
        the expression is true.

    Returns:
        pyspark.sql.DataFrame: The output dataframe with the specified values
        replaced with the new value.

    """
    output_df = input_df.withColumn(column, when(
        expression, new_value).otherwise(col(column)))
    return output_df
