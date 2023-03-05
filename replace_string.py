from pyspark.sql.functions import when, col


def replace_string(input_df, column, old, new):
    output_df = input_df.withColumn(column, when(
        col(column) == old, new).otherwise(col(column)))
    return output_df
