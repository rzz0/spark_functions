from pyspark.sql.functions import when


def replace_values_with_expression(input_df, col, expression, new_value):
    output_df = input_df.withColumn(
        col, when(expression, new_value).otherwise(col(col)))
    return output_df
