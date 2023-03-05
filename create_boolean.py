from pyspark.sql.functions import when


def create_boolean_column(input_df, column, expression):
    """
    Creates a new boolean column in a Spark dataframe based on a specified expression.

    Args:
        input_df (pyspark.sql.DataFrame): The input dataframe to be modified.
        column (str): The name of the new boolean column to be created.
        expression: The expression used to determine the value of the boolean column.

    Returns:
        pyspark.sql.DataFrame: The output dataframe with the new boolean column.

    """
    output_df = input_df.withColumn(
        column, when(expression, True).otherwise(False))
    return output_df
