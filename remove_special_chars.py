from pyspark.sql.functions import regexp_replace, col


def remove_special_chars(input_df, column_name):
    output_df = input_df.withColumn(column_name, regexp_replace(
        col(column_name), "[^0-9a-zA-Z]+", ""))
    return output_df
