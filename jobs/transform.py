from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def transform_sales_data(df: DataFrame) -> DataFrame:
    """Clean and transform the sales DataFrame.

    - drop rows with nulls
    - add `total_amount` = quantity * price
    """
    df_clean = (
        df.dropna()
          .withColumn("total_amount", col("quantity") * col("price"))
    )
    return df_clean