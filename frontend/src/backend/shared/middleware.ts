import type { Middleware } from 'openapi-fetch'
import { ApiError } from '@/types/errors'

export const loggingMiddleware: Middleware = {
    async onRequest({ request }) {
        console.log(`[API] ${request.method} ${request.url}`)
        return request
    },
    async onResponse({ response }) {
        console.log(`[API] ${response.status} ${response.url}`)
        return response
    },
    async onError({ error }) {
        console.error('[API] Network error:', error)
    },
}

export const errorMiddleware: Middleware = {
    async onResponse({ response }) {
        if (!response.ok) {
            throw new ApiError(response.status, `API request failed`, response)
        }
    },

    async onError({ error }) {
        return new ApiError(null, `Fetch error occurred`, error)
    },
}

