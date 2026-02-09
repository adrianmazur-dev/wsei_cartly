export abstract class BaseError extends Error {
    public details: Record<string, unknown>
    public readonly timestamp: string

    constructor(message: string, details?: unknown) {
        super(message)
        this.name = new.target.name
        this.details = this.ensureObject(details)
        this.timestamp = new Date().toISOString()

        Object.setPrototypeOf(this, new.target.prototype)
    }

    public log(context?: string): void {
        const errorLog = this.toObject(context)
        console.error(`[${errorLog.name}] ${errorLog.message}`, errorLog)
    }

    public toObject(context?: string) {
        return {
            name: this.name,
            message: this.message,
            context: context || 'Global',
            timestamp: this.timestamp,
            details: this.details,
            ...this.getExtraInfo(),
        }
    }

    protected getExtraInfo(): Record<string, unknown> {
        return {}
    }

    private ensureObject(details: unknown): Record<string, unknown> {
        if (!details) return {}
        if (typeof details === 'object' && !Array.isArray(details))
            return details as Record<string, unknown>
        return { raw: details }
    }
}
