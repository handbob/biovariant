CREATE TABLE IF NOT EXISTS variants (
    id SERIAL PRIMARY KEY,
    chromosome VARCHAR(10),
    position INTEGER,
    ref_allele VARCHAR(255),
    alt_allele VARCHAR(255)
);
