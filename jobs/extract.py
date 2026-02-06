from spark.spark_session import get_spark_session
from jobs.transform import transform_sales_data

def main():
    spark = get_spark_session("Sales ETL Project")

    df = spark.read.csv(
        "data/raw/sales.csv",
        header=True,
        inferSchema=True
    )

    print("=== RAW DATA ===")
    df.show()

    transformed_df = transform_sales_data(df)

    print("=== TRANSFORMED DATA ===")
    transformed_df.show()

    spark.stop()

if __name__ == "__main__":
    main()