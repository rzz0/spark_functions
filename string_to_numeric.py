def string_to_numeric(input_df, column, data_type):
    """
    Converts the values in a Spark dataframe column from string to a specified
    numeric data type.

    Args:
        input_df (pyspark.sql.DataFrame): The input dataframe to be modified.
        column (str): The name of the column to be converted to numeric data type.
        data_type (str): The data type to which the column will be converted.

    Returns:
        pyspark.sql.DataFrame: The output dataframe with the specified column
        converted to the specified numeric data type.

    """
    output_df = input_df.withColumn(column, input_df[column].cast(data_type))
    return output_df
