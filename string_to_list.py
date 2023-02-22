from pyspark.sql.functions import split, col


def string_to_list(input_df, column, sep):
    output_df = input_df.withColumn(column, split(col(column), sep))
    return output_df
