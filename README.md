# pybiovariant

pybiovariant is a bioinformatics tool designed for the analysis and management of genetic variants from VCF files using Python. It supports filtering genetic variants, storing them in PostgreSQL, querying specific variants, and visualizing allele frequency data via a web interface built with Vue.js.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Description](#description)
- [Features](#features)
- [TODO](#todo)
- [DONE](#done)

## Requirements

- [Python](https://www.python.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [MongoDB](https://www.mongodb.com/)
- [Vue.js](https://vuejs.org/)

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/handbob/pybiovariant.git
    cd pybiovariant
    ```

2. Set up a virtual environment:
    ```
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
      ```
      venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```
      source venv/bin/activate
      ```

4. Install the required Python packages:
    ```
    pip install -r backend/requirements.txt
    ```

5. Set up PostgreSQL and MongoDB databases. Create the necessary tables in PostgreSQL by running:
    ```
    psql -U postgres -d biovariant -f backend/database/create_postgresql_tables.sql
    ```

## Description

#### Backtend

### `load_to_postgresql.py`

This script loads a VCF file, filters variants based on allele frequency, and stores the unique chromosomal positions in a PostgreSQL database.

- **Functions**:
  - `load_vcf()`: Reads the VCF file and filters variants.
  - `store_in_postgresql()`: Saves the filtered variants to PostgreSQL.

### `load_to_mongodb.py`

This script retrieves specific variants from PostgreSQL and stores detailed information about them in MongoDB.

- **Functions**:
  - `retrieve_variants()`: Queries variants from PostgreSQL.
  - `store_in_mongodb()`: Saves the retrieved variants in MongoDB.

### `server.py`

A Flask or FastAPI backend API that serves the Vue.js front-end and provides access to PostgreSQL and MongoDB data.

- **Functions**:
  - `get_variants()`: Retrieves variants from PostgreSQL.
  - `get_variant_details()`: Fetches detailed information from MongoDB.

#### Frontend

- **Components**:
  - `VariantList.vue`: Displays a list of variants and allows searching by chromosome, position, or frequency.
  - `VariantDetail.vue`: Shows detailed information about a specific variant, pulled from MongoDB.

## Features

- Filters genetic variants based on allele frequency from VCF files.
- Stores filtered variants in PostgreSQL for easy querying.
- Retrieves and stores variant details in MongoDB.
- Provides a Vue.js front-end for searching and viewing genetic variants.
- Displays graphical summary of allele frequency data.

## TODO

- [ ] Add more detailed unit tests for MongoDB operations.
- [ ] Implement frontend pagination for large datasets.
- [ ] Provide real-time data update in the Vue.js app using WebSockets.
- [ ] Add more detailed graphical visualizations of genetic data.

## DONE

- [x] Implement basic VCF filtering and storage in PostgreSQL.
- [x] Set up MongoDB integration for storing variant details.
- [x] Build Vue.js front-end for variant search and display.
