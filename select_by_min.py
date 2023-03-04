from pyspark.sql.functions import min, col


def select_by_min(input_df, group_by, filter_column, filter_value):
    min_values = input_df.groupBy(group_by).agg(
        min(col(filter_column)).alias(filter_column))
    output_df = input_df.join(min_values, on=[group_by, filter_column]).filter(
        col(filter_column) == filter_value)
    return output_df
