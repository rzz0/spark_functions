from pyspark.sql.functions import when, col


def replace_nulls(input_df, column, default_value):
    """
    Replaces null values in a Spark dataframe column with a default value.
    """
    output_df = input_df.withColumn(column, when(
        col(column).isNull(), col(default_value)).otherwise(col(column)))
    return output_df
