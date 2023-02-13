from pyspark.sql.functions import col

def calculate_new_column(df, column1, column2, new_column):
    df = df.withColumn(new_column, col(column1) + col(column2))
    return df