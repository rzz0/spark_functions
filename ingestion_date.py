from pyspark.sql.functions import current_timestamp


def add_ingestion_date(input_df):
    """
    Adds a column to a Spark dataframe containing the current timestamp as the ingestion date.

    Args:
        input_df (pyspark.sql.DataFrame): The input dataframe to be modified.

    Returns:
        pyspark.sql.DataFrame: The output dataframe with a new ingestion date column added.

    """
    output_df = input_df.withColumn("ingestion_date", current_timestamp())
    return output_df
