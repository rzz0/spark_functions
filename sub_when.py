from pyspark.sql.functions import when


def replace_values_with_expression(df, column_name, expression, new_value):
    return df.withColumn(column_name, when(expression, new_value).otherwise(col(column_name)))
