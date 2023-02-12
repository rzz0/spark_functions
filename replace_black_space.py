from pyspark.sql.functions import regexp_replace


def replace_blank_space(input_df, column_list):
    for column in column_list:
        output_df = input_df.withColumn(
            column, regexp_replace(column, r'\s', '_'))
        return output_df
