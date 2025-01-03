import React, { useState, useEffect } from "react";
import axios from "axios";
import { useParams, Link } from "react-router-dom";
import "../styles/VariantDetails.css";

class Variant {
  constructor(chromosome, position, ref_allele, alt_allele, info) {
    this.chromosome = chromosome;
    this.position = position;
    this.ref_allele = ref_allele;
    this.alt_allele = alt_allele;
    this.info = info;
  }
}

const VariantDetails = () => {
  const [variant, setVariant] = useState();
  const [error, setError] = useState();
  const { position } = useParams();

  useEffect(() => {
    const fetchVariant = async () => {
      try {
        const response = axios.get<Variant>(`http://localhost:5001/variant/${position}`);
        setVariant(response.data);
      } catch (error) {
        setError("Could not load the variant");
        console.error("Error fetching variant:", error);
      }
    };

    fetchVariant();
  }, [position]);

  if (variant) {
    return (
      <div className="container">
        <h2>Variant Details</h2>
        <p>
          <strong>Chromosome:</strong> {variant.chromosome}
        </p>
        <p>
          <strong>Position:</strong> {variant.position}
        </p>
        <p>
          <strong>Reference Allele:</strong> {variant.ref_allele}
        </p>
        <p>
          <strong>Alternate Allele:</strong> {variant.alt_allele}
        </p>
        <p>
          <strong>Additional Info:</strong>{" "}
          {variant.info ? JSON.stringify(variant.info) : "N/A"}
        </p>
        <Link to="/" className="button">
          Back to List
        </Link>
      </div>
    );
  } else if (error) {
    return (
      <div>
        <p>Error loading variant: {error}</p>
      </div>
    );
  } else {
    return (
      <div>
        <p>Loading...</p>
      </div>
    );
  }
};

export { VariantDetails };
