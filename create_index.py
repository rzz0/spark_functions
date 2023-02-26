from pyspark.sql.functions import dense_rank
from pyspark.sql.window import Window


def create_index(input_df, group_column, index_name):
    """
    Creates a group index column in a Spark dataframe based on a specified group column.
    """
    window = Window.partitionBy(group_column).orderBy(group_column)
    output_df = input_df.withColumn(index_name, dense_rank().over(window))
    return output_df
