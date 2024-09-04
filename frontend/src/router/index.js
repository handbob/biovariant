import { createRouter, createWebHistory } from 'vue-router';
import VariantList from '../components/VariantList.vue';
import VariantDetail from '../components/VariantDetail.vue';

const routes = [
  { path: '/', component: VariantList },
  { path: '/variant/:position', component: VariantDetail },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
