def string_to_numeric(input_df, column, data_type):
    """
    Converts a Spark dataframe column from string to a numeric data data_type.
    """
    output_df = input_df.withColumn(column, input_df[column].cast(data_type))
    return output_df
