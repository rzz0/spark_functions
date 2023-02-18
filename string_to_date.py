from pyspark.sql.functions import to_date, col


def string_to_date(input_df, column, date_format):
    output_df = input_df.withColumn(column, to_date(col(column), date_format))
    return output_df
