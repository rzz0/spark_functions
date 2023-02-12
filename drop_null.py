from pyspark.sql.functions import col


def drop_nulls(df, column):
    df = df.filter(col(column).isNotNull())
    return df
