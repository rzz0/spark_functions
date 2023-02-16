from pyspark.sql.functions import when, col


def fill_nulls(input_df, column, default_value):
    """
    Fills null values in a Spark dataframe column with a default value.

    """
    output_df = input_df.withColumn(column, when(
        col(column).isNull(), default_value).otherwise(col(column)))
    return output_df
