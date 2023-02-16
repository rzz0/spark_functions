from pyspark.sql.functions import concat_ws, col


def merge_columns(input_df, column1, column2, new_column, sep):
    """
    Merges two columns in a Spark dataframe into a new column using a sep.

    """
    output_df = input_df.withColumn(new_column, concat_ws(
        sep, col(column1), col(column2)))
    return output_df
