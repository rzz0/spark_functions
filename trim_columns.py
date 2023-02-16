from pyspark.sql.functions import trim


def trim_columns(input_df):
    output_df = input_df.select([trim(col).alias(col) for col in input_df.columns])
    return output_df
