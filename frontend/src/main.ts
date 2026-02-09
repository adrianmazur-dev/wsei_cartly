import { createApp } from 'vue'
import App from '@/App.vue'
import router from '@/router'
import pinia from '@/plugins/pinia'
import { setupPrimeVue } from '@/plugins/primevue'
import { setupGlobalErrors } from '@/plugins/error-handler'

import './assets/styles/style.css'

async function initApp() {
    const app = createApp(App)

    app.use(pinia)
    app.use(router)

    setupPrimeVue(app)

    setupGlobalErrors()

    app.mount('#app')
}

initApp()
