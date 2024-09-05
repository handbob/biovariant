from cyvcf2 import VCF
import psycopg2
from pymongo import MongoClient

def load_vcf(file_path, frequency_threshold=0.01):
    vcf_reader = VCF(file_path)
    filtered_variants = []

    for record in vcf_reader:
        af = record.INFO.get('AF', 0)

        if isinstance(af, tuple):
            af = af[0]

        if af >= frequency_threshold:
            filtered_variants.append(record)

    return filtered_variants

def store_in_postgresql(variants):
    conn = psycopg2.connect(database="biovariant", user="postgres", password="postgres", host="localhost", port="5432")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS variants
                      (chromosome VARCHAR, position INTEGER, ref_allele VARCHAR, alt_allele VARCHAR);''')

    for variant in variants:
        cursor.execute('''INSERT INTO variants (chromosome, position, ref_allele, alt_allele)
                          VALUES (%s, %s, %s, %s);''',
                       (variant.CHROM, variant.POS, variant.REF, variant.ALT[0]))

    conn.commit()
    cursor.close()
    conn.close()

def store_in_mongodb(variants):
    client = MongoClient('localhost', 27017)
    db = client['biovariant']
    collection = db['variants']

    for variant in variants:
        collection.insert_one({
            'chromosome': variant.CHROM,
            'position': variant.POS,
            'ref_allele': variant.REF,
            'alt_allele': variant.ALT[0],
            'info': dict(variant.INFO)
        })

if __name__ == "__main__":
    vcf_file = 'backend/data/genotypes.vcf.gz'
    variants = load_vcf(vcf_file)
    store_in_postgresql(variants)
    store_in_mongodb(variants)
