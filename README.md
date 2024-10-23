# biovariant

Pybiovariant is a bioinformatics tool designed for the analysis and management of genetic variants from VCF files using Python. It supports filtering genetic variants, storing them in PostgreSQL, querying specific variants, and visualizing allele frequency data via a web interface built with React.

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
- [React](https://reactjs.org/)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/handbob/pybiovariant.git
    cd pybiovariant
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```bash
      source venv/bin/activate
      ```

4. Install the required Python packages:
    ```bash
    cd backend && pip install -r requirements.txt
    ```

5. Configure the PostgreSQL database connection:
   - Create a `.env` file in the `backend` directory:
     ```bash
     touch .env
     ```
   - Add the following environment variables to the `.env` file:
     ```env
     DATABASE_NAME=biovariant
     DATABASE_USER=db_user
     DATABASE_PASSWORD=securepassword
     DATABASE_HOST=localhost
     DATABASE_PORT=5432
     ```
   - Fill in the values for your PostgreSQL setup.

6. Set up the PostgreSQL database:
    ```bash
    psql -U postgres -d biovariant -f backend/database/create_postgresql_tables.sql
    ```

## Description

This tool includes backend and frontend components.

The backend consists of Python scripts and a web server:

- **`load_to_databases.py`**: This script loads a VCF file, filters variants based on allele frequency, and stores the unique chromosomal positions in a PostgreSQL database. Functions:
  - `load_vcf()`: Reads the VCF file and filters variants.
  - `store_in_postgresql()`: Saves the filtered variants to PostgreSQL.

- **`server.py`**: A Flask or FastAPI backend API that serves the React front-end and provides access to PostgreSQL data. Functions:
  - `get_variants()`: Retrieves variants from PostgreSQL.
  - `get_variant_details()`: Fetches detailed information about a specific variant.

To run the backend server:
```bash
cd backend && python api/server.py
```

The frontend, built with React, includes the following components:

- **`VariantList.js`**: Displays a list of variants and allows searching by chromosome, position, or frequency.
- **`VariantDetail.js`**: Shows detailed information about a specific variant.

To run the frontend server:
```bash
cd frontend && npm run dev
```

## Features

- Filters genetic variants based on allele frequency from VCF files.
- Stores filtered variants in PostgreSQL for easy querying.
- Provides a React front-end for searching and viewing genetic variants.
- Displays graphical summary of allele frequency data.

## TODO

- [ ] Add more detailed unit tests for PostgreSQL operations.
- [ ] Implement frontend pagination for large datasets.
- [ ] Provide real-time data update in the React app using WebSockets.
- [ ] Add more detailed graphical visualizations of genetic data.

## DONE

- [x] Implement basic VCF filtering and storage in PostgreSQL.
- [x] Build React front-end for variant search and display.
