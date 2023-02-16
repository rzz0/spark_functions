from pyspark.sql.functions import lower,  col


def string_to_lowercase(input_df, column):
    output_df = input_df.withColumn(column, lower(col(column)))
    return output_df
