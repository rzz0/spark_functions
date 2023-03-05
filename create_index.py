from pyspark.sql.functions import dense_rank
from pyspark.sql.window import Window


def create_index(input_df, group_column, index_name):
    """
    Creates a group index column in a Spark dataframe based on a specified group column.

    Args:
        input_df (pyspark.sql.DataFrame): The input dataframe to be modified.
        group_column (str): The name of the column to group by.
        index_name (str): The name of the new index column to be created.

    Returns:
        pyspark.sql.DataFrame: The output dataframe with the new group index column.

    """
    window = Window.partitionBy(group_column).orderBy(group_column)
    output_df = input_df.withColumn(index_name, dense_rank().over(window))
    return output_df
