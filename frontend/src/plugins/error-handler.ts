import { BaseError } from '@/types/errors'

export function setupGlobalErrors() {
    window.addEventListener('unhandledrejection', (event) => {
        if (event.reason instanceof BaseError) {
            event.reason.log('Unhandled rejection')
            event.preventDefault()
        }
    })
}
