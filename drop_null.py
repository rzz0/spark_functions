from pyspark.sql.functions import col


def drop_nulls(df, column_name):
    return df.filter(col(column_name).isNotNull())
