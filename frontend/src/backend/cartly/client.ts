import { ClientBase } from '@/backend/shared/client-base'
import type { paths } from './schema'

export const cartlyClient = new ClientBase<paths>({
    baseUrl: '/api',
})
