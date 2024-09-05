<template>
  <div class="container" v-if="variant">
    <h2>Variant Details</h2>
    <p><strong>Chromosome:</strong> {{ variant.chromosome }}</p>
    <p><strong>Position:</strong> {{ variant.position }}</p>
    <p><strong>Reference Allele:</strong> {{ variant.ref_allele }}</p>
    <p><strong>Alternate Allele:</strong> {{ variant.alt_allele }}</p>
    <p><strong>Additional Info:</strong> {{ variant.info ? JSON.stringify(variant.info) : 'N/A' }}</p>
    <router-link to="/" class="button">Back to List</router-link>
  </div>
  <div v-else-if="error">
    <p>Error loading variant: {{ error }}</p>
  </div>
  <div v-else>
    <p>Loading...</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      variant: null,
      error: null,
    };
  },
  mounted() {
    const { position } = this.$route.params;
    this.fetchVariant(position);
  },
  methods: {
    async fetchVariant(position) {
      try {
        const response = await axios.get(`http://localhost:5001/variant/${position}`);
        this.variant = response.data;
      } catch (error) {
        this.error = 'Could not load the variant';
        console.error('Error fetching variant:', error);
      }
    },
  },
};
</script>

<style scoped>
.container {
  width: 60%;
  margin: 20px auto;
  background-color: #fff;
  padding: 20px;
  box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

h2 {
  text-align: center;
  color: #007bff;
}

p {
  font-size: 16px;
  line-height: 1.6;
}

.button {
  display: inline-block;
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  text-align: center;
}

.button:hover {
  background-color: #0056b3;
}
</style>
