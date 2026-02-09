import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'dashboard',
            component: () => import('@/views/DashboardView.vue'),
        },
        {
            path: '/lists/:id',
            name: 'list-detail',
            component: () => import('@/views/ShoppingListDetailView.vue'),
        },
    ],
})

router.beforeEach(async (to) => {
    return true
})

export default router
