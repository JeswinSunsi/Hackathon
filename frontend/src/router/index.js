import { createWebHistory, createRouter } from 'vue-router'

import HomeView from '../views/Home.vue'
import LandingView from '../views/Landing.vue'
import CreateView from '../views/Create.vue'
import QuestionView from '../views/QuestionView.vue'

const routes = [
    { name: 'Home', path: '/', component: HomeView },
    { name: 'Shop', path: '/landing', component: LandingView },
    { name: 'Question', path: '/question/:id', component: QuestionView },
    { name: 'Create', path: '/create', component: CreateView },
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
})

export default router;
