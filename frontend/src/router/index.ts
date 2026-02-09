import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [],
})

router.beforeEach(async (to) => {
    return true
})

export default router
