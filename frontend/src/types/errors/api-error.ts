import { BaseError } from './base-error'

export class ApiError extends BaseError {
    constructor(
        public status: number | null,
        message: string,
        details?: unknown,
    ) {
        super(message || 'API error occurred', details)
    }

    protected override getExtraInfo(): Record<string, unknown> {
        return { status: this.status }
    }
}
