from pyspark.sql.functions import to_timestamp, col


def string_to_timestamp(input_df, column):
    """
    Converts a string column to a timestamp column in a Spark dataframe.
    """
    output_df = input_df.withColumn(column, to_timestamp(col(column)))
    return output_df
