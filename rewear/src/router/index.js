import { createWebHistory, createRouter } from 'vue-router'

import HomeView from '../views/Home.vue'
import ShopView from '../views/Shop.vue'
import CreateView from '../views/Create.vue'

const routes = [
    { name: 'Home', path: '/', component: HomeView },
    { name: 'Shop', path: '/shop', component: ShopView },
    { name: 'Create', path: '/create', component: CreateView },
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
})

export default router;
