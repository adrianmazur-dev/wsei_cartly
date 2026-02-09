import { type App } from 'vue'
import PrimeVue from 'primevue/config'
import Aura from '@primeuix/themes/material'

export function setupPrimeVue(app: App) {
    app.use(PrimeVue, {
        theme: {
            preset: Aura,
            options: {
                prefix: 'p',
                darkModeSelector: '.dark',
            },
        },
    })
}
