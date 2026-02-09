import { errorMiddleware, loggingMiddleware } from '@/backend/shared/middleware'
import createClient from 'openapi-fetch'
import type { Client, ClientOptions } from 'openapi-fetch'
import type { MediaType } from 'openapi-typescript-helpers'

export class ClientBase<T extends object> {
    private api: Client<T, MediaType>

    constructor(options: ClientOptions) {
        this.api = createClient<T>(options)

        this.api.use(loggingMiddleware)
        this.api.use(errorMiddleware)

        this.GET = this.api.GET
        this.POST = this.api.POST
        this.PUT = this.api.PUT
        this.DELETE = this.api.DELETE
        this.PATCH = this.api.PATCH
        this.HEAD = this.api.HEAD
    }

    public GET: Client<T, MediaType>['GET']
    public POST: Client<T, MediaType>['POST']
    public PUT: Client<T, MediaType>['PUT']
    public DELETE: Client<T, MediaType>['DELETE']
    public PATCH: Client<T, MediaType>['PATCH']
    public HEAD: Client<T, MediaType>['HEAD']

    public async send<T>(request: Promise<{ data?: T; response: Response; error?: unknown }>) {
        const { data, response } = await request
        return { data: data as T, response }
    }
}
