<template>
  <div class="container">
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
        <tr v-for="variant in paginatedVariants" :key="variant.position">
          <td>{{ variant.chromosome }}</td>
          <td>{{ variant.position }}</td>
          <td>{{ variant.ref_allele }}</td>
          <td>{{ variant.alt_allele }}</td>
          <td>
            <router-link :to="'/variant/' + variant.position" class="button">View</router-link>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Pagination Controls -->
    <div class="pagination">
      <button @click="previousPage" :disabled="currentPage === 1">Previous</button>
      <span>Page {{ currentPage }} of {{ totalPages }}</span>
      <button @click="nextPage" :disabled="currentPage === totalPages">Next</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      variants: [],
      currentPage: 1,
      variantsPerPage: 10, // Number of variants per page
    };
  },
  computed: {
    paginatedVariants() {
      const start = (this.currentPage - 1) * this.variantsPerPage;
      const end = start + this.variantsPerPage;
      return this.variants.slice(start, end);
    },
    totalPages() {
      return Math.ceil(this.variants.length / this.variantsPerPage);
    },
  },
  mounted() {
    this.fetchVariants();
  },
  methods: {
    async fetchVariants() {
      try {
        const response = await axios.get('/variants');
        this.variants = response.data;
      } catch (error) {
        console.error('Error fetching variants:', error);
      }
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage += 1; // Replace `++` with `+= 1`
      }
    },
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage -= 1; // Replace `--` with `-= 1`
      }
    },
  },
};
</script>

<style scoped>
.container {
  width: 80%;
  margin: 20px auto;
  background-color: #fff;
  padding: 20px;
  box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

h1 {
  text-align: center;
  color: #007bff;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th, td {
  padding: 12px 15px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #007bff;
  color: white;
}

tr:hover {
  background-color: #f1f1f1;
}

.button {
  padding: 8px 12px;
  background-color: #007bff;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  text-align: center;
}

.button:hover {
  background-color: #0056b3;
}

/* Pagination Styles */
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}

button {
  padding: 8px 12px;
  margin: 0 5px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

button:hover:not(:disabled) {
  background-color: #0056b3;
}
</style>
