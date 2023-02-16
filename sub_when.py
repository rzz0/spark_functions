from pyspark.sql.functions import when, col


def replace_values_with_expression(input_df, column, expression, new_value):
    output_df = input_df.withColumn(
        column, when(expression, new_value).otherwise(col(column)))
    return output_df
