from pyspark.sql.functions import when


def create_boolean_column(input_df, column, expression):
    output_df = input_df.withColumn(
        column, when(expression, True).otherwise(False))
    return output_df
