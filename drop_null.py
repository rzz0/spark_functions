from pyspark.sql.functions import col


def drop_nulls(input_df, column):
    output_df= input_df.filter(col(column).isNotNull())
    return output_df
