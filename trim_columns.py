from pyspark.sql.functions import trim


def trim_columns(input_df):
    """
    Removes leading and trailing whitespaces from all columns in a Spark dataframe.

    Args:
        input_df (pyspark.sql.DataFrame): The input dataframe to be modified.

    Returns:
        pyspark.sql.DataFrame: The output dataframe with all columns trimmed
        of leading and trailing whitespaces.

    """
    output_df = input_df.select([trim(col).alias(col)
                                for col in input_df.columns])
    return output_df
