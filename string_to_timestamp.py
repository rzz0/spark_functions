from pyspark.sql.functions import to_timestamp, col


def string_to_timestamp(df, column):
    df = df.withColumn(column, to_timestamp(col(column)))
    return df
