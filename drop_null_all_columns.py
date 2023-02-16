from pyspark.sql.functions import col


def drop_nulls_in_all_columns(input_df):
    for column in input_df.columns:
        output_df = input_df.filter(col(column).isNotNull())
    return output_df
