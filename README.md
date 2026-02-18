# PySpark Sales ETL

A robust Extract-Transform-Load (ETL) pipeline for processing and transforming sales data using Apache PySpark.

## Overview

This project implements a complete ETL workflow for sales data processing. It extracts raw sales data, applies transformations and validations, and loads the processed data into multiple output formats (CSV and Parquet).

## Project Structure

```
pyspark-sales-etl/
├── main.py                 # Entry point for running the ETL pipeline
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── configs/
│   └── schema.json        # Schema definitions for data validation
├── data/
│   ├── raw/               # Raw input data
│   │   └── sales.csv      # Source sales data
│   ├── curated/           # Intermediate processed data
│   └── output/            # Final output files
│       ├── sales_transformed.csv
│       └── sales_parquet/
├── jobs/
│   ├── __init__.py
│   ├── extract.py         # Data extraction logic
│   ├── transform.py       # Data transformation logic
│   └── load.py            # Data loading logic
└── spark/
    ├── __init__.py
    └── spark_session.py   # Spark session initialization and configuration
```

## Prerequisites

- Python 3.7 or higher
- Java 8 or higher (required for Spark)
- 4GB+ RAM (recommended for local development)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Deepanshusom/pyspark-sales-etl.git
cd pyspark-sales-etl
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

### Schema Configuration

The data schema is defined in [configs/schema.json](configs/schema.json) and includes:
- Column names and data types
- Validation rules
- Required fields specification

Modify this file to customize the schema for your specific data structure.

## Usage

### Running the ETL Pipeline

Execute the main script to run the complete ETL workflow:

```bash
python main.py
```

This will:
1. Extract data from `data/raw/sales.csv`
2. Apply transformations and validations
3. Load results to `data/output/` in both CSV and Parquet formats

### Individual Components

#### Extract
Handles data ingestion from raw sources:
- Reads CSV files
- Performs initial validation
- Creates Spark DataFrames

#### Transform
Applies business logic transformations:
- Data cleaning
- Aggregations
- Feature engineering
- Data validation

#### Load
Writes processed data to output destinations:
- CSV export for accessibility
- Parquet export for performance
- Multiple output formats support

## Output Formats

- **CSV**: Human-readable format stored in `data/output/sales_transformed.csv`
- **Parquet**: Columnar format for efficient querying in `data/output/sales_parquet/`

## Architecture

### Spark Session
Centralized Spark session management in [spark/spark_session.py](spark/spark_session.py):
- Configures Spark application settings
- Manages RDD and DataFrame APIs
- Handles executor and driver configurations

### Data Flow

```
Raw Data (CSV) 
    ↓
[Extract] → Spark DataFrame
    ↓
[Transform] → Cleaned & Transformed Data
    ↓
[Load] → CSV & Parquet Files
```

## Requirements

See [requirements.txt](requirements.txt) for the complete list of dependencies. Key packages include:
- **pyspark**: Apache Spark for distributed data processing
- **pandas**: For data manipulation and analysis
- **delta**: Delta Lake for ACID transactions (if applicable)

## Performance Considerations

- Parquet format provides better compression and query performance
- Parallel processing enabled by default through Spark
- CSV format suitable for cross-platform compatibility

## Troubleshooting

### Common Issues

1. **Java not found**: Ensure Java 8+ is installed and `JAVA_HOME` is set
2. **Out of memory**: Increase heap size or process data in batches
3. **File not found**: Verify `data/raw/sales.csv` exists before running

## Contributing

1. Create a feature branch
2. Make your changes
3. Submit a pull request

## License

This project is provided as-is for educational and business use.

## Contact

For issues or questions, please contact the project maintainer at [Deepanshusom](https://github.com/Deepanshusom).

---

**Last Updated**: February 18, 2026
