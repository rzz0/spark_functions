from pyspark.sql.functions import lower,  col


def string_to_lowercase(df, column):
    df = df.withColumn(column, lower(col(column)))
    return df
