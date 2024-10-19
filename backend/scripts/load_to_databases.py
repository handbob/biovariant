import os
from cyvcf2 import VCF
import psycopg2

def load_vcf(file_path, frequency_threshold=0.01, batch_size=1000):
    '''Loads and filters variants from a VCF file.'''
    vcf_reader = VCF(file_path)
    filtered_variants = []
    total_records = 0

    for record in vcf_reader:
        total_records += 1
        if total_records % 10000 == 0:
            print(f'Processed {total_records} records...')

        af = record.INFO.get('AF', 0)

        if isinstance(af, tuple):
            af = af[0]

        if af >= frequency_threshold:
            filtered_variants.append(record)

        # Process in batches to avoid memory overload
        if len(filtered_variants) >= batch_size:
            yield filtered_variants
            filtered_variants = []

    # Yield any remaining records
    if filtered_variants:
        yield filtered_variants

def store_in_postgresql(variants):
    '''Stores variants in PostgreSQL.'''
    conn = psycopg2.connect(database='biovariant', user='postgres', password='postgres', host='localhost', port='5432')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS variants
                      (chromosome VARCHAR, position INTEGER, ref_allele VARCHAR, alt_allele VARCHAR);''')

    postgres_data = [(variant.CHROM, variant.POS, variant.REF, variant.ALT[0]) for variant in variants]
    args_str = ','.join(cursor.mogrify('(%s,%s,%s,%s)', variant).decode('utf-8') for variant in postgres_data)

    cursor.execute(f'INSERT INTO variants (chromosome, position, ref_allele, alt_allele) VALUES {args_str}')

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    import sys

    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the VCF file relative to the script directory
    vcf_file = os.path.join(script_dir, '..', 'data', 'ALL.chrY.phase3_integrated_v1a.20130502.genotypes.vcf.gz')

    # Optional: Check if the file exists before proceeding
    if not os.path.isfile(vcf_file):
        print(f"VCF file not found at: {vcf_file}")
        sys.exit(1)

    print(f'Using VCF file at: {vcf_file}')

    # Load and process variants in batches
    for variant_batch in load_vcf(vcf_file):
        store_in_postgresql(variant_batch)
        print(f'Stored batch of {len(variant_batch)} variants.')
