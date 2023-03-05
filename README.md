# spark_functions

## Pyspark

The purpose of this repository is to help beginner developers learn about pyspark.

In this repository it is possible to find some functions in pyspark that can be used in an Extract, Transform and Load (ETL) process in a pipeline developed for the Databricks data platform under the context of Delta Lake.

The functions were developed in pyspark and are separated by file, containing documentation in a very didactic way for learning and fixing knowledge.


Function lists:

----
- calc_columns.py: function that performs calculations on columns of a Spark dataframe.
- create_boolean.py: function that creates a new boolean column in a Spark dataframe based on an expression.
- create_index.py: function that creates a new column in a Spark dataframe with an index based on a group of columns.
- date_diff.py: function that calculates the difference in days between two date columns in a Spark dataframe.
- drop_null.py: function that removes rows with null values in a specific column of a Spark dataframe.
- drop_null_all_columns.py: function that removes rows with null values in all columns of a Spark dataframe.
- fill_nulls.py: function that fills null values in a specific column of a Spark dataframe in Spark with a default value.
- fill_nulls_when.py: function that fills null values in a specific column of a Spark dataframe in Spark with a conditional value based on an expression.
- ingestion_date.py: function that adds a column with the current ingestion date and time in a Spark dataframe.
- merge_columns.py: function that merges two columns of a Spark dataframe into a new column with a specified separator.
- remove_columns.py: function that removes one or more columns from a Spark dataframe.
- remove_special_chars.py: function that removes special characters from a text column in a Spark dataframe.
- rename_column.py: function that renames a column in a Spark dataframe.
- replace_blank_space.py: function that replaces white spaces with underscores in one or more columns of a Spark dataframe.
- replace_string.py: function that replaces a value in a column of a Spark dataframe with a new specified value based on a conditional expression.
- select_by_min.py: function that selects rows from a Spark dataframe based on the minimum value in a column of a specific group of columns.
- string_lower.py: function that converts text in a column of a Spark dataframe to lowercase.
- string_to_date.py: function that converts a text column in a Spark dataframe to the specified date format.
- string_to_list.py: function that converts a text column in a Spark dataframe to a list using a specified separator.
- string_to_numeric.py: function that converts a text column in a Spark dataframe to a specified numeric data type.
- string_to_timestamp.py: function that converts a text column in a Spark dataframe to the specified date and time format.
- sub_when.py: function that replaces a value in a column of a Spark dataframe with a new specified value based on a conditional expression.
- trim_columns.py: function that removes white spaces at the beginning and end of all columns of a Spark dataframe.
----
