import { createPinia } from 'pinia'
import { BaseError } from '@/types/errors/base-error'

const pinia = createPinia()

pinia.use(({ store }) => {
    store.$onAction(({ name, onError }) => {
        onError((error) => {
            if (error instanceof BaseError) {
                error.log(`Store: ${store.$id} | Action: ${name}`)
            }
        })
    })
})

export default pinia
