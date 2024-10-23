import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import '../styles/VariantList.css';

const VariantList = () => {
  const [variants, setVariants] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const variantsPerPage = 10;

  useEffect(() => {
    const fetchVariants = async () => {
      try {
        const response = await axios.get('/variants');
        setVariants(response.data);
      } catch (error) {
        console.error('Error fetching variants:', error);
      }
    };
    fetchVariants();
  }, []);

  const totalPages = Math.ceil(variants.length / variantsPerPage);

  const paginatedVariants = variants.slice(
    (currentPage - 1) * variantsPerPage,
    currentPage * variantsPerPage
  );

  const nextPage = () => {
    if (currentPage < totalPages) {
      setCurrentPage(currentPage + 1);
    }
  };

  const previousPage = () => {
    if (currentPage > 1) {
      setCurrentPage(currentPage - 1);
    }
  };

  return (
    <div className="container">
      <h1>Variant List</h1>
      <table>
        <thead>
          <tr>
            <th>Chromosome</th>
            <th>Position</th>
            <th>Reference Allele</th>
            <th>Alternate Allele</th>
            <th>Details</th>
          </tr>
        </thead>
        <tbody>
          {paginatedVariants.map((variant) => (
            <tr key={variant.position}>
              <td>{variant.chromosome}</td>
              <td>{variant.position}</td>
              <td>{variant.ref_allele}</td>
              <td>{variant.alt_allele}</td>
              <td>
                <Link to={`/variant/${variant.position}`} className="button">
                  View
                </Link>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* Pagination Controls */}
      <div className="pagination">
        <button onClick={previousPage} disabled={currentPage === 1}>
          Previous
        </button>
        <span>
          Page {currentPage} of {totalPages}
        </span>
        <button onClick={nextPage} disabled={currentPage === totalPages}>
          Next
        </button>
      </div>
    </div>
  );
};

export { VariantList };
