from flask import Flask, jsonify
import psycopg2
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Database connection parameters
import os
db_params = {
    'database': os.getenv('DATABASE_NAME'),
    'user': os.getenv('DATABASE_USER'),
    'password': os.getenv('DATABASE_PASSWORD'),
    'host': os.getenv('DATABASE_HOST'),
    'port': os.getenv('DATABASE_PORT')
}

@app.route('/variants', methods=['GET'])
def get_variants():
    '''Fetch variants from PostgreSQL and return as JSON.'''
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        cursor.execute('SELECT chromosome, position, ref_allele, alt_allele FROM variants LIMIT 1000;')
        rows = cursor.fetchall()

        # Convert to list of dictionaries
        variants = [
            {
                'chromosome': row[0],
                'position': row[1],
                'ref_allele': row[2],
                'alt_allele': row[3]
            }
            for row in rows
        ]

        cursor.close()
        conn.close()

        return jsonify(variants)
    except Exception as e:
        print(f"Error fetching variants: {e}")
        return jsonify({'error': 'Failed to fetch variants'}), 500

# **Add this new route**
@app.route('/variant/<position>', methods=['GET'])
def get_variant(position):
    '''Fetch a single variant by position from PostgreSQL and return as JSON.'''
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT chromosome, position, ref_allele, alt_allele
            FROM variants
            WHERE position = %s;
        ''', (position,))
        row = cursor.fetchone()

        if row:
            variant = {
                'chromosome': row[0],
                'position': row[1],
                'ref_allele': row[2],
                'alt_allele': row[3]
            }
            return jsonify(variant)
        else:
            return jsonify({'error': 'Variant not found'}), 404
    except Exception as e:
        print(f"Error fetching variant: {e}")
        return jsonify({'error': 'Failed to fetch variant'}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(port=5001, debug=True)
